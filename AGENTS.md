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

Preferred regeneration command:

```sh
scripts/regenerate-sdk.sh 0.1.0
```

The script runs the equivalent of:

```sh
openapi-generator generate \
  -i https://audithub.dev.veridise.tools/api/v1/openapi.json \
  -g python \
  -o . \
  --additional-properties=packageName=audithub_sdk,projectName=audithub-sdk,packageVersion=0.1.0,hideGenerationTimestamp=true,library=httpx
```

## Important Decisions From Prior Sessions

- The repo should remain mostly generated output. Manual edits should stay limited to repository-specific files and metadata.
- `bump-my-version` is configured for release version bumps, but `README.md`'s generator command should only be updated during SDK regeneration.

## Files That May Be Manually Maintained

- `README.md`
- `AGENTS.md`
- `pyproject.toml`
- `setup.py`
- `.openapi-generator-ignore`
- `scripts/regenerate-sdk.sh`
- `audithub_sdk_ext/`
- `tests/`
- `.github/workflows/python.yml`
- `.github/workflows/publish.yml`

Generated source under `audithub_sdk/`, generated docs under `docs/`, generated tests under `test/`, and generator metadata under `.openapi-generator/` should generally be replaced by regeneration rather than hand-edited. The narrow exception is package-version strings updated by `bump-my-version` in `audithub_sdk/__init__.py`, `audithub_sdk/api_client.py`, and `audithub_sdk/configuration.py`.

## Version Bumping

`bump-my-version` configuration lives in `pyproject.toml`.

Common commands:

```sh
bump-my-version bump patch
bump-my-version bump --new-version 0.1.1
```

The configured bump is for release-only version bumps. For API schema changes, use `scripts/regenerate-sdk.sh VERSION` instead. The configured bump creates a commit and `v{new_version}` tag. It updates `pyproject.toml`, `setup.py`, and runtime package-version strings in generated source. It intentionally does not update `README.md` or `AGENTS.md`; those generation-contract versions are updated by `scripts/regenerate-sdk.sh`.

## CI And Publishing

- Test workflow: `.github/workflows/python.yml`
- Publish workflow: `.github/workflows/publish.yml`
- Publish workflow is read-only with respect to package version files and fails unless the release tag matches `pyproject.toml`, `setup.py`, and `audithub_sdk/__init__.py`.
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
