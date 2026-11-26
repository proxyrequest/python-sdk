from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.static_purchase_page import StaticPurchasePage
from ...models.static_purchases_list_response_400 import StaticPurchasesListResponse400
from ...models.static_purchases_list_response_401 import StaticPurchasesListResponse401
from ...models.static_purchases_list_response_403 import StaticPurchasesListResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/static/purchases",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StaticPurchasePage
    | StaticPurchasesListResponse400
    | StaticPurchasesListResponse401
    | StaticPurchasesListResponse403
    | None
):
    if response.status_code == 200:
        response_200 = StaticPurchasePage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StaticPurchasesListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StaticPurchasesListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StaticPurchasesListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StaticPurchasePage
    | StaticPurchasesListResponse400
    | StaticPurchasesListResponse401
    | StaticPurchasesListResponse403
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticPurchasePage
    | StaticPurchasesListResponse400
    | StaticPurchasesListResponse401
    | StaticPurchasesListResponse403
]:
    """List static rental purchases

     List the current account's reservations and rentals without connection credentials.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticPurchasePage | StaticPurchasesListResponse400 | StaticPurchasesListResponse401 | StaticPurchasesListResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
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
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticPurchasePage
    | StaticPurchasesListResponse400
    | StaticPurchasesListResponse401
    | StaticPurchasesListResponse403
    | None
):
    """List static rental purchases

     List the current account's reservations and rentals without connection credentials.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticPurchasePage | StaticPurchasesListResponse400 | StaticPurchasesListResponse401 | StaticPurchasesListResponse403
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticPurchasePage
    | StaticPurchasesListResponse400
    | StaticPurchasesListResponse401
    | StaticPurchasesListResponse403
]:
    """List static rental purchases

     List the current account's reservations and rentals without connection credentials.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticPurchasePage | StaticPurchasesListResponse400 | StaticPurchasesListResponse401 | StaticPurchasesListResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticPurchasePage
    | StaticPurchasesListResponse400
    | StaticPurchasesListResponse401
    | StaticPurchasesListResponse403
    | None
):
    """List static rental purchases

     List the current account's reservations and rentals without connection credentials.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticPurchasePage | StaticPurchasesListResponse400 | StaticPurchasesListResponse401 | StaticPurchasesListResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
