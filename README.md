# ProcessWire Knowledge Base Skill

This repository builds an LLM-friendly knowledge base skill from ProcessWire core PHPDoc and official guides. Content is extracted as Markdown, text is preserved verbatim where possible, `#pw-*` directives are treated as metadata, and `#pw-internal` / `@internal` items are excluded.

## Outputs
- `docs/api-core/` — Core-only build (recommended for LLMs)
- `docs/api-full/` — Full build (includes modules)
- `docs/documentation/` — Extracted official docs as Markdown (summaries + cheatsheets)
- `docs/blog-posts/` — Extracted ProcessWire blog posts as Markdown
- `docs/_hookable.json` — Global hookable index (core + full)
- `docs/_tasks.json` — Tasks map (task → relevant classes/methods)

Each class/file is chunked into:
- `index.md`
- `group-<name>.md`
- `method-<name>.md` / `const-<name>.md`
- `_manifest.json` for retrieval
- `_search.json` for compact lookup
- `_hookable.json` for hookable method lookup

## Setup
To use the guide extraction scripts, install the Python dependencies:
```bash
# Optional: Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Update
```bash
python3 src/update_docs.py
```

This will:
- Build `docs/api-core` and `docs/api-full` from `sources/processwire`
- Build `docs/documentation` and `docs/blog-posts` from `sources/docs-html`
- Build `docs/_tasks.json`

Downloads happen only if sources are missing. Use `python3 src/update_docs.py --fetch` to refresh.

## Optional: Cache Official Docs (HTML)
```bash
python3 src/cache_docs.py
```

This will:
- Download the ProcessWire guides from `sources/urls.txt`
- Store HTML under `sources/docs-html/` with an `_index.json` manifest

Then build the guides (Markdown):
```bash
python3 src/build_guides.py
```

## Notes
- HTMLPurifier-related docs are skipped.
- Sources are not committed (see `.gitignore`).
