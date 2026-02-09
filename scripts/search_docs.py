#!/usr/bin/env python3
"""Search docs/ for query with priority ordering.

Prefers ripgrep (rg) when available; falls back to pure Python scan.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"

SOURCES = {
    "api-full": "docs/api-full",
    "api-core": "docs/api-core",
    "official-docs": "docs/documentation",
    "blog-posts": "docs/blog-posts",
}

# Higher weight = higher priority.
PRIORITY_WEIGHTS = [
    ("docs/api-core/", 300),
    ("docs/api-full/", 200),
    ("docs/documentation/", 100),
    ("docs/blog-posts/", 50),
]

FILENAME_HIT_BONUS = 500
BLOG_DATE_MAX_BONUS = 120


@dataclass
class Hit:
    path: str
    line: int
    text: str
    score: int


def _score_for_path(path: str, query: str) -> int:
    score = 0
    for prefix, weight in PRIORITY_WEIGHTS:
        if path.startswith(prefix):
            score += weight
            break
    filename = os.path.basename(path).lower()
    if query.lower() in filename:
        score += FILENAME_HIT_BONUS
    if path.startswith("docs/blog-posts/"):
        score += _blog_date_bonus(path)
    return score


def _blog_date_bonus(path: str) -> int:
    # Date is expected in filename: YYYY-MM-DD-*.md
    name = os.path.basename(path)
    match = re.match(r"(\\d{4}-\\d{2}-\\d{2})-", name)
    if not match:
        return 0
    try:
        date = datetime.strptime(match.group(1), "%Y-%m-%d").date()
    except ValueError:
        return 0
    # Newer = higher bonus. Map last 10 years into 0..BLOG_DATE_MAX_BONUS.
    days = (datetime.utcnow().date() - date).days
    if days <= 0:
        return BLOG_DATE_MAX_BONUS
    max_days = 365 * 10
    if days >= max_days:
        return 0
    return int(BLOG_DATE_MAX_BONUS * (1 - (days / max_days)))


def _count_occurrences(text: str, pattern: re.Pattern) -> int:
    return len(pattern.findall(text))


def _rg_search(query: str, root: Path) -> Iterable[Hit]:
    # Use ripgrep for speed when available.
    cmd = [
        "rg",
        "-n",
        "--no-heading",
        "--color=never",
        query,
        str(root),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        raise RuntimeError(proc.stderr.strip() or "rg failed")

    pattern = re.compile(re.escape(query), re.IGNORECASE)
    for raw in proc.stdout.splitlines():
        # Format: path:line:match
        parts = raw.split(":", 2)
        if len(parts) != 3:
            continue
        path, line_s, text = parts
        try:
            line = int(line_s)
        except ValueError:
            continue
        rel = os.path.relpath(path, ROOT)
        score = _score_for_path(rel, query) + _count_occurrences(text, pattern)
        yield Hit(path=rel, line=line, text=text.strip(), score=score)


def _grep_search(query: str, root: Path) -> Iterable[Hit]:
    # Use GNU/BSD grep as a secondary fallback.
    cmd = [
        "grep",
        "-nH",
        "-i",
        query,
        str(root),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        raise RuntimeError(proc.stderr.strip() or "grep failed")

    pattern = re.compile(re.escape(query), re.IGNORECASE)
    for raw in proc.stdout.splitlines():
        parts = raw.split(":", 2)
        if len(parts) != 3:
            continue
        path, line_s, text = parts
        try:
            line = int(line_s)
        except ValueError:
            continue
        rel = os.path.relpath(path, ROOT)
        score = _score_for_path(rel, query) + _count_occurrences(text, pattern)
        yield Hit(path=rel, line=line, text=text.strip(), score=score)


def _python_search(query: str, root: Path) -> Iterable[Hit]:
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    for path in root.rglob("*.md"):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = os.path.relpath(path, ROOT)
        base_score = _score_for_path(rel, query)
        for idx, line in enumerate(content.splitlines(), start=1):
            if not pattern.search(line):
                continue
            score = base_score + _count_occurrences(line, pattern)
            yield Hit(path=rel, line=idx, text=line.strip(), score=score)


def _collect_hits(query: str, roots: List[Path]) -> List[Hit]:
    if not DOCS_DIR.exists():
        raise FileNotFoundError(f"Docs directory not found: {DOCS_DIR}")

    hits: List[Hit] = []
    for root in roots:
        if not root.exists():
            continue
        if shutil.which("rg"):
            hits.extend(list(_rg_search(query, root)))
            continue
        if shutil.which("grep"):
            hits.extend(list(_grep_search(query, root)))
            continue
        hits.extend(list(_python_search(query, root)))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Search ProcessWire docs")
    parser.add_argument("query", help="Search term")
    parser.add_argument(
        "--source",
        choices=["api-full", "api-core", "official-docs", "blog-posts", "all"],
        default="all",
        help="Restrict search to a docs group",
    )
    parser.add_argument(
        "--per-file",
        type=int,
        default=1,
        help="Max results per file (default: 1)",
    )
    parser.add_argument(
        "--show-score",
        action="store_true",
        help="Include score in text output",
    )
    parser.add_argument(
        "--context",
        type=int,
        default=0,
        help="Include N lines of context before/after each hit",
    )
    parser.add_argument("--limit", type=int, default=20, help="Max results")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )
    args = parser.parse_args()

    if args.source == "all":
        roots = [DOCS_DIR / SOURCES[name].split("/", 1)[1] for name in SOURCES]
    else:
        roots = [DOCS_DIR / SOURCES[args.source].split("/", 1)[1]]
    hits = _collect_hits(args.query, roots)
    hits.sort(key=lambda h: (-h.score, h.path, h.line))

    per_file_limit = max(args.per_file, 1)
    limited: List[Hit] = []
    per_file_counts: dict[str, int] = {}
    for h in hits:
        count = per_file_counts.get(h.path, 0)
        if count >= per_file_limit:
            continue
        per_file_counts[h.path] = count + 1
        limited.append(h)
        if len(limited) >= max(args.limit, 0):
            break
    hits = limited

    if args.format == "json":
        print(
            json.dumps(
                [
                    {
                        "path": h.path,
                        "line": h.line,
                        "text": h.text,
                        "score": h.score,
                    }
                    for h in hits
                ],
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    if args.context > 0:
        ctx = max(args.context, 0)
        for h in hits:
            try:
                content = (ROOT / h.path).read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            lines = content.splitlines()
            start = max(h.line - 1 - ctx, 0)
            end = min(h.line + ctx, len(lines))
            header = f"{h.path}:{h.line}"
            if args.show_score:
                header += f" (score {h.score})"
            print(header)
            for i in range(start, end):
                prefix = ">" if i == h.line - 1 else " "
                print(f"{prefix} {i+1}: {lines[i]}")
            print("")
        return 0

    for h in hits:
        line = f"{h.path}:{h.line}: {h.text}"
        if args.show_score:
            line += f" (score {h.score})"
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
