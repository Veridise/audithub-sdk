# AGENTS.md

## Purpose

This repository contains the generated Python SDK for the AuditHub API.
It is intended to be the shared/core dependency for other Python repositories that need to interact with AuditHub.

## Current Generation Contract

- OpenAPI source: `https://audithub.dev.veridise.tools/api/v1/openapi.json`
- Generator: `openapi-generator` 7.20.0
- Generator target: `python`
- Distribution name: `audithub-sdk`
- Import package: `audithub_sdk`
- Package version currently used during generation: `0.1.0`
- Transport template: `httpx`

Generation command:

```sh
openapi-generator generate \
  -i https://audithub.dev.veridise.tools/api/v1/openapi.json \
  -g python \
  -o . \
  --additional-properties=packageName=audithub_sdk,projectName=audithub-sdk,packageVersion=0.1.0,hideGenerationTimestamp=true,library=httpx
```

## Important Decisions From Prior Sessions

- The repo should remain mostly generated output. Manual edits should stay limited to repository-specific files and metadata.

## Files That May Be Manually Maintained

- `README.md`
- `AGENTS.md`
- `pyproject.toml`
- `setup.py`
- `.github/workflows/python.yml`
- `.github/workflows/publish.yml`

Generated source under `audithub_sdk/`, generated docs under `docs/`, generated tests under `test/`, and generator metadata under `.openapi-generator/` should generally be replaced by regeneration rather than hand-edited.

## CI And Publishing

- Test workflow: `.github/workflows/python.yml`
- Publish workflow: `.github/workflows/publish.yml`
- Publish workflow uses GitHub Actions trusted publishing to PyPI via OIDC.
- PyPI publishing expects the GitHub repository to be registered as a trusted publisher for the `audithub-sdk` project.

## Verification Commands

Common verification commands used successfully in prior sessions:

```sh
pytest -q
python -m build
```

Expected current behavior:

- Generated test suite passes.
- Package build succeeds and produces both sdist and wheel.
