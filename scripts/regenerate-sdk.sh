#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/regenerate-sdk.sh VERSION

Regenerates the AuditHub Python SDK from the live OpenAPI document using
VERSION as the packageVersion, then syncs repository-maintained version
references.
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 2
fi

VERSION="$1"

if [[ -z "$VERSION" || "$VERSION" == *","* || "$VERSION" =~ [[:space:]] ]]; then
  echo "Version must be non-empty and must not contain commas or whitespace." >&2
  exit 2
fi

if ! command -v openapi-generator >/dev/null 2>&1; then
  echo "openapi-generator is required. Install OpenAPI Generator 7.20.0 before regenerating." >&2
  exit 127
fi

PYTHON="${PYTHON:-python3}"
if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "$PYTHON is required to sync repository metadata." >&2
  exit 127
fi

openapi-generator generate \
  -i https://audithub.dev.veridise.tools/api/v1/openapi.json \
  -g python \
  -o . \
  --additional-properties="packageName=audithub_sdk,projectName=audithub-sdk,packageVersion=${VERSION},hideGenerationTimestamp=true,library=httpx"

"$PYTHON" - "$VERSION" <<'PY'
from __future__ import annotations

from pathlib import Path
import re
import sys


version = sys.argv[1]


def replace_exact(path: str, pattern: str, replacement, expected: int) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, flags=re.MULTILINE)
    if count != expected:
        raise SystemExit(f"{path}: expected {expected} replacement(s), made {count}")
    file_path.write_text(updated, encoding="utf-8")


replace_exact(
    "pyproject.toml",
    r'^(version = ")[^"]+(")$',
    lambda match: f"{match.group(1)}{version}{match.group(2)}",
    1,
)
replace_exact(
    "setup.py",
    r'^(VERSION = ")[^"]+(")$',
    lambda match: f"{match.group(1)}{version}{match.group(2)}",
    1,
)
replace_exact(
    "README.md",
    r"packageVersion=[^,]+",
    f"packageVersion={version}",
    1,
)
replace_exact(
    "AGENTS.md",
    r"(Package version currently used during generation: `)[^`]+(`)",
    lambda match: f"{match.group(1)}{version}{match.group(2)}",
    1,
)
replace_exact(
    "AGENTS.md",
    r"packageVersion=[^,]+",
    f"packageVersion={version}",
    1,
)
PY
