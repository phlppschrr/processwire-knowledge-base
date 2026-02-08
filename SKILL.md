---
name: processwire-docs-skill
version: 0.1.0
description: Extracted ProcessWire API documentation from core source PHPDoc.
---

# ProcessWire Docs Skill

Use the extracted documentation in `docs/` as the canonical source of truth. The text is taken verbatim from ProcessWire core PHPDoc, with `#pw-*` directives treated as metadata and `#pw-internal`/`@internal` items excluded.

## Entry Point
- `docs/core/index.md` (core-only, recommended)
- `docs/full/index.md` (full)

The index is organized into:
- API Variables (from `ProcessWire` class `@property` list)
- Core Classes
- Functions (file-level docs without classes)

Index categories are configured in `categories.json` (official API structure). If an entry is not listed there, heuristic grouping is used and it falls back to `Additional`/`Other`.

## Retrieval Tips
- Prefer `docs/core` for smaller context; fall back to `docs/full` only if needed.
- Start from `index.md`, then drill down via group files (`group-*.md`) before opening method files.
- Each class/file has a `_manifest.json` entry in `docs/*/_manifest.json` with paths and method metadata.

## Hookable Methods
Methods implemented with a `___` prefix are hookable. In the docs:
- Filenames keep the `___` prefix (e.g. `method-___if.md`).
- Headings, usage and links use the public name without the prefix (e.g. `$page->if()`).
- Hookable methods include a **Hookable** section with both the public name and the implementation name.
- Class index lists mark hookable methods with `(hookable)`.
In `_manifest.json`, hookable methods include `hookable`, `name_public`, and `name_internal` fields for reliable lookup.

## Official Guides (Optional Cache)
If you need conceptual guidance beyond API docs, cache the official guides as HTML:
- `python3 scripts/cache-docs.py`

Cached HTML lives under `cache/docs-html/` with an `_index.json` manifest. Use these sources to summarize key concepts like templates, selectors, hooks, modules, security, and multi-language setup.

## Update
Run:
- `scripts/update-docs.sh`

This will sync the ProcessWire source (DEV branch) into `source/processwire` and rebuild:
- `docs/core/` (core-only)
- `docs/full/` (full)
