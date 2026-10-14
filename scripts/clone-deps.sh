#!/usr/bin/env bash
# Clone MySciAgent-owned component sources. Existing working trees are never updated.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CODE_DIR="${CODE_DIR:-$(dirname "${REPO_ROOT}")}"
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.10+ is required. On Windows run: python scripts/repositories.py" >&2
  exit 2
fi
exec python3 "${SCRIPT_DIR}/repositories.py" --directory "${CODE_DIR}" "$@"
