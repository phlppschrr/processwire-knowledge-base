#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/build_api_docs_repo.sh <output_dir>

Builds the standalone api-docs repository payload with this layout:
  api-docs/                      (from docs/api-full)
  _processwire_version.json
  LICENSE
  NOTICE
  README.md
  context7.json
EOF
}

if [[ $# -ne 1 ]]; then
  usage
  exit 1
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out_dir="$1"

mkdir -p "$out_dir"
mkdir -p "$out_dir/api-docs"

if [[ ! -d "$repo_root/docs/api-full" ]]; then
  echo "Error: $repo_root/docs/api-full not found" >&2
  exit 1
fi

if [[ ! -f "$repo_root/docs/_processwire_version.json" ]]; then
  echo "Error: $repo_root/docs/_processwire_version.json not found" >&2
  exit 1
fi

find "$out_dir" -mindepth 1 -maxdepth 1 -exec rm -rf {} +
mkdir -p "$out_dir/api-docs"

cp -R "$repo_root/docs/api-full/." "$out_dir/api-docs/"
cp "$repo_root/docs/_processwire_version.json" "$out_dir/_processwire_version.json"
cp "$repo_root/LICENSE" "$out_dir/LICENSE"
cp "$repo_root/NOTICE.md" "$out_dir/NOTICE"

cat > "$out_dir/README.md" <<'EOF'
# ProcessWire API Docs (Unofficial)

Unofficial, auto-generated ProcessWire API documentation in an LLM-friendly Markdown format.

The docs are generated from ProcessWire source code API docs for the ProcessWire CMS/CMF.

## Layout

- `api-docs/`: Full generated API reference (from `docs/api-full`)
- `_processwire_version.json`: Version and build metadata
- `LICENSE`
- `NOTICE`
EOF

cat > "$out_dir/context7.json" <<'EOF'
{
  "$schema": "https://context7.com/schema/context7.json",
  "projectTitle": "ProcessWire API Docs",
  "description": "Unofficial auto-generated ProcessWire API docs in LLM-friendly Markdown format.",
  "folders": [
    "api-docs"
  ],
  "excludeFiles": [
    "LICENSE",
    "NOTICE",
    "_processwire_version.json"
  ]
}
EOF
