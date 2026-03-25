import asyncio

import httpx
import pytest

import audithub_sdk
from audithub_sdk.exceptions import UnauthorizedException
from audithub_sdk_ext.auth import AuthenticatedApiClient
from audithub_sdk_ext.auth import OIDCClientCredentialsContext
from audithub_sdk_ext.auth import OIDCTokenProvider


def async_test(coro):
    return asyncio.run(coro)


def test_oidc_discovery_and_token_fetch_are_cached():
    calls = {"discovery": 0, "token": 0}
    token_requests = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url == httpx.URL("https://issuer/.well-known/openid-configuration"):
            calls["discovery"] += 1
            return httpx.Response(
                200,
                json={"token_endpoint": "https://issuer/oauth/token"},
            )
        if request.url == httpx.URL("https://issuer/oauth/token"):
            calls["token"] += 1
            token_requests.append(request.content.decode("utf-8"))
            return httpx.Response(200, json={"access_token": "token-1"})
        raise AssertionError(f"Unexpected request: {request.method} {request.url}")

    provider = OIDCTokenProvider(
        OIDCClientCredentialsContext(
            oidc_configuration_url="https://issuer/.well-known/openid-configuration",
            client_id="client-id",
            client_secret="client-secret",
        ),
        _client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(handler),
            **kwargs,
        ),
    )

    first = async_test(provider.get_token())
    second = async_test(provider.get_token())

    assert first == "token-1"
    assert second == "token-1"
    assert calls == {"discovery": 1, "token": 1}
    assert token_requests == [
        "client_id=client-id&client_secret=client-secret&grant_type=client_credentials&scope=openid+profile"
    ]


def test_client_credentials_scope_is_optional():
    token_requests = []

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url == httpx.URL("https://issuer/.well-known/openid-configuration"):
            return httpx.Response(
                200,
                json={"token_endpoint": "https://issuer/oauth/token"},
            )
        if request.url == httpx.URL("https://issuer/oauth/token"):
            token_requests.append(request.content.decode("utf-8"))
            return httpx.Response(200, json={"access_token": "token-1"})
        raise AssertionError(f"Unexpected request: {request.method} {request.url}")

    provider = OIDCTokenProvider(
        OIDCClientCredentialsContext(
            oidc_configuration_url="https://issuer/.well-known/openid-configuration",
            client_id="client-id",
            client_secret="client-secret",
            scope=None,
        ),
        _client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(handler),
            **kwargs,
        ),
    )

    assert async_test(provider.get_token()) == "token-1"
    assert token_requests == [
        "client_id=client-id&client_secret=client-secret&grant_type=client_credentials"
    ]


def test_authenticated_api_client_injects_bearer_token():
    seen_headers = []

    def oidc_handler(request: httpx.Request) -> httpx.Response:
        if request.url == httpx.URL("https://issuer/.well-known/openid-configuration"):
            return httpx.Response(
                200,
                json={"token_endpoint": "https://issuer/oauth/token"},
            )
        if request.url == httpx.URL("https://issuer/oauth/token"):
            return httpx.Response(200, json={"access_token": "token-1"})
        raise AssertionError(f"Unexpected OIDC request: {request.method} {request.url}")

    def api_handler(request: httpx.Request) -> httpx.Response:
        seen_headers.append(request.headers["Authorization"])
        return httpx.Response(200, json={"ok": True})

    api_client = AuthenticatedApiClient(
        audithub_sdk.Configuration(host="https://api.example.test"),
        auth_context=OIDCClientCredentialsContext(
            oidc_configuration_url="https://issuer/.well-known/openid-configuration",
            client_id="client-id",
            client_secret="client-secret",
        ),
        _oidc_client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(oidc_handler),
            **kwargs,
        ),
        _rest_client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(api_handler),
            **kwargs,
        ),
    )

    async def run_test():
        async with api_client:
            admin_api = audithub_sdk.AdminApi(api_client)
            result = await admin_api.about_admin_about_get()
            assert result == {"ok": True}

    async_test(run_test())
    assert seen_headers == ["Bearer token-1"]


def test_explicit_authorization_header_is_preserved():
    def api_handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["Authorization"] == "Bearer explicit-token"
        return httpx.Response(200, json={"ok": True})

    api_client = AuthenticatedApiClient(
        audithub_sdk.Configuration(host="https://api.example.test"),
        token_provider=OIDCTokenProvider(
            OIDCClientCredentialsContext(
                oidc_configuration_url="https://issuer/.well-known/openid-configuration",
                client_id="client-id",
                client_secret="client-secret",
            ),
            _client_factory=lambda **kwargs: pytest.fail("provider should not be used"),
        ),
        _rest_client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(api_handler),
            **kwargs,
        ),
    )

    async def run_test():
        async with api_client:
            admin_api = audithub_sdk.AdminApi(api_client)
            result = await admin_api.about_admin_about_get(
                _headers={"Authorization": "Bearer explicit-token"}
            )
            assert result == {"ok": True}

    async_test(run_test())


def test_401_refreshes_token_and_retries_once():
    token_responses = iter(["token-1", "token-2"])
    api_authorizations = []

    def oidc_handler(request: httpx.Request) -> httpx.Response:
        if request.url == httpx.URL("https://issuer/.well-known/openid-configuration"):
            return httpx.Response(
                200,
                json={"token_endpoint": "https://issuer/oauth/token"},
            )
        if request.url == httpx.URL("https://issuer/oauth/token"):
            return httpx.Response(200, json={"access_token": next(token_responses)})
        raise AssertionError(f"Unexpected OIDC request: {request.method} {request.url}")

    def api_handler(request: httpx.Request) -> httpx.Response:
        api_authorizations.append(request.headers["Authorization"])
        if len(api_authorizations) == 1:
            return httpx.Response(401, json={"detail": "expired"})
        return httpx.Response(200, json={"ok": True})

    api_client = AuthenticatedApiClient(
        audithub_sdk.Configuration(host="https://api.example.test"),
        auth_context=OIDCClientCredentialsContext(
            oidc_configuration_url="https://issuer/.well-known/openid-configuration",
            client_id="client-id",
            client_secret="client-secret",
        ),
        _oidc_client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(oidc_handler),
            **kwargs,
        ),
        _rest_client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(api_handler),
            **kwargs,
        ),
    )

    async def run_test():
        async with api_client:
            admin_api = audithub_sdk.AdminApi(api_client)
            result = await admin_api.about_admin_about_get()
            assert result == {"ok": True}

    async_test(run_test())
    assert api_authorizations == ["Bearer token-1", "Bearer token-2"]


def test_repeated_401_surfaces_sdk_unauthorized_exception():
    def oidc_handler(request: httpx.Request) -> httpx.Response:
        if request.url == httpx.URL("https://issuer/.well-known/openid-configuration"):
            return httpx.Response(
                200,
                json={"token_endpoint": "https://issuer/oauth/token"},
            )
        if request.url == httpx.URL("https://issuer/oauth/token"):
            return httpx.Response(200, json={"access_token": "token-1"})
        raise AssertionError(f"Unexpected OIDC request: {request.method} {request.url}")

    def api_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"detail": "still unauthorized"})

    api_client = AuthenticatedApiClient(
        audithub_sdk.Configuration(host="https://api.example.test"),
        auth_context=OIDCClientCredentialsContext(
            oidc_configuration_url="https://issuer/.well-known/openid-configuration",
            client_id="client-id",
            client_secret="client-secret",
        ),
        _oidc_client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(oidc_handler),
            **kwargs,
        ),
        _rest_client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(api_handler),
            **kwargs,
        ),
    )

    async def run_test():
        async with api_client:
            admin_api = audithub_sdk.AdminApi(api_client)
            with pytest.raises(UnauthorizedException):
                await admin_api.about_admin_about_get()

    async_test(run_test())


def test_concurrent_requests_share_single_token_fetch():
    calls = {"discovery": 0, "token": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url == httpx.URL("https://issuer/.well-known/openid-configuration"):
            calls["discovery"] += 1
            return httpx.Response(
                200,
                json={"token_endpoint": "https://issuer/oauth/token"},
            )
        if request.url == httpx.URL("https://issuer/oauth/token"):
            calls["token"] += 1
            return httpx.Response(200, json={"access_token": "shared-token"})
        raise AssertionError(f"Unexpected request: {request.method} {request.url}")

    provider = OIDCTokenProvider(
        OIDCClientCredentialsContext(
            oidc_configuration_url="https://issuer/.well-known/openid-configuration",
            client_id="client-id",
            client_secret="client-secret",
        ),
        _client_factory=lambda **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(handler),
            **kwargs,
        ),
    )

    async def run_test():
        tokens = await asyncio.gather(provider.get_token(), provider.get_token(), provider.get_token())
        assert tokens == ["shared-token", "shared-token", "shared-token"]

    async_test(run_test())
    assert calls == {"discovery": 1, "token": 1}
