"""Stable authentication helpers layered on top of the generated SDK."""

from __future__ import annotations

import asyncio
import ssl
from dataclasses import dataclass
from typing import Callable, Optional, Union

import httpx

import audithub_sdk
from audithub_sdk import rest

VerifyTypes = Union[bool, str, ssl.SSLContext]
AsyncClientFactory = Callable[..., httpx.AsyncClient]


@dataclass(frozen=True)
class OIDCClientCredentialsContext:
    """Configuration for OIDC client-credentials authentication."""

    oidc_configuration_url: str
    client_id: str
    client_secret: str
    scope: Optional[str] = "openid profile"
    auth_timeout: Union[float, httpx.Timeout] = 10.0
    verify_ssl: Optional[VerifyTypes] = None


class OIDCTokenProvider:
    """Fetches and caches OIDC access tokens."""

    def __init__(
        self,
        context: OIDCClientCredentialsContext,
        *,
        _client_factory: Optional[AsyncClientFactory] = None,
    ) -> None:
        self.context = context
        self._client_factory = _client_factory or httpx.AsyncClient
        self._access_token: Optional[str] = None
        self._token_endpoint: Optional[str] = None
        self._lock = asyncio.Lock()

    async def get_token(self) -> str:
        """Return a cached access token, fetching one if needed."""
        async with self._lock:
            if self._access_token is not None:
                return self._access_token

            token_endpoint = await self._get_token_endpoint_locked()
            token_request_data = {
                "client_id": self.context.client_id,
                "client_secret": self.context.client_secret,
                "grant_type": "client_credentials",
            }
            if self.context.scope is not None:
                token_request_data["scope"] = self.context.scope

            async with self._create_http_client() as client:
                response = await client.post(token_endpoint, data=token_request_data)
                response.raise_for_status()

            token_data = response.json()
            access_token = token_data.get("access_token")
            if not isinstance(access_token, str) or not access_token:
                raise RuntimeError("OIDC token response did not include an access_token")

            self._access_token = access_token
            return access_token

    async def invalidate(self) -> None:
        """Drop the cached access token."""
        async with self._lock:
            self._access_token = None

    async def _get_token_endpoint_locked(self) -> str:
        if self._token_endpoint is not None:
            return self._token_endpoint

        async with self._create_http_client() as client:
            response = await client.get(self.context.oidc_configuration_url)
            response.raise_for_status()

        configuration_data = response.json()
        token_endpoint = configuration_data.get("token_endpoint")
        if not isinstance(token_endpoint, str) or not token_endpoint:
            raise RuntimeError("OIDC discovery response did not include a token_endpoint")

        self._token_endpoint = token_endpoint
        return token_endpoint

    def _create_http_client(self) -> httpx.AsyncClient:
        client_kwargs = {"timeout": self.context.auth_timeout}
        if self.context.verify_ssl is not None:
            client_kwargs["verify"] = self.context.verify_ssl
        return self._client_factory(**client_kwargs)


class _AuthenticatedRESTClientObject(rest.RESTClientObject):
    """Generated REST client with token injection and a single 401 retry."""

    def __init__(
        self,
        configuration: audithub_sdk.Configuration,
        token_provider: OIDCTokenProvider,
        *,
        _client_factory: Optional[AsyncClientFactory] = None,
    ) -> None:
        super().__init__(configuration)
        self._token_provider = token_provider
        self._client_factory = _client_factory

    async def request(
        self,
        method,
        url,
        headers=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ):
        request_headers = dict(headers or {})
        used_provider_token = "Authorization" not in request_headers

        if used_provider_token:
            request_headers["Authorization"] = f"Bearer {await self._token_provider.get_token()}"

        response = await super().request(
            method,
            url,
            headers=request_headers,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
        )

        if response.status != 401 or not used_provider_token:
            return response

        await self._token_provider.invalidate()
        request_headers["Authorization"] = f"Bearer {await self._token_provider.get_token()}"
        return await super().request(
            method,
            url,
            headers=request_headers,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
        )

    def _create_pool_manager(self) -> httpx.AsyncClient:
        if self._client_factory is not None:
            client_kwargs = {
                "trust_env": True,
                "verify": self.ssl_context,
            }
            if self.proxy:
                client_kwargs["proxy"] = httpx.Proxy(
                    url=self.proxy,
                    headers=self.proxy_headers,
                )
            return self._client_factory(**client_kwargs)
        return super()._create_pool_manager()


class AuthenticatedApiClient(audithub_sdk.ApiClient):
    """Generated ApiClient wired with a stable handwritten OIDC auth layer."""

    def __init__(
        self,
        configuration: Optional[audithub_sdk.Configuration] = None,
        *,
        token_provider: Optional[OIDCTokenProvider] = None,
        auth_context: Optional[OIDCClientCredentialsContext] = None,
        header_name=None,
        header_value=None,
        cookie=None,
        _oidc_client_factory: Optional[AsyncClientFactory] = None,
        _rest_client_factory: Optional[AsyncClientFactory] = None,
    ) -> None:
        if token_provider is None:
            if auth_context is None:
                raise ValueError("AuthenticatedApiClient requires token_provider or auth_context")
            token_provider = OIDCTokenProvider(
                auth_context,
                _client_factory=_oidc_client_factory,
            )

        super().__init__(
            configuration=configuration,
            header_name=header_name,
            header_value=header_value,
            cookie=cookie,
        )
        self.token_provider = token_provider
        self.rest_client = _AuthenticatedRESTClientObject(
            self.configuration,
            token_provider,
            _client_factory=_rest_client_factory,
        )
