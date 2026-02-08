# ProcessWire Docs Skill

This repository builds an LLM-friendly documentation skill from ProcessWire core PHPDoc. It extracts text verbatim, treats `#pw-*` directives as metadata, and excludes `#pw-internal` and `@internal` items.

## Outputs
- `docs/core/` — Core-only build (recommended for LLMs)
- `docs/full/` — Full build (includes modules)

Each class/file is chunked into:
- `index.md`
- `group-<name>.md`
- `method-<name>.md` / `const-<name>.md`
- `_manifest.json` for retrieval

## Update
```bash
./scripts/update-docs.sh
```

This will:
- Sync ProcessWire source (DEV branch) into `source/processwire`
- Build `docs/core` and `docs/full`

## Optional: Cache Official Docs (HTML)
```bash
python3 scripts/cache-docs.py
```

This will:
- Download the ProcessWire guides from `cache/urls.txt`
- Store HTML under `cache/docs-html/` with an `_index.json` manifest

## Notes
- HTMLPurifier-related docs are skipped.
- Source is not committed (see `.gitignore`).
