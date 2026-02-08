#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="${ROOT_DIR}/source/processwire"
REMOTE_URL="git@github.com:processwire/processwire.git"
BRANCH="${PW_SOURCE_BRANCH:-dev}"

if [ ! -d "${SOURCE_DIR}" ]; then
  mkdir -p "${ROOT_DIR}/source"
  git clone --branch "${BRANCH}" "${REMOTE_URL}" "${SOURCE_DIR}"
else
  if ! git -C "${SOURCE_DIR}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    backup_dir="${SOURCE_DIR}.backup"
    if [ -e "${backup_dir}" ]; then
      i=1
      while [ -e "${backup_dir}.${i}" ]; do
        i=$((i+1))
      done
      backup_dir="${backup_dir}.${i}"
    fi
    mv "${SOURCE_DIR}" "${backup_dir}"
    git clone --branch "${BRANCH}" "${REMOTE_URL}" "${SOURCE_DIR}"
  else
    git -C "${SOURCE_DIR}" fetch origin
    git -C "${SOURCE_DIR}" checkout "${BRANCH}"
    git -C "${SOURCE_DIR}" pull --ff-only origin "${BRANCH}"
  fi
fi

COMMIT_SHA="$(git -C "${SOURCE_DIR}" rev-parse HEAD)"
{
  echo "branch=${BRANCH}"
  echo "commit=${COMMIT_SHA}"
} > "${ROOT_DIR}/source/processwire.lock"

echo "ProcessWire source synced: ${BRANCH} @ ${COMMIT_SHA}"
