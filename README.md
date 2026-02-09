# ProcessWire Docs Skill

This repository builds an LLM-friendly documentation skill from ProcessWire core PHPDoc. It extracts text verbatim, treats `#pw-*` directives as metadata, and excludes `#pw-internal` and `@internal` items.

## Outputs
- `docs/core/` — Core-only build (recommended for LLMs)
- `docs/full/` — Full build (includes modules)
- `docs/guides/` — Extracted official guides (summaries + cheatsheets)
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
- Build `docs/core` and `docs/full` from `sources/processwire`
- Build `docs/guides` from `sources/docs-html`
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
