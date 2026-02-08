#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"

# Ensure virtual environment exists
if [ ! -d "${VENV_DIR}" ]; then
  echo "Creating virtual environment in ${VENV_DIR}..."
  python3 -m venv "${VENV_DIR}"
fi

# Activate virtual environment for this script
source "${VENV_DIR}/bin/activate"

# Install dependencies locally
echo "Installing dependencies..."
pip install -r "${ROOT_DIR}/requirements.txt"

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
