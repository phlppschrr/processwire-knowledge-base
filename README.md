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

To pick the ProcessWire branch:
```bash
python3 src/update_docs.py --branch dev
python3 src/update_docs.py --branch master
```

## Release Tags
Generate a ProcessWire+date release tag (e.g. `pw-3.0.255-2026-02-09`):
```bash
python3 scripts/make_release_tag.py
```

The docs build writes `docs/_processwire_version.json`, which is used by the release workflow.

## Manual Release (GitHub Actions)
Use the **Actions → Release** workflow and click **Run workflow**. You can optionally provide a date (YYYY-MM-DD). The workflow will tag the release and attach a ZIP with `docs/`, `SKILL.md`, and scripts.

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

## License
This repository is licensed under the Mozilla Public License 2.0 (MPL-2.0). Documentation and blog content extracted from processwire.com remain subject to their original terms.

## Contributing
Improvement suggestions, experience reports, and PRs are welcome.
