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
