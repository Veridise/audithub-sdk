# audithub-sdk

`audithub-sdk` is the generated Python SDK for the AuditHub API at `https://audithub.dev.veridise.tools/api/v1`.
This repository is intended to be the core dependency used by other Python repos that need a typed client for interacting with AuditHub.

## Generation

The client code in this repository is generated from the live OpenAPI document:

`https://audithub.dev.veridise.tools/api/v1/openapi.json`

The repository contents are produced with OpenAPI Generator 7.20.0. The current generated package version is `0.1.0`.

The current generation command is:

```sh
openapi-generator generate \
  -i https://audithub.dev.veridise.tools/api/v1/openapi.json \
  -g python \
  -o . \
  --additional-properties=packageName=audithub_sdk,projectName=audithub-sdk,packageVersion=0.1.0,hideGenerationTimestamp=true,library=httpx
```

## Regenerating

When the AuditHub API schema changes, regenerate the SDK from the repository root and pass the new SDK version:

```sh
scripts/regenerate-sdk.sh 0.1.1
```

The script passes that version as `packageVersion` to OpenAPI Generator, then syncs repository-maintained version references in:

- `pyproject.toml`
- `setup.py`
- `README.md`
- `AGENTS.md`

The version in this README's generator command is intentionally updated only when regenerating the SDK.

Manual changes in this repo should stay limited to repository-specific files such as:

- `README.md`
- packaging metadata
- CI workflows
- `scripts/regenerate-sdk.sh`

Generated source, models, docs, and tests should be replaced by regeneration rather than edited by hand.

## Version Bumping

`bump-my-version` is configured in `pyproject.toml` for release-only version bumps. For API schema changes, use `scripts/regenerate-sdk.sh VERSION` instead. The bump command updates package metadata and runtime package-version strings, commits the change, and creates a `vX.Y.Z` tag:

```sh
uv tool install bump-my-version
```

```sh
bump-my-version bump patch
```

To set an exact version:

```sh
bump-my-version bump --new-version 0.1.1
```

The bump configuration intentionally does not update this README's generator command. That command is updated by `scripts/regenerate-sdk.sh` when the SDK is regenerated.

## Installation

From PyPI:

```sh
pip install audithub-sdk
```

From the repository:

```sh
pip install .
```

## Usage

```python
import audithub_sdk

configuration = audithub_sdk.Configuration(
    host="https://audithub.dev.veridise.tools/api/v1"
)

async with audithub_sdk.ApiClient(configuration) as api_client:
    api = audithub_sdk.AdminApi(api_client)
    print(await api.about_admin_about_get())
```

For OIDC client-credentials authentication, use the handwritten extension package:

```python
import audithub_sdk
from audithub_sdk_ext import AuthenticatedApiClient, OIDCClientCredentialsContext

configuration = audithub_sdk.Configuration(
    host="https://audithub.dev.veridise.tools/api/v1"
)
auth_context = OIDCClientCredentialsContext(
    oidc_configuration_url="https://issuer.example/.well-known/openid-configuration",
    client_id="your-client-id",
    client_secret="your-client-secret",
)

async with AuthenticatedApiClient(configuration, auth_context=auth_context) as api_client:
    api = audithub_sdk.AdminApi(api_client)
    print(await api.about_admin_about_get())
```

## Testing

Install dependencies and run the generated test suite:

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r test-requirements.txt
pytest --cov=audithub_sdk
```

## Publishing

The repository includes `pyproject.toml` and `setup.py` so the package can be built and published to PyPI with standard Python packaging tools.

To build distributions locally:

```sh
python -m build
```

Publishing is handled by `.github/workflows/publish.yml` from a GitHub release tag. The workflow does not edit version files; it fails unless the tag version matches:

- `pyproject.toml`
- `setup.py`
- `audithub_sdk/__init__.py`

Use `vX.Y.Z` tags for releases, for example:

```sh
git tag v0.1.1
git push origin v0.1.1
```
