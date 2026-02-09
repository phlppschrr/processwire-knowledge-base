#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/release.sh --master [--date YYYY-MM-DD] [--no-fetch] [--commit SHA]
  scripts/release.sh --dev    [--date YYYY-MM-DD] [--no-fetch] [--commit SHA]

Options:
  --master       Build from ProcessWire master branch
  --dev          Build from ProcessWire dev branch
  --date         Override release date used by the workflow
  --no-fetch     Do not refresh ProcessWire source (skip --fetch)
  --commit       Checkout specific ProcessWire commit before building docs
EOF
}

branch=""
date_override=""
fetch_flag="--fetch"
commit_sha=""
commit_flag=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --master)
      branch="master"
      ;;
    --dev)
      branch="dev"
      ;;
    --date)
      shift
      date_override="${1:-}"
      ;;
    --no-fetch)
      fetch_flag=""
      ;;
    --commit)
      shift
      commit_sha="${1:-}"
      commit_flag=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
  shift
 done

if [[ -z "$branch" ]]; then
  echo "Error: choose --master or --dev" >&2
  usage
  exit 1
fi

if [[ "$commit_flag" -eq 1 && -z "$commit_sha" ]]; then
  echo "Error: --commit requires a SHA" >&2
  usage
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "Error: gh not found. Install GitHub CLI first." >&2
  exit 1
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Error: working tree not clean. Commit or stash changes first." >&2
  exit 1
fi

if [[ -n "$commit_sha" ]]; then
  sync_args=(--branch "$branch")
  if [[ -z "$fetch_flag" ]]; then
    sync_args+=(--no-update)
  fi
  python3 src/sync_processwire.py "${sync_args[@]}"

  if ! git -C sources/processwire diff --quiet || ! git -C sources/processwire diff --cached --quiet; then
    echo "Error: sources/processwire has uncommitted changes." >&2
    exit 1
  fi

  git -C sources/processwire checkout "$commit_sha"
  resolved_commit=$(git -C sources/processwire rev-parse HEAD)
  printf "branch=%s\ncommit=%s\n" "$branch" "$resolved_commit" > sources/processwire.lock

  python3 src/update_docs.py --branch "$branch"
else
  python3 src/update_docs.py --branch "$branch" $fetch_flag
fi

version=$(python3 - <<'PY'
import json
from pathlib import Path
meta = Path('docs/_processwire_version.json')
if not meta.exists():
    raise SystemExit('docs/_processwire_version.json not found')
print(json.loads(meta.read_text(encoding='utf-8')).get('version') or 'unknown')
PY
)

git add -A
if git diff --cached --quiet; then
  echo "No changes to commit."
else
  git commit -m "Update docs for ProcessWire $branch $version"
  git push
fi

if [[ -n "$date_override" ]]; then
  gh workflow run Release -R phlppschrr/processwire-knowledge-base -f date="$date_override"
else
  gh workflow run Release -R phlppschrr/processwire-knowledge-base
fi

echo "Release workflow triggered for $branch ($version)."
