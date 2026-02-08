#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse
from html.parser import HTMLParser


IGNORE_TAGS = {"script", "style", "noscript"}
SUPPRESS_TOKENS = {
    "breadcrumb",
    "breadcrumbs",
    "nav",
    "menu",
    "footer",
    "sidebar",
    "content-side",
    "content-secondary",
    "content-meta",
    "jumplinks",
}
HEADING_TAGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4}


@dataclass
class Block:
    kind: str
    text: str | None = None
    level: int | None = None
    items: list[str] = field(default_factory=list)
    rows: list[list[str]] = field(default_factory=list)


@dataclass
class GuideDoc:
    url: str
    title: str
    summary: str | None
    blocks: list[Block]


@dataclass
class GuidePage:
    url: str
    title: str
    summary: str | None
    category: str
    file: Path
    kind: str = "page"


class GuideHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[Block] = []
        self.title: str | None = None
        self._stack: list[tuple[str, bool, bool]] = []
        self._suppress_depth = 0
        self._ignore_depth = 0
        self._current_tag: str | None = None
        self._current_text: list[str] = []
        self._list_depth = 0
        self._current_list: list[str] | None = None
        self._table_depth = 0
        self._current_row: list[str] | None = None
        self._current_cell: list[str] | None = None
        self._current_table: list[list[str]] | None = None
        self._in_pre = False
        self._block_start_tags = set(HEADING_TAGS.keys()) | {"p", "ul", "ol", "table", "pre"}

    def _push(self, tag: str, suppress: bool, ignore: bool) -> None:
        self._stack.append((tag, suppress, ignore))
        if suppress:
            self._suppress_depth += 1
        if ignore:
            self._ignore_depth += 1

    def _pop(self, tag: str) -> None:
        while self._stack:
            current_tag, suppress, ignore = self._stack.pop()
            if suppress:
                self._suppress_depth = max(self._suppress_depth - 1, 0)
            if ignore:
                self._ignore_depth = max(self._ignore_depth - 1, 0)
            if current_tag == tag:
                break

    def _is_suppressed(self) -> bool:
        return self._suppress_depth > 0 or self._ignore_depth > 0

    def _should_suppress(self, attrs: list[tuple[str, str | None]]) -> bool:
        for key, value in attrs:
            if value is None:
                continue
            if key in {"id", "class"}:
                lowered = value.lower()
                for token in SUPPRESS_TOKENS:
                    if token in lowered:
                        return True
        return False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        ignore = tag in IGNORE_TAGS
        suppress = self._should_suppress(attrs)
        self._push(tag, suppress, ignore)
        if ignore or self._is_suppressed():
            return

        if tag in self._block_start_tags:
            self._flush_current_tag()

        if tag in HEADING_TAGS:
            self._current_tag = tag
            self._current_text = []
            return
        if tag == "p":
            self._current_tag = tag
            self._current_text = []
            return
        if tag in {"ul", "ol"}:
            self._list_depth += 1
            if self._list_depth == 1:
                self._current_list = []
            return
        if tag == "li" and self._list_depth >= 1:
            self._current_tag = tag
            self._current_text = []
            return
        if tag == "table":
            self._table_depth += 1
            if self._table_depth == 1:
                self._current_table = []
            return
        if tag == "tr" and self._table_depth == 1:
            if self._current_cell is not None:
                text = normalize_text("".join(self._current_cell))
                if self._current_row is not None:
                    self._current_row.append(text)
                self._current_cell = None
            if self._current_row is not None and self._current_table is not None:
                self._current_table.append(self._current_row)
            self._current_row = []
            return
        if tag in {"td", "th"} and self._table_depth == 1:
            if self._current_cell is not None:
                text = normalize_text("".join(self._current_cell))
                if self._current_row is not None:
                    self._current_row.append(text)
            self._current_cell = []
            return
        if tag == "pre":
            self._in_pre = True
            self._current_tag = tag
            self._current_text = []
            return
        if tag == "br" and self._current_tag:
            self._current_text.append("\n")

    def handle_data(self, data: str) -> None:
        if self._is_suppressed():
            return
        if not data:
            return
        if self._current_cell is not None:
            self._current_cell.append(data)
            return
        if self._current_tag:
            self._current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in HEADING_TAGS and self._current_tag == tag:
            text = normalize_text("".join(self._current_text))
            if text:
                if tag == "h1" and self.title is None:
                    self.title = text
                else:
                    self.blocks.append(Block(kind="heading", text=text, level=HEADING_TAGS[tag]))
            self._current_tag = None
            self._current_text = []
        elif tag == "p" and self._current_tag == tag:
            text = normalize_text("".join(self._current_text))
            if text:
                self.blocks.append(Block(kind="paragraph", text=text))
            self._current_tag = None
            self._current_text = []
        elif tag == "li" and self._current_tag == tag:
            text = normalize_text("".join(self._current_text))
            if text and self._current_list is not None:
                if text.lower() not in {"learn more", "learn more →", "learn more →"}:
                    self._current_list.append(text)
            self._current_tag = None
            self._current_text = []
        elif tag in {"ul", "ol"}:
            if self._list_depth > 0:
                if self._list_depth == 1 and self._current_list:
                    self.blocks.append(Block(kind="list", items=self._current_list))
                self._list_depth = max(self._list_depth - 1, 0)
                if self._list_depth == 0:
                    self._current_list = None
        elif tag in {"td", "th"} and self._current_cell is not None:
            text = normalize_text("".join(self._current_cell))
            if self._current_row is not None:
                self._current_row.append(text)
            self._current_cell = None
        elif tag == "tr" and self._current_row is not None:
            if self._current_table is not None:
                self._current_table.append(self._current_row)
            self._current_row = None
        elif tag == "table" and self._table_depth > 0:
            if self._current_cell is not None:
                text = normalize_text("".join(self._current_cell))
                if self._current_row is not None:
                    self._current_row.append(text)
                self._current_cell = None
            if self._current_row is not None and self._current_table is not None:
                self._current_table.append(self._current_row)
                self._current_row = None
            if self._table_depth == 1 and self._current_table:
                self.blocks.append(Block(kind="table", rows=self._current_table))
            self._table_depth = max(self._table_depth - 1, 0)
            if self._table_depth == 0:
                self._current_table = None
        elif tag == "pre" and self._current_tag == tag:
            text = "".join(self._current_text)
            if text:
                self.blocks.append(Block(kind="code", text=text))
            self._current_tag = None
            self._current_text = []
            self._in_pre = False

        self._pop(tag)

    def _flush_current_tag(self) -> None:
        if not self._current_tag:
            return
        tag = self._current_tag
        if tag in HEADING_TAGS:
            text = normalize_text("".join(self._current_text))
            if text:
                if tag == "h1" and self.title is None:
                    self.title = text
                else:
                    self.blocks.append(Block(kind="heading", text=text, level=HEADING_TAGS[tag]))
        elif tag == "p":
            text = normalize_text("".join(self._current_text))
            if text:
                self.blocks.append(Block(kind="paragraph", text=text))
        elif tag == "li":
            text = normalize_text("".join(self._current_text))
            if text and self._current_list is not None:
                if text.lower() not in {"learn more", "learn more →", "learn more →"}:
                    self._current_list.append(text)
        elif tag == "pre":
            text = "".join(self._current_text)
            if text:
                self.blocks.append(Block(kind="code", text=text))

        self._current_tag = None
        self._current_text = []


def normalize_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_main_html(text: str) -> str:
    lower = text.lower()
    start = lower.find("<main")
    end = lower.find("</main>", start) if start != -1 else -1
    if start != -1 and end != -1:
        return text[start:end]
    start = lower.find("<article")
    end = lower.find("</article>", start) if start != -1 else -1
    if start != -1 and end != -1:
        return text[start:end]
    start = lower.find("<body")
    end = lower.find("</body>", start) if start != -1 else -1
    if start != -1 and end != -1:
        return text[start:end]
    return text


def extract_meta_description(text: str) -> str | None:
    match = re.search(
        r"<meta[^>]+name=[\"']description[\"'][^>]+content=[\"']([^\"']+)[\"']",
        text,
        re.I,
    )
    if not match:
        return None
    return normalize_text(match.group(1))


def extract_title(text: str) -> str | None:
    match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    if not match:
        return None
    return normalize_text(match.group(1))


def parse_html_doc(url: str, html_text: str) -> GuideDoc:
    meta_desc = extract_meta_description(html_text)
    main_html = extract_main_html(html_text)
    parser = GuideHTMLParser()
    parser.feed(main_html)
    title = parser.title or extract_title(html_text) or url
    summary = None
    for block in parser.blocks:
        if block.kind == "paragraph" and block.text:
            summary = block.text
            break
    if not summary:
        summary = meta_desc
    return GuideDoc(url=url, title=title, summary=summary, blocks=parser.blocks)


def render_table_as_list(rows: list[list[str]], max_rows: int = 40) -> list[str]:
    lines: list[str] = []
    for row in rows[:max_rows]:
        cells = [c for c in row if c]
        if not cells:
            continue
        lines.append(f"- {' — '.join(cells)}")
    return lines


def extract_key_points(blocks: list[Block], max_items: int = 5) -> list[str]:
    for block in blocks:
        if block.kind == "list" and block.items:
            return block.items[:max_items]
    points: list[str] = []
    for block in blocks:
        if block.kind == "paragraph" and block.text:
            points.append(block.text)
        if len(points) >= 3:
            break
    return points


def build_sections(blocks: list[Block]) -> list[tuple[int, str, list[Block]]]:
    sections: list[tuple[int, str, list[Block]]] = []
    current: list[Block] | None = None
    current_level = 2
    current_heading = "Overview"
    for block in blocks:
        if block.kind == "heading" and block.text:
            current_level = block.level or 2
            current_heading = block.text
            current = []
            sections.append((current_level, current_heading, current))
            continue
        if current is None:
            continue
        current.append(block)
    return sections


def render_sections(sections: list[tuple[int, str, list[Block]]], max_sections: int | None = None) -> list[str]:
    lines: list[str] = []
    
    # Filter sections if max_sections is set
    effective_sections = sections
    if max_sections is not None:
        effective_sections = sections[:max_sections]

    for level, heading, blocks in effective_sections:
        if not heading:
            continue
        header = "##" if level <= 2 else "###"
        lines.extend(["", f"{header} {heading}", ""])
        
        for block in blocks:
            if block.kind == "paragraph" and block.text:
                lines.append(block.text)
                lines.append("")
                continue
            if block.kind == "list" and block.items:
                for item in block.items:
                    lines.append(f"- {item}")
                lines.append("")
                continue
            if block.kind == "table" and block.rows:
                lines.extend(render_table_as_list(block.rows))
                lines.append("")
                continue
            if block.kind == "code" and block.text:
                # Basic code block detection/formatting
                lang = ""
                if "<?php" in block.text or "$pages->" in block.text:
                    lang = "php"
                lines.append(f"```{lang}")
                lines.append(block.text)
                lines.append("```")
                lines.append("")
                continue

        if lines and lines[-1] == "":
            continue
            
    if lines and lines[-1] == "":
        lines.pop()
    return lines


def url_to_cache_path(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc or "processwire.com"
    path = parsed.path or "/"
    if path.endswith("/"):
        path = f"{path}index.html"
    elif not path.endswith(".html"):
        path = f"{path}/index.html"
    if parsed.query:
        safe_query = parsed.query.replace("/", "_").replace("&", "_").replace("=", "-")
        path = f"{path}__{safe_query}"
    return f"{host}{path}"


def url_to_out_path(url: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "docs"
    if path.endswith("/"):
        path = path[:-1]
    return Path(f"{path}.md")


def load_url_groups(path: Path) -> list[tuple[str, list[str]]]:
    groups: list[tuple[str, list[str]]] = []
    current_name = "Other"
    current_urls: list[str] = []

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            label = line.lstrip("#").strip()
            if not label:
                continue
            lower = label.lower()
            if lower.startswith("processwire docs pages") or lower.startswith("one url per line"):
                continue
            if label:
                if current_urls:
                    groups.append((current_name, current_urls))
                current_name = label
                current_urls = []
            continue
        current_urls.append(line)

    if current_urls:
        groups.append((current_name, current_urls))
    return groups


def render_guide_page(doc: GuideDoc, out_path: Path) -> None:
    lines: list[str] = [f"# {doc.title}", "", f"Source: {doc.url}", ""]
    if doc.summary:
        lines.extend(["## Summary", "", doc.summary, ""])

    key_points = extract_key_points(doc.blocks)
    if key_points:
        lines.extend(["## Key Points", ""])
        for point in key_points:
            lines.append(f"- {point}")
        lines.append("")

    sections = build_sections(doc.blocks)
    if sections:
        lines.extend(["## Sections", ""])
        lines.extend(render_sections(sections, max_sections=None))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def extract_summary_from_doc(doc: GuideDoc) -> str | None:
    return doc.summary


def extract_operator_rows(doc: GuideDoc) -> list[list[str]]:
    for block in doc.blocks:
        if block.kind == "heading" and block.text:
            continue
        if block.kind == "table" and block.rows:
            return block.rows
    return []


def build_selectors_cheatsheet(
    selectors_doc: GuideDoc,
    operators_doc: GuideDoc,
    out_path: Path,
) -> GuidePage:
    lines: list[str] = ["# Selector Cheatsheet", ""]
    lines.append(f"Source: {selectors_doc.url}")
    lines.append(f"Source: {operators_doc.url}")
    lines.append("")

    if selectors_doc.summary:
        lines.extend(["## Selector Structure", "", selectors_doc.summary, ""])

    rows = extract_operator_rows(operators_doc)
    if rows:
        lines.extend(["## Operators", ""])
        lines.extend(render_table_as_list(rows, max_rows=80))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return GuidePage(
        url=operators_doc.url,
        title="Selector Cheatsheet",
        summary=selectors_doc.summary,
        category="Cheatsheets",
        file=out_path,
        kind="cheatsheet",
    )


def build_template_output_primer(
    pages_doc: GuideDoc,
    templates_doc: GuideDoc,
    fields_doc: GuideDoc,
    output_doc: GuideDoc,
    out_path: Path,
) -> GuidePage:
    lines: list[str] = ["# Templates, Fields & Output Primer", ""]
    lines.append(f"Source: {pages_doc.url}")
    lines.append(f"Source: {templates_doc.url}")
    lines.append(f"Source: {fields_doc.url}")
    lines.append(f"Source: {output_doc.url}")
    lines.append("")

    lines.extend(["## Core Concepts", ""])
    if pages_doc.summary:
        lines.append(f"- Pages: {pages_doc.summary}")
    if templates_doc.summary:
        lines.append(f"- Templates: {templates_doc.summary}")
    if fields_doc.summary:
        lines.append(f"- Fields: {fields_doc.summary}")

    if output_doc.summary:
        lines.extend(["", "## Output Strategies", "", output_doc.summary])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return GuidePage(
        url=output_doc.url,
        title="Templates, Fields & Output Primer",
        summary=output_doc.summary,
        category="Cheatsheets",
        file=out_path,
        kind="cheatsheet",
    )


def extract_api_variables(core_index: Path) -> list[tuple[str, str]]:
    if not core_index.exists():
        return []
    variables: list[tuple[str, str]] = []
    lines = core_index.read_text(encoding="utf-8").splitlines()
    in_api = False
    for line in lines:
        if line.strip() == "## API Variables":
            in_api = True
            continue
        if in_api and line.startswith("## "):
            break
        if not in_api:
            continue
        match = re.search(r"- `\$([^`]+)`(?: \[`[^`]+`\]\(([^)]+)\))?", line)
        if match:
            variables.append((match.group(1), match.group(2) or ""))
    return variables


def build_api_variables_map(
    variables_doc: GuideDoc,
    core_index: Path,
    out_path: Path,
) -> GuidePage:
    lines: list[str] = ["# API Variables Map", ""]
    lines.append(f"Source: {variables_doc.url}")
    lines.append("")

    if variables_doc.summary:
        lines.extend(["## Summary", "", variables_doc.summary, ""])

    variables = extract_api_variables(core_index)
    if variables:
        lines.extend(["## Variables", ""])
        seen = set()
        for name, link in variables:
            if name in seen:
                continue
            seen.add(name)
            if link:
                target = core_index.parent / link
                rel_link = Path(os.path.relpath(target, start=out_path.parent))
                lines.append(f"- ${name} ({rel_link.as_posix()})")
            else:
                lines.append(f"- ${name}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return GuidePage(
        url=variables_doc.url,
        title="API Variables Map",
        summary=variables_doc.summary,
        category="Cheatsheets",
        file=out_path,
        kind="cheatsheet",
    )


def build_checklist(
    title: str,
    docs: list[GuideDoc],
    out_path: Path,
    category: str,
) -> GuidePage:
    lines: list[str] = [f"# {title}", ""]
    for doc in docs:
        lines.append(f"Source: {doc.url}")
    lines.append("")
    lines.extend(["## Checklist", ""])
    for doc in docs:
        summary = doc.summary or ""
        summary = summary.rstrip(".")
        lines.append(f"- {doc.title}: {summary}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return GuidePage(
        url=docs[0].url if docs else "",
        title=title,
        summary=docs[0].summary if docs else None,
        category=category,
        file=out_path,
        kind="cheatsheet",
    )


def build_index(pages: list[GuidePage], out_path: Path) -> None:
    lines: list[str] = ["# ProcessWire Guides (Extracted)", ""]
    by_cat: dict[str, list[GuidePage]] = {}
    for page in pages:
        by_cat.setdefault(page.category, []).append(page)

    ordered = [
        "Cheatsheets",
        "Getting Started",
        "Front-end",
        "Selectors",
        "Modules & Hooks",
        "Fields",
        "Access Control",
        "Security",
        "Multi-language",
        "More Topics",
        "Tutorials",
        "Other",
    ]

    for cat in ordered:
        items = by_cat.get(cat)
        if not items:
            continue
        lines.append(f"## {cat}")
        lines.append("")
        for item in sorted(items, key=lambda p: p.title.lower()):
            rel_link = Path(os.path.relpath(item.file, start=out_path.parent))
            lines.append(f"- [{item.title}]({rel_link.as_posix()})")
        lines.append("")

    if lines and lines[-1] == "":
        lines.pop()
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_manifest(pages: list[GuidePage], out_path: Path, root: Path) -> None:
    items = []
    for page in pages:
        items.append(
            {
                "title": page.title,
                "url": page.url,
                "category": page.category,
                "file": Path(page.file).relative_to(root).as_posix(),
                "summary": page.summary,
                "kind": page.kind,
            }
        )
    out_path.write_text(
        json.dumps({"items": items}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def build_search_index(pages: list[GuidePage], out_path: Path, root: Path) -> None:
    items = []
    for page in pages:
        items.append(
            {
                "title": page.title,
                "category": page.category,
                "file": Path(page.file).relative_to(root).as_posix(),
                "summary": page.summary,
                "kind": page.kind,
            }
        )
    out_path.write_text(
        json.dumps({"items": items}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build guide summaries from cached HTML")
    parser.add_argument("--cache", default="cache/docs-html", help="Cache root")
    parser.add_argument("--urls", default="cache/urls.txt", help="URL list")
    parser.add_argument("--out", default="docs/guides", help="Output directory")
    args = parser.parse_args()

    cache_root = Path(args.cache)
    urls_path = Path(args.urls)
    out_dir = Path(args.out)

    if not cache_root.exists():
        raise SystemExit(f"Cache root not found: {cache_root}")
    if not urls_path.exists():
        raise SystemExit(f"URL list not found: {urls_path}")

    groups = load_url_groups(urls_path)
    docs: dict[str, GuideDoc] = {}
    pages: list[GuidePage] = []

    for category, urls in groups:
        for url in urls:
            cache_rel = url_to_cache_path(url)
            html_path = cache_root / cache_rel
            if not html_path.exists():
                continue
            html_text = html_path.read_text(encoding="utf-8", errors="replace")
            doc = parse_html_doc(url, html_text)
            docs[url] = doc
            rel_out = url_to_out_path(url)
            page_path = out_dir / rel_out
            render_guide_page(doc, page_path)
            pages.append(
                GuidePage(
                    url=url,
                    title=doc.title,
                    summary=extract_summary_from_doc(doc),
                    category=category,
                    file=page_path,
                )
            )

    # Cheatsheets
    selectors_doc = docs.get("https://processwire.com/docs/selectors/")
    operators_doc = docs.get("https://processwire.com/docs/selectors/operators/")
    if selectors_doc and operators_doc:
        pages.append(
            build_selectors_cheatsheet(
                selectors_doc,
                operators_doc,
                out_dir / "cheatsheets/selectors.md",
            )
        )

    pages_doc = docs.get("https://processwire.com/docs/start/structure/pages/")
    templates_doc = docs.get("https://processwire.com/docs/start/structure/templates/")
    fields_doc = docs.get("https://processwire.com/docs/start/structure/fields/")
    output_doc = docs.get("https://processwire.com/docs/front-end/output/")
    if pages_doc and templates_doc and fields_doc and output_doc:
        pages.append(
            build_template_output_primer(
                pages_doc,
                templates_doc,
                fields_doc,
                output_doc,
                out_dir / "cheatsheets/templates-output.md",
            )
        )

    variables_doc = docs.get("https://processwire.com/docs/start/variables/")
    if variables_doc:
        core_index = Path("docs/core/index.md")
        pages.append(
            build_api_variables_map(
                variables_doc,
                core_index,
                out_dir / "cheatsheets/api-variables.md",
            )
        )

    security_urls = [
        "https://processwire.com/docs/security/file-permissions/",
        "https://processwire.com/docs/security/admin/",
        "https://processwire.com/docs/security/web-hosting/",
        "https://processwire.com/docs/security/migration/",
        "https://processwire.com/docs/security/remove-unnecessary-files/",
        "https://processwire.com/docs/security/sessions/",
        "https://processwire.com/docs/security/third-party-modules/",
        "https://processwire.com/docs/security/template-files/",
        "https://processwire.com/docs/security/two-factor-authentication/",
    ]
    security_docs = [docs[url] for url in security_urls if url in docs]
    if security_docs:
        pages.append(
            build_checklist(
                "Security Checklist",
                security_docs,
                out_dir / "cheatsheets/security.md",
                "Cheatsheets",
            )
        )

    language_urls = [
        "https://processwire.com/docs/multi-language-support/",
        "https://processwire.com/docs/multi-language-support/code-i18n/",
        "https://processwire.com/docs/multi-language-support/multi-language-fields/",
        "https://processwire.com/docs/multi-language-support/multi-language-urls/",
        "https://processwire.com/docs/multi-language-support/multi-language-modules/",
    ]
    language_docs = [docs[url] for url in language_urls if url in docs]
    if language_docs:
        pages.append(
            build_checklist(
                "Multi-language Checklist",
                language_docs,
                out_dir / "cheatsheets/multi-language.md",
                "Cheatsheets",
            )
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    build_index(pages, out_dir / "index.md")
    build_manifest(pages, out_dir / "_manifest.json", out_dir)
    build_search_index(pages, out_dir / "_search.json", out_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
