from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
from importlib.metadata import PackageNotFoundError, version
from types import TracebackType
from typing import Any, TypeVar
from urllib.parse import parse_qs, urlparse

import httpx

from . import resources
from ._generated.client import AuthenticatedClient as GeneratedClient
from ._generated.types import Response, Unset
from .errors import ApiError, PaginationError
from .files import FileDownload

DEFAULT_BASE_URL = "https://api.proxyrequest.com/api/v1"
T = TypeVar("T")

try:
    _PACKAGE_VERSION = version("proxyrequest-sdk")
except PackageNotFoundError:  # pragma: no cover - only possible in an uninstalled source tree
    _PACKAGE_VERSION = "0.0.0"
USER_AGENT = f"proxyrequest-python-sdk/{_PACKAGE_VERSION}"


def _base_url(value: str) -> str:
    normalized = value.rstrip("/")
    url = httpx.URL(normalized)
    if url.scheme not in {"http", "https"} or not url.host:
        raise ValueError("base_url must be an absolute HTTP or HTTPS URL.")
    return normalized


def _timeout(value: float | httpx.Timeout, connect_timeout: float) -> httpx.Timeout:
    return (
        value if isinstance(value, httpx.Timeout) else httpx.Timeout(value, connect=connect_timeout)
    )


def _headers(language: str, authorization: str | None, user_agent: str) -> dict[str, str]:
    if not language.strip():
        raise ValueError("language must not be empty.")
    headers = {
        "Accept": "application/json",
        "Accept-Language": language,
        "User-Agent": user_agent,
    }
    if authorization is not None:
        headers["Authorization"] = authorization
    return headers


def _authorization(api_key: str | None, bearer_token: str | None) -> str | None:
    if api_key and bearer_token:
        raise ValueError("Configure either api_key or bearer_token, not both.")
    if api_key is not None:
        if not api_key:
            raise ValueError("api_key must not be empty.")
        return f"Static {api_key}"
    if bearer_token is not None:
        if not bearer_token:
            raise ValueError("bearer_token must not be empty.")
        return f"Bearer {bearer_token}"
    return None


def _ensure_base_url(client: httpx.Client | httpx.AsyncClient, base_url: str) -> None:
    configured = str(client.base_url).rstrip("/")
    if configured != base_url:
        raise ValueError(f"The injected httpx client must use base_url={base_url!r}.")


def _apply_headers(client: httpx.Client | httpx.AsyncClient, headers: Mapping[str, str]) -> None:
    client.headers.update(headers)
    if "Authorization" not in headers:
        client.headers.pop("Authorization", None)


def _response_value(response: Response[Any]) -> Any:
    status_code = int(response.status_code)
    if not 200 <= status_code < 300:
        raise ApiError.from_response(status_code, response.content, response.headers)
    if response.parsed is None and response.content and status_code not in {204, 205}:
        raise ApiError.unexpected(
            f"ProxyRequest returned an unreadable HTTP {status_code} response."
        )
    return response.parsed


def _next_offset(page: Any, current_offset: int, count: int, visited: set[str]) -> int | None:
    next_url = getattr(page, "next_", None)
    if next_url is None or isinstance(next_url, Unset) or next_url == "":
        return None
    if not isinstance(next_url, str) or next_url in visited:
        raise PaginationError("The API returned an invalid or repeated pagination URL.")
    visited.add(next_url)
    values = parse_qs(urlparse(next_url).query).get("offset", [])
    if values:
        try:
            return int(values[0])
        except ValueError as error:
            raise PaginationError("The API returned a non-integer pagination offset.") from error
    return current_offset + count


class Client:
    """Synchronous ProxyRequest API client."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        language: str = "en",
        timeout: float | httpx.Timeout = 15.0,
        connect_timeout: float = 5.0,
        verify: bool = True,
        follow_redirects: bool = False,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.base_url = _base_url(base_url)
        authorization = _authorization(api_key, bearer_token)
        default_headers = _headers(language, authorization, USER_AGENT)
        self._owns_http_client = http_client is None
        if http_client is None:
            http_client = httpx.Client(
                base_url=self.base_url,
                headers=default_headers,
                timeout=_timeout(timeout, connect_timeout),
                verify=verify,
                follow_redirects=follow_redirects,
            )
        else:
            _ensure_base_url(http_client, self.base_url)
            _apply_headers(http_client, default_headers)
        self._http_client = http_client
        self._generated = GeneratedClient(base_url=self.base_url, token="")
        self._generated.set_httpx_client(http_client)
        self._closed = False
        self._attach_resources()

    @classmethod
    def with_api_key(cls, api_key: str, **options: Any) -> Client:
        return cls(api_key=api_key, **options)

    @classmethod
    def with_bearer_token(cls, token: str, **options: Any) -> Client:
        return cls(bearer_token=token, **options)

    @classmethod
    def anonymous(cls, **options: Any) -> Client:
        return cls(**options)

    def _attach_resources(self) -> None:
        self.api_keys = resources.APIKeysResource(self)
        self.affiliates = resources.AffiliatesResource(self)
        self.analytics = resources.AnalyticsResource(self)
        self.authorization = resources.AuthorizationResource(self)
        self.coupons = resources.CouponsResource(self)
        self.invoices = resources.InvoicesResource(self)
        self.locations = resources.LocationsResource(self)
        self.news = resources.NewsResource(self)
        self.orders = resources.OrdersResource(self)
        self.packages = resources.PackagesResource(self)
        self.profile = resources.ProfileResource(self)
        self.proxies = resources.ProxiesResource(self)
        self.rewards = resources.RewardsResource(self)
        self.sessions = resources.SessionsResource(self)
        self.settings = resources.SettingsResource(self)
        self.telegram = resources.TelegramDashboardResource(self)
        self.telegram_service = resources.TelegramServiceResource(self)
        self.users = resources.UsersResource(self)
        self.webhooks = resources.WebhooksResource(self)

    def _call(self, endpoint: Callable[..., Response[Any]], **kwargs: Any) -> Any:
        try:
            return _response_value(endpoint(client=self._generated, **kwargs))
        except ApiError:
            raise
        except httpx.HTTPError as error:
            raise ApiError.network(error) from error
        except Exception as error:
            raise ApiError.unexpected(
                "Unable to decode the ProxyRequest API response.", error
            ) from error

    def _download(self, endpoint: Callable[..., Response[Any]], **kwargs: Any) -> FileDownload:
        try:
            response = endpoint(client=self._generated, **kwargs)
            _response_value(response)
            return FileDownload.from_response(response.content, response.headers)
        except ApiError:
            raise
        except httpx.HTTPError as error:
            raise ApiError.network(error) from error

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        headers: Mapping[str, str] | None = None,
        **options: Any,
    ) -> httpx.Response:
        try:
            response = self._http_client.request(
                method.upper(), path, params=params, json=json, headers=headers, **options
            )
        except httpx.HTTPError as error:
            raise ApiError.network(error) from error
        if not response.is_success:
            raise ApiError.from_response(response.status_code, response.content, response.headers)
        return response

    def paginate(
        self,
        page_fetcher: Callable[..., Any],
        *,
        limit: int = 100,
        offset: int = 0,
        max_pages: int = 10_000,
        **filters: Any,
    ) -> Iterator[Any]:
        if limit <= 0 or offset < 0 or max_pages <= 0:
            raise ValueError("limit and max_pages must be positive; offset must not be negative.")
        visited: set[str] = set()
        current_offset = offset
        for _ in range(max_pages):
            page = page_fetcher(limit=limit, offset=current_offset, **filters)
            results = getattr(page, "results", None)
            if not isinstance(results, list):
                raise PaginationError("A page object must expose a list in results.")
            yield from results
            next_offset = _next_offset(page, current_offset, len(results), visited)
            if next_offset is None:
                return
            current_offset = next_offset
        raise PaginationError("Pagination stopped after the configured maximum number of pages.")

    def download_invoice_pdf(self, invoice_id: str) -> FileDownload:
        return self.invoices.download_pdf(invoice_id)

    def close(self) -> None:
        if not self._closed and self._owns_http_client:
            self._http_client.close()
        self._closed = True

    def __enter__(self) -> Client:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


class AsyncClient:
    """Asynchronous ProxyRequest API client."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        language: str = "en",
        timeout: float | httpx.Timeout = 15.0,
        connect_timeout: float = 5.0,
        verify: bool = True,
        follow_redirects: bool = False,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self.base_url = _base_url(base_url)
        authorization = _authorization(api_key, bearer_token)
        default_headers = _headers(language, authorization, USER_AGENT)
        self._owns_http_client = http_client is None
        if http_client is None:
            http_client = httpx.AsyncClient(
                base_url=self.base_url,
                headers=default_headers,
                timeout=_timeout(timeout, connect_timeout),
                verify=verify,
                follow_redirects=follow_redirects,
            )
        else:
            _ensure_base_url(http_client, self.base_url)
            _apply_headers(http_client, default_headers)
        self._http_client = http_client
        self._generated = GeneratedClient(base_url=self.base_url, token="")
        self._generated.set_async_httpx_client(http_client)
        self._closed = False
        self._attach_resources()

    @classmethod
    def with_api_key(cls, api_key: str, **options: Any) -> AsyncClient:
        return cls(api_key=api_key, **options)

    @classmethod
    def with_bearer_token(cls, token: str, **options: Any) -> AsyncClient:
        return cls(bearer_token=token, **options)

    @classmethod
    def anonymous(cls, **options: Any) -> AsyncClient:
        return cls(**options)

    def _attach_resources(self) -> None:
        self.api_keys = resources.AsyncAPIKeysResource(self)
        self.affiliates = resources.AsyncAffiliatesResource(self)
        self.analytics = resources.AsyncAnalyticsResource(self)
        self.authorization = resources.AsyncAuthorizationResource(self)
        self.coupons = resources.AsyncCouponsResource(self)
        self.invoices = resources.AsyncInvoicesResource(self)
        self.locations = resources.AsyncLocationsResource(self)
        self.news = resources.AsyncNewsResource(self)
        self.orders = resources.AsyncOrdersResource(self)
        self.packages = resources.AsyncPackagesResource(self)
        self.profile = resources.AsyncProfileResource(self)
        self.proxies = resources.AsyncProxiesResource(self)
        self.rewards = resources.AsyncRewardsResource(self)
        self.sessions = resources.AsyncSessionsResource(self)
        self.settings = resources.AsyncSettingsResource(self)
        self.telegram = resources.AsyncTelegramDashboardResource(self)
        self.telegram_service = resources.AsyncTelegramServiceResource(self)
        self.users = resources.AsyncUsersResource(self)
        self.webhooks = resources.AsyncWebhooksResource(self)

    async def _call(
        self,
        endpoint: Callable[..., Awaitable[Response[Any]]],
        **kwargs: Any,
    ) -> Any:
        try:
            return _response_value(await endpoint(client=self._generated, **kwargs))
        except ApiError:
            raise
        except httpx.HTTPError as error:
            raise ApiError.network(error) from error
        except Exception as error:
            raise ApiError.unexpected(
                "Unable to decode the ProxyRequest API response.", error
            ) from error

    async def _download(
        self,
        endpoint: Callable[..., Awaitable[Response[Any]]],
        **kwargs: Any,
    ) -> FileDownload:
        try:
            response = await endpoint(client=self._generated, **kwargs)
            _response_value(response)
            return FileDownload.from_response(response.content, response.headers)
        except ApiError:
            raise
        except httpx.HTTPError as error:
            raise ApiError.network(error) from error

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        headers: Mapping[str, str] | None = None,
        **options: Any,
    ) -> httpx.Response:
        try:
            response = await self._http_client.request(
                method.upper(), path, params=params, json=json, headers=headers, **options
            )
        except httpx.HTTPError as error:
            raise ApiError.network(error) from error
        if not response.is_success:
            raise ApiError.from_response(response.status_code, response.content, response.headers)
        return response

    async def paginate(
        self,
        page_fetcher: Callable[..., Awaitable[Any]],
        *,
        limit: int = 100,
        offset: int = 0,
        max_pages: int = 10_000,
        **filters: Any,
    ) -> AsyncIterator[Any]:
        if limit <= 0 or offset < 0 or max_pages <= 0:
            raise ValueError("limit and max_pages must be positive; offset must not be negative.")
        visited: set[str] = set()
        current_offset = offset
        for _ in range(max_pages):
            page = await page_fetcher(limit=limit, offset=current_offset, **filters)
            results = getattr(page, "results", None)
            if not isinstance(results, list):
                raise PaginationError("A page object must expose a list in results.")
            for result in results:
                yield result
            next_offset = _next_offset(page, current_offset, len(results), visited)
            if next_offset is None:
                return
            current_offset = next_offset
        raise PaginationError("Pagination stopped after the configured maximum number of pages.")

    async def download_invoice_pdf(self, invoice_id: str) -> FileDownload:
        return await self.invoices.download_pdf(invoice_id)

    async def close(self) -> None:
        if not self._closed and self._owns_http_client:
            await self._http_client.aclose()
        self._closed = True

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()
