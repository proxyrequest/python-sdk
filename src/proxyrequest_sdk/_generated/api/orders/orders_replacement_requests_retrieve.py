from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_replacement_requests_retrieve_response_400 import (
    OrdersReplacementRequestsRetrieveResponse400,
)
from ...models.orders_replacement_requests_retrieve_response_401 import (
    OrdersReplacementRequestsRetrieveResponse401,
)
from ...models.orders_replacement_requests_retrieve_response_403 import (
    OrdersReplacementRequestsRetrieveResponse403,
)
from ...models.orders_replacement_requests_retrieve_response_404 import (
    OrdersReplacementRequestsRetrieveResponse404,
)
from ...models.replacement_page import ReplacementPage
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
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
        "url": "/orders/{id}/replacement-requests".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OrdersReplacementRequestsRetrieveResponse400
    | OrdersReplacementRequestsRetrieveResponse401
    | OrdersReplacementRequestsRetrieveResponse403
    | OrdersReplacementRequestsRetrieveResponse404
    | ReplacementPage
    | None
):
    if response.status_code == 200:
        response_200 = ReplacementPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersReplacementRequestsRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersReplacementRequestsRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersReplacementRequestsRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersReplacementRequestsRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrdersReplacementRequestsRetrieveResponse400
    | OrdersReplacementRequestsRetrieveResponse401
    | OrdersReplacementRequestsRetrieveResponse403
    | OrdersReplacementRequestsRetrieveResponse404
    | ReplacementPage
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersReplacementRequestsRetrieveResponse400
    | OrdersReplacementRequestsRetrieveResponse401
    | OrdersReplacementRequestsRetrieveResponse403
    | OrdersReplacementRequestsRetrieveResponse404
    | ReplacementPage
]:
    """List order replacement requests

     Read replacement requests for an owned static rental order, including per-IP status. Results are
    paginated.

    Args:
        id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersReplacementRequestsRetrieveResponse400 | OrdersReplacementRequestsRetrieveResponse401 | OrdersReplacementRequestsRetrieveResponse403 | OrdersReplacementRequestsRetrieveResponse404 | ReplacementPage]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersReplacementRequestsRetrieveResponse400
    | OrdersReplacementRequestsRetrieveResponse401
    | OrdersReplacementRequestsRetrieveResponse403
    | OrdersReplacementRequestsRetrieveResponse404
    | ReplacementPage
    | None
):
    """List order replacement requests

     Read replacement requests for an owned static rental order, including per-IP status. Results are
    paginated.

    Args:
        id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersReplacementRequestsRetrieveResponse400 | OrdersReplacementRequestsRetrieveResponse401 | OrdersReplacementRequestsRetrieveResponse403 | OrdersReplacementRequestsRetrieveResponse404 | ReplacementPage
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersReplacementRequestsRetrieveResponse400
    | OrdersReplacementRequestsRetrieveResponse401
    | OrdersReplacementRequestsRetrieveResponse403
    | OrdersReplacementRequestsRetrieveResponse404
    | ReplacementPage
]:
    """List order replacement requests

     Read replacement requests for an owned static rental order, including per-IP status. Results are
    paginated.

    Args:
        id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersReplacementRequestsRetrieveResponse400 | OrdersReplacementRequestsRetrieveResponse401 | OrdersReplacementRequestsRetrieveResponse403 | OrdersReplacementRequestsRetrieveResponse404 | ReplacementPage]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersReplacementRequestsRetrieveResponse400
    | OrdersReplacementRequestsRetrieveResponse401
    | OrdersReplacementRequestsRetrieveResponse403
    | OrdersReplacementRequestsRetrieveResponse404
    | ReplacementPage
    | None
):
    """List order replacement requests

     Read replacement requests for an owned static rental order, including per-IP status. Results are
    paginated.

    Args:
        id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersReplacementRequestsRetrieveResponse400 | OrdersReplacementRequestsRetrieveResponse401 | OrdersReplacementRequestsRetrieveResponse403 | OrdersReplacementRequestsRetrieveResponse404 | ReplacementPage
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            offset=offset,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
