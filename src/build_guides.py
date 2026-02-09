#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from html.parser import HTMLParser

from cache_docs import fetch_urls
try:
    from bs4 import BeautifulSoup, Tag, NavigableString
except ImportError:
    import sys
    sys.exit("Error: 'bs4' module not found.\nPlease run 'python3 src/update_docs.py' to set up the environment, or verify you have activated the virtual environment (source .venv/bin/activate).")

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
    has_header: bool = False


@dataclass
class GuideDoc:
    url: str
    title: str
    summary: str | None
    blocks: list[Block]
    date: str | None = None


@dataclass
class GuidePage:
    url: str
    title: str
    summary: str | None
    category: str
    file: Path
    kind: str = "page"
    date: str | None = None


@dataclass
class ApiLinkIndex:
    docs_root: Path
    class_map: dict[str, Path]
    method_map: dict[tuple[str, str], Path]


API_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

API_CLASS_ALIASES = {
    "functions": "functionsapi",
    "input": "wireinput",
    "log": "wirelog",
}

API_VARIABLE_ALIASES = {
    "arrays": "wirearray",
    "array": "wirearray",
    "input": "wireinput",
}

API_REF_OVERRIDES = {
    "markuppagernav": "full/wire/modules/Markup/MarkupPagerNav/PagerNav/index.md",
}


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


def normalize_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def build_api_link_index(docs_root: Path) -> ApiLinkIndex | None:
    index_path = None
    full_index = docs_root / "api-full" / "_search.json"
    core_index = docs_root / "api-core" / "_search.json"
    if full_index.exists():
        index_path = full_index
    elif core_index.exists():
        index_path = core_index
    class_map: dict[str, Path] = {}
    method_map: dict[tuple[str, str], Path] = {}

    if index_path is not None:
        base_dir = index_path.parent
        try:
            data = json.loads(index_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}
        for item in data.get("items", []):
            item_type = item.get("type")
            if item_type in {"class", "file"}:
                name = item.get("name")
                file = item.get("file")
                if not name or not file:
                    continue
                class_map[normalize_key(name)] = base_dir / file
            elif item_type == "method":
                class_name = item.get("class")
                name = item.get("name")
                file = item.get("file")
                if not class_name or not name or not file:
                    continue
                method_map[(normalize_key(class_name), normalize_key(name))] = base_dir / file

    return ApiLinkIndex(
        docs_root=docs_root,
        class_map=class_map,
        method_map=method_map,
    )


def extract_api_path(url: str) -> tuple[str, str, str, bool]:
    raw = url.strip()
    if raw.startswith("api/"):
        raw = "/" + raw
    if raw.startswith("//"):
        parsed = urlparse("https:" + raw)
    elif re.match(r"^[a-z][a-z0-9+.-]*://", raw):
        parsed = urlparse(raw)
    elif raw.startswith("processwire.com/") or raw.startswith("www.processwire.com/"):
        parsed = urlparse("https://" + raw)
    else:
        parsed = urlparse(raw)

    path = parsed.path or ""
    is_processwire = "processwire.com" in (parsed.netloc or "").lower()
    if not is_processwire and "processwire.com" in path:
        idx = path.find("processwire.com")
        path = path[idx + len("processwire.com") :]
        if not path.startswith("/"):
            path = "/" + path
        is_processwire = True

    return path, parsed.query, parsed.fragment, is_processwire


def resolve_api_ref(path: str, index: ApiLinkIndex | None) -> Path | None:
    if index is None:
        return None
    remainder = path.split("/api/ref/", 1)[1].strip("/")
    if not remainder:
        target = index.docs_root / "api-full" / "index.md"
        if target.exists():
            return target
        target = index.docs_root / "api-core" / "index.md"
        return target if target.exists() else None

    parts = [p for p in remainder.split("/") if p]
    if not parts:
        return None

    class_key = normalize_key(parts[0])
    class_key = API_CLASS_ALIASES.get(class_key, class_key)
    override = API_REF_OVERRIDES.get(class_key)
    if override:
        override_path = index.docs_root / override
        if override_path.exists():
            return override_path
    class_target = index.class_map.get(class_key)
    if not class_target:
        return None

    if len(parts) == 1:
        return class_target

    method_key = normalize_key(parts[1])
    method_target = index.method_map.get((class_key, method_key))
    return method_target or class_target


def resolve_api_docs(path: str, index: ApiLinkIndex | None) -> Path | None:
    remainder = path.split("/api/", 1)[1].strip("/")
    if not remainder:
        return None

    docs_root = index.docs_root if index else None
    if docs_root:
        guide_candidate = docs_root / "guides" / "docs" / f"{remainder}.md"
        if guide_candidate.exists():
            return guide_candidate

    if remainder.startswith("variables/"):
        var_slug = remainder.split("/", 1)[1].strip("/")
        class_key = normalize_key(var_slug)
        class_key = API_VARIABLE_ALIASES.get(class_key, class_key)
        if index and class_key in index.class_map:
            return index.class_map[class_key]
        return None

    if remainder in {"arrays", "array"}:
        class_key = normalize_key("WireArray")
        if index and class_key in index.class_map:
            return index.class_map[class_key]
        return None

    return None


def rewrite_api_url(url: str, out_path: Path, index: ApiLinkIndex | None) -> str | None:
    path, query, fragment, is_processwire = extract_api_path(url)
    if not path:
        return None
    if not (is_processwire or path.startswith("/api/")):
        return None
    if not path.startswith("/api/"):
        return None

    target: Path | None
    if path.startswith("/api/ref/"):
        target = resolve_api_ref(path, index)
    else:
        target = resolve_api_docs(path, index)

    if target is None:
        return None

    rel = Path(os.path.relpath(target, start=out_path.parent)).as_posix()
    if query:
        rel = f"{rel}?{query}"
    if fragment:
        rel = f"{rel}#{fragment}"
    return rel


def rewrite_api_links(lines: list[str], out_path: Path, index: ApiLinkIndex | None) -> list[str]:
    if index is None:
        return lines
    updated: list[str] = []

    def repl(match: re.Match) -> str:
        text, url = match.group(1), match.group(2)
        new_url = rewrite_api_url(url, out_path, index)
        if new_url:
            return f"[{text}]({new_url})"
        return match.group(0)

    for line in lines:
        updated.append(API_LINK_RE.sub(repl, line))
    return updated



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

            # Skip block-level tags to avoid mashing their text into paragraphs
            if tag in BLOCK_TAGS and tag not in ("strong", "b", "em", "i", "a", "code", "span", "br", "u"):
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
                # Do NOT return, let it recurse if there are block children (buggy HTML)

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
                has_header = bool(element.find("thead") or element.find("th"))
                for tr in element.find_all("tr"):
                    if should_suppress(tr):
                        continue
                    cells = []
                    for td in tr.find_all(["td", "th"]):
                        if should_suppress(td):
                            continue
                        cells.append(normalize_text(get_clean_text(td)))
                    if cells:
                        rows.append(cells)
                if rows:
                    blocks.append(Block(kind="table", rows=rows, has_header=has_header))
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


BLOG_DATE_RE = re.compile(
    r"\b(\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})\b"
)


def is_blog_post_url(url: str) -> bool:
    parsed = urlparse(url)
    path = (parsed.path or "").rstrip("/")
    if not path.startswith("/blog/posts/"):
        return False
    slug = path[len("/blog/posts/") :]
    return bool(slug) and "/" not in slug


def parse_blog_date_text(text: str) -> str | None:
    if not text:
        return None
    match = BLOG_DATE_RE.search(text)
    if not match:
        return None
    date_text = match.group(1)
    try:
        return datetime.strptime(date_text, "%d %B %Y").strftime("%Y-%m-%d")
    except ValueError:
        return None


def extract_blog_post_date(html_text: str, soup: BeautifulSoup | None = None) -> str | None:
    if soup is not None:
        date_node = soup.find("li", class_="date")
        if date_node:
            parsed = parse_blog_date_text(date_node.get_text(" ", strip=True))
            if parsed:
                return parsed
    return parse_blog_date_text(html_text)


def strip_blog_extras(soup: BeautifulSoup) -> None:
    # Remove comments section
    for comment_list in soup.select("ul#comments, ul.CommentList"):
        heading = comment_list.find_previous(["h2", "h3", "h4", "h5"])
        if heading and "comment" in heading.get_text(" ", strip=True).lower():
            heading.decompose()
        comment_list.decompose()
    for comment_form in soup.select("form#CommentForm, form.CommentForm, .CommentForm"):
        comment_form.decompose()
    for comment_bits in soup.select(
        ".CommentListItem, .CommentHeader, .CommentFooter, .CommentText"
    ):
        comment_bits.decompose()

    # Remove prev/next post cards at the bottom
    for article in soup.select("article.blog-post-summary"):
        text = article.get_text(" ", strip=True).lower()
        if text.startswith("prev") or text.startswith("next"):
            article.decompose()
    for container in soup.select("div.blog-posts"):
        if not container.get_text(" ", strip=True):
            container.decompose()


def parse_html_doc(url: str, html_text: str) -> GuideDoc:
    meta_desc = extract_meta_description(html_text)
    main_html = extract_main_html(html_text)
    
    # Use html5lib to correctly handle implicitly closed tags (like <p>)
    soup = BeautifulSoup(main_html, "html5lib")

    post_date = None
    if is_blog_post_url(url):
        strip_blog_extras(soup)
        post_date = extract_blog_post_date(html_text, soup)
    
    blocks = extract_blocks_from_soup(soup)
    
    title = extract_title(html_text) or url
    
    for block in blocks:
        if block.kind == "heading" and block.level == 1:
             pass

    summary = None
    for block in blocks:
        if block.kind == "paragraph" and block.text:
            if is_blog_post_url(url) and is_blog_summary_noise(block.text):
                continue
            summary = block.text
            break
    if not summary:
        summary = meta_desc
        
    return GuideDoc(url=url, title=title, summary=summary, blocks=blocks, date=post_date)


def is_blog_summary_noise(text: str) -> bool:
    if not text:
        return False
    lowered = text.lower()
    if "comment" in lowered and " by " in lowered:
        return True
    if BLOG_DATE_RE.search(text) and " by " in lowered:
        return True
    return False


def maybe_wrap_code(text: str) -> str:
    """Wrap text in backticks if it looks like code and isn't already."""
    if not text:
        return text
    
    # If it's already wrapped or looks like markdown formatting, skip
    if text.startswith("`") or text.startswith("**") or text.startswith("*") or text.startswith("_"):
        return text

    # Heuristic for code: $var, ->method, function(), etc.
    # 1. Single tokens with code-like characters
    if " " not in text:
        if any(c in text for c in ("$", "->", "(", ")", "::", "[", "]", "=", ">", "<")) or text.endswith(".php"):
             return f"`{text}`"
    
    # 2. Short phrases that start with $ or contain -> (likely assignments or calls)
    if text.startswith("$") or "->" in text:
        # Code rarely has many spaces unless it's very verbose
        if text.count(" ") < 6:
             return f"`{text}`"

    return text


CODE_SNIPPET_RE = re.compile(
    r"(\$[A-Za-z_][A-Za-z0-9_]*(?:->\w+(?:\([^)]*\))?)?)"
)


def wrap_inline_code_snippets(text: str) -> str:
    if not text or "$" not in text:
        return text
    parts = text.split("`")
    for idx in range(0, len(parts), 2):
        parts[idx] = CODE_SNIPPET_RE.sub(r"`\1`", parts[idx])
    return "`".join(parts)


def wrap_table_key(text: str) -> str:
    if not text:
        return text
    if text.startswith("`") and text.endswith("`"):
        return text
    if " " not in text and len(text) <= 60:
        return f"`{text}`"
    return text


def render_markdown_table(rows: list[list[str]], has_header: bool = True) -> list[str]:
    """Render a List of Lists as a Markdown table."""
    if not rows:
        return []
    
    # Determine max cols
    max_cols = 0
    for row in rows:
        max_cols = max(max_cols, len(row))
    
    if max_cols == 0:
        return []

    # Prepare rows: escape pipes, wrap code (if short), ensure length
    clean_rows = []
    for row in rows:
        clean_row = []
        for idx, cell in enumerate(row):
            val = cell
            if not has_header and idx == 0:
                val = wrap_table_key(val)
            val = wrap_inline_code_snippets(val)
            val = val.replace("|", "\\|")
            val = maybe_wrap_code(val)
            clean_row.append(val)
        
        while len(clean_row) < max_cols:
            clean_row.append("")
        clean_rows.append(clean_row)

    lines = []
    
    header_row = []
    body_start_idx = 0

    if has_header:
        header_row = clean_rows[0]
        body_start_idx = 1
    else:
        # Markdown REQUIRES a header. If we don't have one, use generic or empty.
        # PW tables without headers are usually "Key | Value" or "Prop | Desc".
        # Let's use empty headers to be safe and clean.
        header_row = [""] * max_cols
        body_start_idx = 0

    # Header
    lines.append("| " + " | ".join(header_row) + " |")
    # Separator
    lines.append("| " + " | ".join(["---"] * max_cols) + " |")
    # Body
    for row in clean_rows[body_start_idx:]:
        lines.append("| " + " | ".join(row) + " |")
    
    return lines


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
                # Use real table if it has at least 2 columns and looks structured
                if any(len(row) > 1 for row in block.rows):
                    lines.extend(render_markdown_table(block.rows, has_header=block.has_header))
                else:
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


def url_to_out_path(url: str, date_prefix: str | None = None) -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "docs"

    if path == "docs" or path.startswith("docs/"):
        remainder = path[5:] if path.startswith("docs/") else ""
        if remainder:
            rel_path = f"documentation/{remainder}"
        else:
            rel_path = "documentation/index"
        return Path(f"{rel_path}.md")

    if path.startswith("blog/posts/") or path == "blog/posts":
        remainder = path[len("blog/posts/") :] if path.startswith("blog/posts/") else ""
        if remainder:
            parts = remainder.split("/")
            if date_prefix and parts:
                parts[-1] = f"{date_prefix}-{parts[-1]}"
            remainder = "/".join(parts)
            rel_path = f"blog-posts/{remainder}"
        else:
            rel_path = "blog-posts/index"
        return Path(f"{rel_path}.md")

    if date_prefix and is_blog_post_url(url):
        parts = path.split("/")
        if parts:
            parts[-1] = f"{date_prefix}-{parts[-1]}"
            path = "/".join(parts)
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
            if label.startswith("http://") or label.startswith("https://"):
                continue
            if current_name == "Blog" and label != "Blog":
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


def render_guide_page(doc: GuideDoc, out_path: Path, link_index: ApiLinkIndex | None = None) -> None:
    lines: list[str] = [f"# {doc.title}", "", f"Source: {doc.url}", ""]

    sections = build_sections(doc.blocks)
    if sections:
        lines.extend(["## Sections", ""])
        lines.extend(render_sections(sections, max_sections=None))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = rewrite_api_links(lines, out_path, link_index)
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
    link_index: ApiLinkIndex | None = None,
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
    lines = rewrite_api_links(lines, out_path, link_index)
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
    link_index: ApiLinkIndex | None = None,
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
    lines = rewrite_api_links(lines, out_path, link_index)
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
    link_index: ApiLinkIndex | None = None,
) -> GuidePage:
    lines: list[str] = ["# API Variables Map", ""]
    lines.append(f"Source: {variables_doc.url}")
    lines.append("")

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
    lines = rewrite_api_links(lines, out_path, link_index)
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
    link_index: ApiLinkIndex | None = None,
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
    lines = rewrite_api_links(lines, out_path, link_index)
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
        item = {
            "title": page.title,
            "url": page.url,
            "category": page.category,
            "file": Path(page.file).relative_to(root).as_posix(),
            "summary": page.summary,
            "kind": page.kind,
        }
        if page.date:
            item["date"] = page.date
        items.append(item)
    out_path.write_text(
        json.dumps({"items": items}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def build_search_index(pages: list[GuidePage], out_path: Path, root: Path) -> None:
    items = []
    for page in pages:
        item = {
            "title": page.title,
            "category": page.category,
            "file": Path(page.file).relative_to(root).as_posix(),
            "summary": page.summary,
            "kind": page.kind,
        }
        if page.date:
            item["date"] = page.date
        items.append(item)
    out_path.write_text(
        json.dumps({"items": items}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def extract_date_from_filename(path: Path) -> str | None:
    match = re.match(r"(\\d{4}-\\d{2}-\\d{2})-", path.name)
    if not match:
        return None
    return match.group(1)


def build_blog_index(pages: list[GuidePage], out_path: Path, root: Path) -> None:
    def sort_key(page: GuidePage) -> tuple[str, str]:
        date = page.date or extract_date_from_filename(page.file) or ""
        return (date, page.title.lower())

    lines: list[str] = ["# ProcessWire Blog Posts (Extracted)", ""]
    for page in sorted(pages, key=sort_key, reverse=True):
        date = page.date or extract_date_from_filename(page.file) or "unknown-date"
        rel_link = Path(os.path.relpath(page.file, start=out_path.parent))
        lines.append(f"- `{date}` [{page.title}]({rel_link.as_posix()})")
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build guide summaries from cached HTML")
    parser.add_argument("--cache", default="sources/docs-html", help="Cache root")
    parser.add_argument("--urls", default="sources/urls.txt", help="URL list")
    parser.add_argument("--out", default="docs", help="Output directory")
    parser.add_argument(
        "--fetch",
        action="store_true",
        help="Fetch HTML cache if missing or refresh existing",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.5,
        help="Sleep between requests in seconds (default: 0.5)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Request timeout in seconds (default: 30)",
    )
    args = parser.parse_args()

    cache_root = Path(args.cache)
    urls_path = Path(args.urls)
    out_dir = Path(args.out)
    link_index = build_api_link_index(out_dir)

    if args.fetch or not cache_root.exists() or not (cache_root / "_index.json").exists():
        try:
            fetch_urls(
                urls_path,
                cache_root,
                refresh=args.fetch,
                sleep=args.sleep,
                timeout=args.timeout,
                reporter=lambda msg: print(msg, file=sys.stderr),
            )
        except (FileNotFoundError, ValueError) as exc:
            raise SystemExit(str(exc))

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
            date_prefix = doc.date if is_blog_post_url(url) else None
            rel_out = url_to_out_path(url, date_prefix=date_prefix)
            page_path = out_dir / rel_out
            render_guide_page(doc, page_path, link_index=link_index)
            is_blog = is_blog_post_url(url)
            pages.append(
                GuidePage(
                    url=url,
                    title=doc.title,
                    summary=extract_summary_from_doc(doc),
                    category=category,
                    file=page_path,
                    kind="blog-post" if is_blog else "page",
                    date=doc.date if is_blog else None,
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
                out_dir / "documentation/cheatsheets/selectors.md",
                link_index=link_index,
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
                out_dir / "documentation/cheatsheets/templates-output.md",
                link_index=link_index,
            )
        )

    variables_doc = docs.get("https://processwire.com/docs/start/variables/")
    if variables_doc:
        core_index = out_dir / "api-core" / "index.md"
        pages.append(
            build_api_variables_map(
                variables_doc,
                core_index,
                out_dir / "documentation/cheatsheets/api-variables.md",
                link_index=link_index,
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
                out_dir / "documentation/cheatsheets/security.md",
                "Cheatsheets",
                link_index=link_index,
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
                out_dir / "documentation/cheatsheets/multi-language.md",
                "Cheatsheets",
                link_index=link_index,
            )
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    guides_root = out_dir / "documentation"
    guides_root.mkdir(parents=True, exist_ok=True)

    docs_pages = [p for p in pages if p.category != "Blog"]
    blog_pages = [p for p in pages if p.category == "Blog"]

    build_index(docs_pages, guides_root / "index.md")
    build_manifest(docs_pages, guides_root / "_manifest.json", out_dir)
    build_search_index(docs_pages, guides_root / "_search.json", out_dir)

    if blog_pages:
        blog_root = out_dir / "blog-posts"
        blog_root.mkdir(parents=True, exist_ok=True)
        build_blog_index(blog_pages, blog_root / "index.md", out_dir)
        build_manifest(blog_pages, blog_root / "_manifest.json", out_dir)
        build_search_index(blog_pages, blog_root / "_search.json", out_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
