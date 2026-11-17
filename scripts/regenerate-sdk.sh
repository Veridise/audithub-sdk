#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/regenerate-sdk.sh VERSION

Regenerates the AuditHub Python SDK from the live OpenAPI document using
VERSION as the packageVersion, then syncs repository-maintained version
references. Set OPENAPI_SPEC to a local schema snapshot to regenerate offline.
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
OPENAPI_SPEC="${OPENAPI_SPEC:-https://audithub.dev.veridise.tools/api/v1/openapi.json}"

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

# Generate into a clean directory: the generator skips existing test stubs and
# does not remove models/docs for schemas that have been removed upstream.
OUTPUT_DIR="$(mktemp -d)"
trap 'rm -rf "$OUTPUT_DIR"' EXIT
cp .openapi-generator-ignore "$OUTPUT_DIR/"

# Local snapshots lose the origin used to resolve relative OpenAPI servers.
# Preserve the live schema's default host, including for offline regeneration.
if [[ -f "$OPENAPI_SPEC" ]]; then
  "$PYTHON" - "$OPENAPI_SPEC" "$OUTPUT_DIR/openapi.json" "${OPENAPI_BASE_URL:-https://audithub.dev.veridise.tools/api/v1/openapi.json}" <<'SCHEMA'
import json
import sys
from urllib.parse import urljoin

with open(sys.argv[1], encoding="utf-8") as source:
    schema = json.load(source)

def resolve_servers(node):
    if isinstance(node, dict):
        for server in node.get("servers", []):
            if isinstance(server, dict) and isinstance(server.get("url"), str):
                server["url"] = urljoin(sys.argv[3], server["url"])
        for value in node.values():
            resolve_servers(value)
    elif isinstance(node, list):
        for value in node:
            resolve_servers(value)

resolve_servers(schema)
with open(sys.argv[2], "w", encoding="utf-8") as output:
    json.dump(schema, output)
SCHEMA
  OPENAPI_SPEC="$OUTPUT_DIR/openapi.json"
fi

openapi-generator generate \
  -i "$OPENAPI_SPEC" \
  -g python \
  -o "$OUTPUT_DIR" \
  --additional-properties="packageName=audithub_sdk,projectName=audithub-sdk,packageVersion=${VERSION},hideGenerationTimestamp=true,library=httpx"

# Replace only generator-owned trees. Keep handwritten extensions and tests.
for directory in audithub_sdk docs test .openapi-generator; do
  rm -rf "$directory"
  cp -R "$OUTPUT_DIR/$directory" "$directory"
done

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

