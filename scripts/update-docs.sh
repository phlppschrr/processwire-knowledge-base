#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"${ROOT_DIR}/scripts/sync-processwire.sh"

python3 "${ROOT_DIR}/src/build_docs.py" \
  --source "${ROOT_DIR}/source/processwire" \
  --out "${ROOT_DIR}/docs/core" \
  --profile core

python3 "${ROOT_DIR}/src/build_docs.py" \
  --source "${ROOT_DIR}/source/processwire" \
  --out "${ROOT_DIR}/docs/full" \
  --profile full

if [ -f "${ROOT_DIR}/cache/docs-html/_index.json" ]; then
  python3 "${ROOT_DIR}/src/build_guides.py" \
    --cache "${ROOT_DIR}/cache/docs-html" \
    --urls "${ROOT_DIR}/cache/urls.txt" \
    --out "${ROOT_DIR}/docs/guides"
else
  echo "No cached HTML found in cache/docs-html; skipping guides build."
fi

python3 "${ROOT_DIR}/src/build_tasks.py" \
  --core "${ROOT_DIR}/docs/core" \
  --full "${ROOT_DIR}/docs/full" \
  --tasks "${ROOT_DIR}/tasks.json" \
  --out "${ROOT_DIR}/docs"
