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

try:
    from bs4 import BeautifulSoup, Tag, NavigableString
except ImportError:
    import sys
    sys.exit("Error: 'bs4' module not found.\nPlease run './scripts/update-docs.sh' to set up the environment, or verify you have activated the virtual environment (source .venv/bin/activate).")

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


def should_suppress(element: Tag) -> bool:
    for attr in ["id", "class"]:
        val = element.get(attr)
        if not val:
            continue
        if isinstance(val, list):
            val = " ".join(val)
        lowered = val.lower()
        for token in SUPPRESS_TOKENS:
            if token in lowered:
                return True
    return False


def normalize_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()



BLOCK_TAGS = set(HEADING_TAGS.keys()) | {"p", "ul", "ol", "table", "pre", "div", "section", "article", "main", "header", "footer", "nav", "aside", "blockquote", "li", "td", "th", "tr"}


def get_clean_text(element: Tag, separator: str = "\n") -> str:
    """
    Extract text from tag, respecting SUPPRESS_TOKENS and handling <br>,
    while converting inline formatting to Markdown.
    """
    texts = []
    for child in element.children:
        if isinstance(child, NavigableString):
            # Escape HTML characters to prevent them being interpreted as tags
            # We use quote=False because we don't need to escape quotes in markdown text
            texts.append(html.escape(str(child), quote=False))
        elif isinstance(child, Tag):
            tag = child.name.lower()
            
            if tag == "br":
                texts.append(separator)
                continue
            
            if should_suppress(child):
                continue
            
            if tag in IGNORE_TAGS:
                continue

            # Handle inline code
            if tag == "code":
                # For code, we want the raw text, but we wrap it in backticks.
                # We do NOT escape the content, because it's inside backticks.
                # But we definitely want to avoid it matching the backticks themselves.
                code_content = child.get_text()
                # Simple handling for backticks in code
                if "`" in code_content:
                    texts.append(f"`` {code_content} ``")
                else:
                    texts.append(f"`{code_content}`")
                continue

            # Recurse for others
            inner_text = get_clean_text(child, separator)
            
            # Formatting tags
            if tag in ("strong", "b"):
                 texts.append(f"**{inner_text}**")
            elif tag in ("em", "i"):
                 texts.append(f"*{inner_text}*")
            elif tag == "a":
                 # Extract href for links?
                 # For now, let's just keep the text to match previous behavior 
                 # or we could make it a link [text](href).
                 # The user wants guides, so links are valuable.
                 # Let's add link support if href exists.
                 href = child.get("href")
                 if href:
                     texts.append(f"[{inner_text}]({href})")
                 else:
                     texts.append(inner_text)
            else:
                 texts.append(inner_text)
                 
    return "".join(texts)


def extract_blocks_from_soup(soup: BeautifulSoup | Tag) -> list[Block]:
    blocks: list[Block] = []
    
    def walk(element: Tag | NavigableString):
        if isinstance(element, NavigableString):
            return

        if isinstance(element, Tag):
            tag_name = element.name.lower()
            
            if tag_name in IGNORE_TAGS:
                return
            
            if should_suppress(element):
                return

            # Handle headings
            if tag_name in HEADING_TAGS:
                text = normalize_text(get_clean_text(element, separator=" "))
                if text:
                    blocks.append(Block(kind="heading", text=text, level=HEADING_TAGS[tag_name]))
                return

            # Handle paragraphs
            if tag_name == "p":
                text = normalize_text(get_clean_text(element))
                if text:
                   blocks.append(Block(kind="paragraph", text=text))
                return

            # Handle lists
            if tag_name in ("ul", "ol"):
                items = []
                for li in element.find_all("li", recursive=False):
                    if should_suppress(li):
                        continue
                    text = normalize_text(get_clean_text(li))
                    if text and text.lower() not in {"learn more", "learn more →", "learn more →"}:
                        items.append(text)
                if items:
                    blocks.append(Block(kind="list", items=items))
                return

            # Handle tables
            if tag_name == "table":
                rows = []
                for tr in element.find_all("tr"):
                    if should_suppress(tr):
                        continue
                    cells = []
                    for td in tr.find_all(["td", "th"]):
                        if should_suppress(td):
                            continue
                        cells.append(normalize_text(get_clean_text(td)))
                    rows.append(cells)
                if rows:
                    blocks.append(Block(kind="table", rows=rows))
                return

            # Handle code blocks
            if tag_name == "pre":
                text = element.get_text() # Preserve whitespace for code
                if text:
                    blocks.append(Block(kind="code", text=text))
                return
            
            # Recurse for containers not handled above
            for child in element.children:
                walk(child)

    walk(soup)
    return blocks


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
    
    # Use html5lib to correctly handle implicitly closed tags (like <p>)
    soup = BeautifulSoup(main_html, "html5lib")
    
    blocks = extract_blocks_from_soup(soup)
    
    title = extract_title(html_text) or url
    
    for block in blocks:
        if block.kind == "heading" and block.level == 1:
             pass

    summary = None
    for block in blocks:
        if block.kind == "paragraph" and block.text:
            summary = block.text
            break
    if not summary:
        summary = meta_desc
        
    return GuideDoc(url=url, title=title, summary=summary, blocks=blocks)


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
