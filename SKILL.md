---
name: processwire-docs-skill
version: 0.1.0
description: Extracted ProcessWire API documentation from core source PHPDoc.
---

# ProcessWire Docs Skill

Use the extracted documentation in `docs/` as the canonical source of truth. The text is taken verbatim from ProcessWire core PHPDoc, with `#pw-*` directives treated as metadata and `#pw-internal` items excluded.

## Entry Point
- `docs/index.md`

## Update
Run:
- `scripts/update-docs.sh`

This will sync the ProcessWire source (DEV branch) into `source/processwire` and rebuild the docs into `docs/`.
