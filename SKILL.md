---
name: processwire-api-lookup
version: 0.2.0
description: A specialized tool for finding ProcessWire API documentation, core classes, methods, and hooks. Use this to explain how to use ProcessWire features.
usage_tips: Prefer docs/api-core first to reduce context size. Read only the specific files needed.
---

# ProcessWire API Lookup Logic

Use this skill to answer technical questions about ProcessWire classes, methods, hooks, selectors, and core functionality. The documentation is pre-extracted in `docs/`. Do not modify the extracted docs when answering.

## Triggers
Use this skill when the user asks about ProcessWire Core API, classes, methods, hooks, selectors, or core functionality (for example: how to find pages, save pages, use hooks, or build selectors).

## Entry Point
- `docs/api-core/index.md` (core-only, recommended)
- `docs/api-full/index.md` (full)
- `docs/documentation/index.md` (official guides + cheatsheets)
- `docs/_tasks.json` (task → relevant classes/methods)

The index is organized into API Variables, Core Classes, and Functions. Categories are configured in `categories.json` (official API structure). If an entry is not listed there, heuristic grouping is used and it falls back to `Additional`/`Other`.

## Search Workflow
1. Identify intent. Is it a specific class or a conceptual question?
2. Consult index. Start with `docs/api-core/index.md`.
3. Task matching. If the user asks “How do I…”, check `docs/_tasks.json` first.
4. Drill down. Open the specific class or method file only after locating it.
5. Guides. If the question is conceptual, consult `docs/documentation/` after core API.

## Retrieval Tips
- Prefer `docs/api-core` for smaller context; fall back to `docs/api-full` only if needed.
- Start from `index.md`, then drill down via group files (`group-*.md`) before opening method files.
- Use `_search.json` for compact lookups before opening full files.

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

## Maintenance (For Developers Only)
Only run these when explicitly asked to update documentation.
- `python3 src/update_docs.py` to rebuild `docs/api-core`, `docs/api-full`, `docs/documentation`, `docs/blog-posts`, and `docs/_tasks.json`.
- `python3 src/cache_docs.py` to refresh the local HTML cache for guides.
- `python3 src/build_guides.py` to rebuild `docs/documentation/` and `docs/blog-posts/` from cached HTML.
