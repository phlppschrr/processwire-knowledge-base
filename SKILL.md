---
name: processwire-knowledge-base
version: 0.2.0
description: A specialized tool for finding ProcessWire API documentation, official guides, and blog posts (including latest updates). Use this to explain how to use ProcessWire features, selectors, hooks, and to locate recent announcements or best practices.
usage_tips: Prefer docs/api-core first to reduce context size. Read only the specific files needed.
---

# ProcessWire API Lookup Logic

Use this skill to answer technical questions about ProcessWire classes, methods, hooks, selectors, core functionality, official guides, and blog posts. The documentation is pre-extracted in `docs/`. Do not modify the extracted docs when answering.

## Triggers
Use this skill when the user asks about ProcessWire Core API, classes, methods, hooks, selectors, official guides, or blog posts (for example: how to find pages, save pages, use hooks, build selectors, or find the latest ProcessWire announcements).

## Entry Point
- `docs/api-core/index.md` (core-only, recommended)
- `docs/api-full/index.md` (full)
- `docs/documentation/index.md` (official guides + cheatsheets)
- `docs/documentation/_search.json` (guide search index)
- `docs/blog-posts/index.md` (blog index, newest first)
- `docs/blog-posts/_search.json` (blog search index with dates)
- `docs/_tasks.json` (task → relevant classes/methods)

The index is organized into API Variables, Core Classes, and Functions. Categories are configured in `categories.json` (official API structure). If an entry is not listed there, heuristic grouping is used and it falls back to `Additional`/`Other`.

## Search Workflow
1. Identify intent. Is it a specific class or a conceptual question?
2. Task matching. If the user asks “How do I…”, check `docs/_tasks.json` first.
3. API lookups. Use `docs/api-core/_search.json` (or `docs/api-core/index.md`) first; fall back to `docs/api-full/_search.json` only if needed.
4. Guides. For conceptual questions, use `docs/documentation/_search.json` and then open the specific guide.
5. Blog/announcements. For “latest”, “new”, or release posts, use `docs/blog-posts/_search.json` and sort by the `date` field (YYYY-MM-DD).
6. Drill down. Open the specific class/method/guide/blog file only after locating it.
7. Fallback. Use `scripts/search_docs.py` only if indexes don’t yield a good target.

## Retrieval Tips
- Prefer `docs/api-core` for smaller context; fall back to `docs/api-full` only if needed.
- Start from `index.md`, then drill down via group files (`group-*.md`) before opening method files.
- Use `_search.json` for compact lookups before opening full files.
- For blog searches, prefer `docs/blog-posts/_search.json` (has `date` for recency) before full-text search.
- If a broad keyword search is needed across `docs/`, use `scripts/search_docs.py` and prioritize hits from `docs/api-core`, then `docs/api-full`, then `docs/documentation`, then `docs/blog-posts`. Exact filename matches should be treated as highest priority.

## Search Script
Use the script when the user asks for broad keyword search across the docs folder or within a specific docs group.

```bash
python3 scripts/search_docs.py "selector" --limit 20
python3 scripts/search_docs.py "selector" --limit 20 --format json
python3 scripts/search_docs.py "selector" --source api-full
python3 scripts/search_docs.py "selector" --source official-docs
python3 scripts/search_docs.py "selector" --source blog-posts
python3 scripts/search_docs.py "selector" --source blog-posts --per-file 3
python3 scripts/search_docs.py "selector" --source blog-posts --show-score
python3 scripts/search_docs.py "selector" --source blog-posts --context 2
```

Behavior:
- Searches only `docs/` (no other folders).
- Prefers ripgrep (`rg`) when available; falls back to pure Python for portability.
- Ranking priority: `docs/api-core` > `docs/api-full` > `docs/documentation` > `docs/blog-posts`.
- Filename matches (query appears in filename) receive the highest priority boost.
- Blog posts are additionally ranked by recency based on the date in the filename (YYYY-MM-DD-...).
- `--source` can restrict search to a docs group: `api-full`, `api-core`, `official-docs` (docs/documentation), `blog-posts`, or `all`.
- `--per-file` limits results per file to reduce noise (default: 1).
- `--show-score` appends the ranking score to each hit.
- `--context N` prints N lines before and after each hit.

## Hookable Methods
Methods implemented with a `___` prefix are hookable. In the docs:
- Filenames keep the `___` prefix (e.g. `method-___if.md`).
- Headings, usage and links use the public name without the prefix (e.g. `$page->if()`).
- Hookable methods include a **Hookable** section with both the public name and the implementation name.
- Class index lists mark hookable methods with `(hookable)`.
In `_manifest.json`, hookable methods include `hookable`, `name_public`, and `name_internal` fields for reliable lookup.

## JSON Helpers
- `docs/_tasks.json`: Map user intent to relevant classes and methods. Search this first for “How do I…” questions.
- `docs/_hookable.json`: Look here when the user wants to customize behavior via hooks.
- `docs/*/_search.json`: Compact lookup for classes, methods, and summaries.
- `docs/*/_manifest.json`: Full metadata and paths for each class/file.
- `docs/blog-posts/_search.json`: Blog search index including `date` for recency sorting.

## Maintenance (For Developers Only)
Only run these when explicitly asked to update documentation.
- `python3 src/update_docs.py` to rebuild `docs/api-core`, `docs/api-full`, `docs/documentation`, `docs/blog-posts`, and `docs/_tasks.json`.
- `python3 src/cache_docs.py` to refresh the local HTML cache for guides.
- `python3 src/build_guides.py` to rebuild `docs/documentation/` and `docs/blog-posts/` from cached HTML.
