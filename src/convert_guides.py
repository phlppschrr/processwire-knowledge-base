#!/usr/bin/env python3
import argparse
import html
import json
import re
import os
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

# Tags to ignore content from entirely
IGNORE_TAGS = {"script", "style", "noscript", "head", "iframe", "svg"}

# Classes or IDs to skip (navigation, footers, etc.)
SKIP_CLASSES = {
    "uk-breadcrumb", "uk-navbar", "uk-offcanvas", "uk-modal", 
    "pw-sidebar", "pw-footer", "pw-search-form", "pw-search-overlay",
    "pw-mobil-nav-toggle", "pw-logo", "pw-branding", "pw-search-icon",
    "uk-navbar-container", "uk-navbar-nav", "uk-navbar-left", "uk-navbar-right"
}

def normalize_text(text):
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text)
    return text

class MarkdownConverter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = []
        self._ignore_depth = 0
        self._pre_depth = 0
        self._list_stack = []  # Stores 'ul' or 'ol'
        self._list_counters = [] # Stores current count for OL, None for UL
        
        # Table handling
        self._in_table = False
        self._in_table_head = False
        self._table_rows = []
        self._current_row = []
        self._current_cell = [] # List of strings for current cell
        self._in_cell = False
        
        # Link handling
        self._current_href = None
        self._link_text_buffer = [] 
        
        self._last_tag = None

    def get_markdown(self):
        return "".join(self.output).strip()

    def _add_text(self, text, raw=False):
        if self._ignore_depth > 0:
            return
        
        if self._in_cell:
            self._current_cell.append(text)
            return

        # Buffer link text if we are inside a link
        if self._current_href is not None:
             # Normalize but don't output yet
             if not raw:
                 text = normalize_text(text)
             self._link_text_buffer.append(text)
             return

        if self._pre_depth > 0:
            self.output.append(text)
            return

        if not raw:
            text = normalize_text(text)
            
        if not text:
            return
            
        # Avoid double spaces
        if self.output and self.output[-1].endswith(' ') and text.startswith(' '):
            text = text.lstrip()
            
        self.output.append(text)

    def _ensure_newline(self, count=1):
        if self._ignore_depth > 0 or self._in_cell or self._current_href is not None:
            return
            
        current_newlines = 0
        if self.output:
            for i in range(len(self.output)-1, -1, -1):
                chunk = self.output[i]
                if chunk.endswith('\n'):
                    current_newlines += chunk.count('\n') # approximate, checking end is better
                    # Actually let's just checking trailing newlines
                    stripped = chunk.rstrip('\n')
                    current_newlines += len(chunk) - len(stripped)
                    if stripped: break
                elif not chunk.strip():
                    continue # Empty chunk
                else:
                    break
                    
        # Simplified check: just look at the last few chars
        joined = "".join(self.output[-3:])
        existing = 0
        for c in reversed(joined):
            if c == '\n': existing += 1
            elif c.isspace(): continue
            else: break
            
        needed = count - existing
        if needed > 0:
            self.output.append('\n' * needed)

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        ids = attrs_dict.get('id', '')
        
        # Check for suppression
        if tag in IGNORE_TAGS or any(c in SKIP_CLASSES for c in classes) or ids in SKIP_CLASSES:
            self._ignore_depth += 1
            return

        if self._ignore_depth > 0:
            self._ignore_depth += 1
            return
        
        self._last_tag = tag

        # Structuring
        if tag in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self._ensure_newline(2)
            level = int(tag[1])
            self.output.append('#' * level + ' ')

        elif tag == 'p':
            self._ensure_newline(2)

        elif tag == 'ul':
            self._ensure_newline(1 if self._list_stack else 2)
            self._list_stack.append('ul')
            self._list_counters.append(None)

        elif tag == 'ol':
            self._ensure_newline(1 if self._list_stack else 2)
            self._list_stack.append('ol')
            self._list_counters.append(1)

        elif tag == 'li':
            self._ensure_newline(1)
            indent = '  ' * (len(self._list_stack) - 1)
            if self._list_stack:
                if self._list_stack[-1] == 'ol':
                    idx = self._list_counters[-1]
                    self.output.append(f"{indent}{idx}. ")
                    self._list_counters[-1] += 1
                else:
                    self.output.append(f"{indent}- ")

        elif tag == 'pre':
            self._ensure_newline(2)
            self._pre_depth += 1
            self.output.append("```\n")

        elif tag == 'code':
            if self._pre_depth == 0:
                 self.output.append('`')
            # Inside pre, code tag is usually redundant for formatting but maybe has lang class
            # We could parse lang here but let's keep it simple

        elif tag == 'blockquote':
            self._ensure_newline(2)
            self.output.append('> ')

        elif tag == 'br':
            self.output.append('\n')

        elif tag == 'hr':
            self._ensure_newline(2)
            self.output.append('---')
            self._ensure_newline(2)

        # Inline Formatting
        elif tag in {'b', 'strong'}:
            self.output.append('**')
        elif tag in {'i', 'em'}:
            self.output.append('*')

        # Links
        elif tag == 'a':
            href = attrs_dict.get('href', '')
            self._current_href = href
            self._link_text_buffer = []

        # Tables
        elif tag == 'table':
            self._ensure_newline(2)
            self._in_table = True
            self._table_rows = []

        elif tag == 'thead':
            self._in_table_head = True

        elif tag == 'tr':
            self._current_row = []

        elif tag in {'td', 'th'}:
            self._in_cell = True
            self._current_cell = []

    def handle_endtag(self, tag):
        if self._ignore_depth > 0:
            self._ignore_depth -= 1
            return

        # Structuring
        if tag in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self._ensure_newline(2)

        elif tag == 'p':
            self._ensure_newline(2)

        elif tag in {'ul', 'ol'}:
            if self._list_stack:
                self._list_stack.pop()
                self._list_counters.pop()
            self._ensure_newline(2)

        elif tag == 'li':
            self._ensure_newline(1)

        elif tag == 'pre':
            self.output.append("\n```")
            self._ensure_newline(2)
            self._pre_depth -= 1

        elif tag == 'code':
            if self._pre_depth == 0:
                self.output.append('`')

        elif tag == 'blockquote':
            self._ensure_newline(2)

        # Inline Formatting
        elif tag in {'b', 'strong'}:
             if self.output and self.output[-1] == '**': 
                 self.output.pop() # empty bold
             else:
                 self.output.append('**')
        elif tag in {'i', 'em'}:
             if self.output and self.output[-1] == '*':
                 self.output.pop() # empty italics
             else:
                 self.output.append('*')

        # Links
        elif tag == 'a':
            if self._current_href is not None:
                text = "".join(self._link_text_buffer).strip()
                if not text: text = self._current_href
                # Escape brackets in text to avoid breaking markdown
                text = text.replace('[', '\\[').replace(']', '\\]')
                self.output.append(f"[{text}]({self._current_href})")
                self._current_href = None
                self._link_text_buffer = []

        # Tables
        elif tag in {'td', 'th'}:
            if self._in_cell:
                cell_content = normalize_text("".join(self._current_cell))
                # Escape pipes in tables
                cell_content = cell_content.replace('|', '\\|')
                self._current_row.append(cell_content)
                self._in_cell = False
                self._current_cell = []

        elif tag == 'tr':
            if self._in_table:
                self._table_rows.append(self._current_row)
                
                # If we are in head or it's the first row and we haven't seen head, render separators later
                if self._in_table_head:
                    pass # Mark as header row implicitly by being in thead or first row logic
                
        elif tag == 'thead':
            self._in_table_head = False

        elif tag == 'table':
            self._in_table = False
            self._render_table()
            self._ensure_newline(2)

    def _render_table(self):
        if not self._table_rows:
            return
            
        # Normalize column count
        max_cols = max(len(r) for r in self._table_rows)
        
        # Render rows
        for i, row in enumerate(self._table_rows):
            # Pad row
            while len(row) < max_cols:
                row.append("")
                
            line = "| " + " | ".join(row) + " |"
            self.output.append(line + "\n")
            
            # Assume first row is header if we found a thead OR if it's just the first row (common convention)
            # But let's only do it if we are conceptually separating headers. 
            # For simplicity: Always treating first row as header is often safer in Markdown than no header.
            if i == 0:
                sep = "| " + " | ".join(['---'] * max_cols) + " |"
                self.output.append(sep + "\n")

    def handle_data(self, data):
        self._add_text(data, raw=False)


# --- Helper Functions from build_guides.py ---

def url_to_cache_path(url):
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

def url_to_out_path(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "docs"
    if path.endswith("/"):
        path = path[:-1]
    return Path(f"{path}.md")

def load_url_groups(path: Path):
    groups = []
    current_name = "Other"
    current_urls = []

    if not path.exists():
        return []

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

def extract_main_html(text):
    lower = text.lower()
    # Try finding the specific content area div for ProcessWire docs
    # Often <div id="content" ...> or <div class="uk-width-expand">
    # Fallback to main/article
    
    start = lower.find('id="content"')
    if start != -1:
        # scan for closing div seems hard without parsing. 
        # Let's use simple tag boundaries if possible.
        pass
        
    start = lower.find("<main")
    end = lower.find("</main>", start) if start != -1 else -1
    if start != -1 and end != -1:
        return text[start:end+7]
        
    start = lower.find("<article")
    end = lower.find("</article>", start) if start != -1 else -1
    if start != -1 and end != -1:
        return text[start:end+10]
        
    start = lower.find("<body")
    end = lower.find("</body>", start) if start != -1 else -1
    if start != -1 and end != -1:
        return text[start:end+7]
        
    return text

def convert_guides(cache_root, urls_path, out_dir):
    cache_root = Path(cache_root)
    urls_path = Path(urls_path)
    out_dir = Path(out_dir)
    
    groups = load_url_groups(urls_path)
    
    for category, urls in groups:
        for url in urls:
            print(f"Converting {url}...")
            cache_rel = url_to_cache_path(url)
            html_path = cache_root / cache_rel
            
            if not html_path.exists():
                print(f"  Missing cache: {html_path}")
                continue
                
            try:
                html_text = html_path.read_text(encoding="utf-8", errors="replace")
                
                # Extract content
                main_html = extract_main_html(html_text)
                
                # Parse
                title = "Unknown"
                # Simple title extraction
                m = re.search(r'<title>(.*?)</title>', html_text, re.I)
                if m: title = html.unescape(m.group(1)).split('|')[0].strip()
                
                converter = MarkdownConverter()
                converter.feed(main_html)
                md_content = converter.get_markdown()
                
                # Output
                rel_out = url_to_out_path(url)
                final_out = out_dir / rel_out
                final_out.parent.mkdir(parents=True, exist_ok=True)
                
                with open(final_out, 'w', encoding='utf-8') as f:
                    f.write(f"# {title}\n\n")
                    f.write(f"Source: {url}\n\n")
                    f.write(md_content)
                    f.write("\n")
                    
            except Exception as e:
                print(f"  Error converting {url}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="cache/docs-html")
    parser.add_argument("--urls", default="cache/urls.txt")
    parser.add_argument("--out", default="docs/guides")
    args = parser.parse_args()
    
    convert_guides(args.cache, args.urls, args.out)

if __name__ == '__main__':
    main()
