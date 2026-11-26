from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_proxy_password_reset_create_response_400 import (
    OrdersProxyPasswordResetCreateResponse400,
)
from ...models.orders_proxy_password_reset_create_response_401 import (
    OrdersProxyPasswordResetCreateResponse401,
)
from ...models.orders_proxy_password_reset_create_response_403 import (
    OrdersProxyPasswordResetCreateResponse403,
)
from ...models.orders_proxy_password_reset_create_response_404 import (
    OrdersProxyPasswordResetCreateResponse404,
)
from ...models.proxy_password_reset_response import ProxyPasswordResetResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/orders/{id}/proxy-password/reset".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OrdersProxyPasswordResetCreateResponse400
    | OrdersProxyPasswordResetCreateResponse401
    | OrdersProxyPasswordResetCreateResponse403
    | OrdersProxyPasswordResetCreateResponse404
    | ProxyPasswordResetResponse
    | None
):
    if response.status_code == 200:
        response_200 = ProxyPasswordResetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersProxyPasswordResetCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersProxyPasswordResetCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersProxyPasswordResetCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersProxyPasswordResetCreateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrdersProxyPasswordResetCreateResponse400
    | OrdersProxyPasswordResetCreateResponse401
    | OrdersProxyPasswordResetCreateResponse403
    | OrdersProxyPasswordResetCreateResponse404
    | ProxyPasswordResetResponse
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
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersProxyPasswordResetCreateResponse400
    | OrdersProxyPasswordResetCreateResponse401
    | OrdersProxyPasswordResetCreateResponse403
    | OrdersProxyPasswordResetCreateResponse404
    | ProxyPasswordResetResponse
]:
    """Rotate the password for a static rental order

     Rotate the password for an owned static rental order. Read the rental again to obtain the new
    credentials.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersProxyPasswordResetCreateResponse400 | OrdersProxyPasswordResetCreateResponse401 | OrdersProxyPasswordResetCreateResponse403 | OrdersProxyPasswordResetCreateResponse404 | ProxyPasswordResetResponse]
    """

    kwargs = _get_kwargs(
        id=id,
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
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersProxyPasswordResetCreateResponse400
    | OrdersProxyPasswordResetCreateResponse401
    | OrdersProxyPasswordResetCreateResponse403
    | OrdersProxyPasswordResetCreateResponse404
    | ProxyPasswordResetResponse
    | None
):
    """Rotate the password for a static rental order

     Rotate the password for an owned static rental order. Read the rental again to obtain the new
    credentials.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersProxyPasswordResetCreateResponse400 | OrdersProxyPasswordResetCreateResponse401 | OrdersProxyPasswordResetCreateResponse403 | OrdersProxyPasswordResetCreateResponse404 | ProxyPasswordResetResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersProxyPasswordResetCreateResponse400
    | OrdersProxyPasswordResetCreateResponse401
    | OrdersProxyPasswordResetCreateResponse403
    | OrdersProxyPasswordResetCreateResponse404
    | ProxyPasswordResetResponse
]:
    """Rotate the password for a static rental order

     Rotate the password for an owned static rental order. Read the rental again to obtain the new
    credentials.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersProxyPasswordResetCreateResponse400 | OrdersProxyPasswordResetCreateResponse401 | OrdersProxyPasswordResetCreateResponse403 | OrdersProxyPasswordResetCreateResponse404 | ProxyPasswordResetResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersProxyPasswordResetCreateResponse400
    | OrdersProxyPasswordResetCreateResponse401
    | OrdersProxyPasswordResetCreateResponse403
    | OrdersProxyPasswordResetCreateResponse404
    | ProxyPasswordResetResponse
    | None
):
    """Rotate the password for a static rental order

     Rotate the password for an owned static rental order. Read the rental again to obtain the new
    credentials.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersProxyPasswordResetCreateResponse400 | OrdersProxyPasswordResetCreateResponse401 | OrdersProxyPasswordResetCreateResponse403 | OrdersProxyPasswordResetCreateResponse404 | ProxyPasswordResetResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
