"""Handwritten extensions for the generated AuditHub SDK."""

from audithub_sdk_ext.auth import AuthenticatedApiClient
from audithub_sdk_ext.auth import OIDCClientCredentialsContext
from audithub_sdk_ext.auth import OIDCTokenProvider

__all__ = [
    "AuthenticatedApiClient",
    "OIDCClientCredentialsContext",
    "OIDCTokenProvider",
]
