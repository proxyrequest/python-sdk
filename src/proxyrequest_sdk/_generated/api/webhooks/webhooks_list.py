from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_webhook_list import PaginatedWebhookList
from ...models.webhooks_list_response_400 import WebhooksListResponse400
from ...models.webhooks_list_response_401 import WebhooksListResponse401
from ...models.webhooks_list_response_403 import WebhooksListResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhooks",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PaginatedWebhookList
    | WebhooksListResponse400
    | WebhooksListResponse401
    | WebhooksListResponse403
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedWebhookList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = WebhooksListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = WebhooksListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = WebhooksListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PaginatedWebhookList
    | WebhooksListResponse400
    | WebhooksListResponse401
    | WebhooksListResponse403
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedWebhookList
    | WebhooksListResponse400
    | WebhooksListResponse401
    | WebhooksListResponse403
]:
    """List customer webhooks

     Returns webhook destinations configured by the authenticated account, including delivery timeouts
    and retry settings.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWebhookList | WebhooksListResponse400 | WebhooksListResponse401 | WebhooksListResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PaginatedWebhookList
    | WebhooksListResponse400
    | WebhooksListResponse401
    | WebhooksListResponse403
    | None
):
    """List customer webhooks

     Returns webhook destinations configured by the authenticated account, including delivery timeouts
    and retry settings.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWebhookList | WebhooksListResponse400 | WebhooksListResponse401 | WebhooksListResponse403
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedWebhookList
    | WebhooksListResponse400
    | WebhooksListResponse401
    | WebhooksListResponse403
]:
    """List customer webhooks

     Returns webhook destinations configured by the authenticated account, including delivery timeouts
    and retry settings.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWebhookList | WebhooksListResponse400 | WebhooksListResponse401 | WebhooksListResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PaginatedWebhookList
    | WebhooksListResponse400
    | WebhooksListResponse401
    | WebhooksListResponse403
    | None
):
    """List customer webhooks

     Returns webhook destinations configured by the authenticated account, including delivery timeouts
    and retry settings.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWebhookList | WebhooksListResponse400 | WebhooksListResponse401 | WebhooksListResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            accept_language=accept_language,
        )
    ).parsed
