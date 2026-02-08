#!/usr/bin/env python3
import argparse
import html
import re
import os
from pathlib import Path
from urllib.parse import urlparse
try:
    from bs4 import BeautifulSoup, Tag
except ImportError:
    # Fallback message if dependencies are missing
    print("Error: beautifulsoup4 is required. Please install it using:")
    print("pip install -r requirements.txt")
    exit(1)

# Selector attributes for main content identification
CONTENT_SELECTORS = [
    {"id": "content"},
    {"class": "uk-width-expand"},
    {"name": "main"},
    {"name": "article"}
]

# Tags or classes to remove
UNWANTED = [
    {"class": "uk-breadcrumb"},
    {"class": "pw-sidebar"},
    {"class": "pw-footer"},
    {"class": "pw-search-form"},
    {"class": "prev-next-links"},
    {"id": "content-secondary"},
    {"id": "content-meta"},
    {"id": "content-side"},
    {"name": "nav"},
    {"name": "header"},
    {"name": "footer"},
    {"name": "script"},
    {"name": "style"},
    {"name": "noscript"},
    {"class": "pw-card-pages"}
]

class BSMarkdownConverter:
    def __init__(self):
        self.output = []

    def convert(self, element, list_depth=0, list_type=None, list_index=1):
        """Recursively converts soup elements to markdown."""
        if isinstance(element, str):
            text = self._clean_text(element)
            if text:
                self._add_text(text)
            return

        tag = element.name
        
        if tag in ['p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'pre', 'blockquote', 'table', 'tr']:
            self._ensure_newline(2 if tag in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'pre', 'blockquote', 'table'] else 1)

        # Headings
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self._add_text('#' * level + ' ', raw=True)
            for child in element.children:
                self.convert(child)
            self._ensure_newline(2)

        # Formatting
        elif tag in ['strong', 'b']:
            self._add_text('**', raw=True)
            for child in element.children:
                self.convert(child)
            self._add_text('**', raw=True)
        elif tag in ['em', 'i']:
            self._add_text('*', raw=True)
            for child in element.children:
                self.convert(child)
            self._add_text('*', raw=True)

        # Lists
        elif tag == 'ul':
            for i, child in enumerate(element.find_all('li', recursive=False)):
                self.convert(child, list_depth + 1, 'ul')
            self._ensure_newline(2)
        elif tag == 'ol':
            for i, child in enumerate(element.find_all('li', recursive=False)):
                self.convert(child, list_depth + 1, 'ol', i + 1)
            self._ensure_newline(2)
        elif tag == 'li':
            indent = '  ' * (list_depth - 1)
            bullet = f"{list_index}. " if list_type == 'ol' else "- "
            self._add_text(f"{indent}{bullet}", raw=True)
            for child in element.children:
                self.convert(child, list_depth)
            self._ensure_newline(1)

        # Code
        elif tag == 'pre':
            # Check for nested code tag
            code_tag = element.find('code')
            content = code_tag.get_text() if code_tag else element.get_text()
            self._add_text("```\n", raw=True)
            self._add_text(content.strip(), raw=True)
            self._add_text("\n```", raw=True)
            self._ensure_newline(2)
        elif tag == 'code':
            self._add_text('`', raw=True)
            self._add_text(element.get_text(), raw=True)
            self._add_text('`', raw=True)

        # Links
        elif tag == 'a':
            href = element.get('href')
            # Skip empty anchors (often used for targets)
            if not href:
                for child in element.children:
                    self.convert(child)
            else:
                self._add_text('[', raw=True)
                for child in element.children:
                    self.convert(child)
                self._add_text(f']({href})', raw=True)

        # Tables
        elif tag == 'table':
            # print(f"DEBUG: Found table with {len(element.find_all('tr'))} rows")
            self._convert_table(element)
            self._ensure_newline(2)

        # Line breaks
        elif tag == 'br':
            self._add_text('\n', raw=True)
        elif tag == 'hr':
            self._ensure_newline(2)
            self._add_text('---\n', raw=True)

        # Blockquote
        elif tag == 'blockquote':
            self._add_text('> ', raw=True)
            for child in element.children:
                self.convert(child)
            self._ensure_newline(2)

        # Definition Lists
        elif tag == 'dl':
            for child in element.children:
                self.convert(child)
            self._ensure_newline(2)
        elif tag == 'dt':
            self._add_text('**', raw=True)
            for child in element.children:
                self.convert(child)
            self._add_text('**\n', raw=True)
        elif tag == 'dd':
            self._add_text(': ', raw=True)
            for child in element.children:
                self.convert(child)
            self._ensure_newline(2)

        # General Fallback for div, section, etc.
        else:
            for child in element.children:
                self.convert(child, list_depth, list_type, list_index)

    def get_markdown(self):
        return "".join(self.output).strip()

    def _convert_table(self, table):
        rows = []
        # Support tbody, thead, tfoot explicitly
        all_rows = table.find_all('tr')
        if not all_rows:
             # Maybe rows are direct children?
             pass 

        for tr in all_rows:
            row_cells = []
            for cell in tr.find_all(['td', 'th']):
                # Convert cell content to markdown
                sub_converter = BSMarkdownConverter()
                # Process children of the cell, not the cell itself (to avoid wrapper)
                for child in cell.children:
                    sub_converter.convert(child)
                cell_md = sub_converter.get_markdown()
                # Escape pipes for table format
                cell_md = cell_md.replace('|', '\\|').replace('\n', ' ')
                row_cells.append(cell_md)
            
            if row_cells:
                rows.append(row_cells)
        
        if not rows: return

        max_cols = max(len(r) for r in rows)
        for i, row in enumerate(rows):
            while len(row) < max_cols: row.append("")
            self.output.append("| " + " | ".join(row) + " |\n")
            # Assume first row is header if widely used convention, or check for TH
            # For simplicity, always add separator after first row
            if i == 0:
                self.output.append("| " + " | ".join(['---'] * max_cols) + " |\n")

    def _clean_text(self, text):
        return re.sub(r'\s+', ' ', text)

    def _add_text(self, text, raw=False):
        if not raw:
            # Avoid leading space if previous ended with newline
            if self.output and self.output[-1].endswith('\n'):
                text = text.lstrip()
        self.output.append(text)

    def _ensure_newline(self, count=1):
        joined = "".join(self.output[-min(len(self.output), 5):])
        existing = 0
        for c in reversed(joined):
            if c == '\n': existing += 1
            elif c.isspace(): continue
            else: break
        needed = count - existing
        if needed > 0:
            self.output.append('\n' * needed)

def normalize_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def url_to_cache_path(url):
    parsed = urlparse(url)
    host = parsed.netloc or "processwire.com"
    path = parsed.path or "/"
    if path.endswith("/"): path = f"{path}index.html"
    elif not path.endswith(".html"): path = f"{path}/index.html"
    if parsed.query:
        safe_query = parsed.query.replace("/", "_").replace("&", "_").replace("=", "-")
        path = f"{path}__{safe_query}"
    return f"{host}{path}"

def url_to_out_path(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/") or "docs"
    if path.endswith("/"): path = path[:-1]
    return Path(f"{path}.md")

def load_url_groups(path: Path):
    groups = []
    current_name, current_urls = "Other", []
    if not path.exists(): return []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line: continue
        if line.startswith("#"):
            label = line.lstrip("#").strip()
            if not label or label.lower().startswith("processwire docs pages"): continue
            if current_urls: groups.append((current_name, current_urls))
            current_name, current_urls = label, []
        else: current_urls.append(line)
    if current_urls: groups.append((current_name, current_urls))
    return groups

def convert_guides(cache, urls, out):
    cache_root, urls_path, out_dir = Path(cache), Path(urls), Path(out)
    groups = load_url_groups(urls_path)
    
    for category, urls in groups:
        for url in urls:
            print(f"Converting {url}...")
            html_path = cache_root / url_to_cache_path(url)
            if not html_path.exists(): continue
                
            try:
                html_text = html_path.read_text(encoding="utf-8", errors="replace")
                soup = BeautifulSoup(html_text, 'html5lib')
                
                # Metadata
                title = soup.title.string.split('|')[0].strip() if soup.title else "Unknown"
                
                # Content Selection
                content = None
                for selector in CONTENT_SELECTORS:
                    if "id" in selector: content = soup.find(id=selector["id"])
                    elif "class" in selector: content = soup.find(class_=selector["class"])
                    elif "name" in selector: content = soup.find(selector["name"])
                    if content: break
                
                if not content: content = soup.body or soup

                # Cleaning
                for crit in UNWANTED:
                    if "class" in crit:
                        for el in content.find_all(class_=crit["class"]): el.decompose()
                    elif "id" in crit:
                        for el in content.find_all(id=crit["id"]): el.decompose()
                    elif "name" in crit:
                        for el in content.find_all(crit["name"]): el.decompose()

                # Conversion
                converter = BSMarkdownConverter()
                converter.convert(content)
                md = converter.get_markdown()
                
                # Output
                final_out = out_dir / url_to_out_path(url)
                final_out.parent.mkdir(parents=True, exist_ok=True)
                with open(final_out, 'w', encoding='utf-8') as f:
                    f.write(f"# {title}\n\nSource: {url}\n\n{md}\n")
            except Exception as e:
                print(f"  Error converting {url}: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", default="cache/docs-html")
    parser.add_argument("--urls", default="cache/urls.txt")
    parser.add_argument("--out", default="docs/guides")
    convert_guides(**vars(parser.parse_args()))
