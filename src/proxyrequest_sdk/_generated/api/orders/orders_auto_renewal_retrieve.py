from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auto_renewal_status import AutoRenewalStatus
from ...models.orders_auto_renewal_retrieve_response_400 import OrdersAutoRenewalRetrieveResponse400
from ...models.orders_auto_renewal_retrieve_response_401 import OrdersAutoRenewalRetrieveResponse401
from ...models.orders_auto_renewal_retrieve_response_403 import OrdersAutoRenewalRetrieveResponse403
from ...models.orders_auto_renewal_retrieve_response_404 import OrdersAutoRenewalRetrieveResponse404
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
        "method": "get",
        "url": "/orders/{id}/auto-renewal".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AutoRenewalStatus
    | OrdersAutoRenewalRetrieveResponse400
    | OrdersAutoRenewalRetrieveResponse401
    | OrdersAutoRenewalRetrieveResponse403
    | OrdersAutoRenewalRetrieveResponse404
    | None
):
    if response.status_code == 200:
        response_200 = AutoRenewalStatus.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersAutoRenewalRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersAutoRenewalRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersAutoRenewalRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersAutoRenewalRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AutoRenewalStatus
    | OrdersAutoRenewalRetrieveResponse400
    | OrdersAutoRenewalRetrieveResponse401
    | OrdersAutoRenewalRetrieveResponse403
    | OrdersAutoRenewalRetrieveResponse404
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
    AutoRenewalStatus
    | OrdersAutoRenewalRetrieveResponse400
    | OrdersAutoRenewalRetrieveResponse401
    | OrdersAutoRenewalRetrieveResponse403
    | OrdersAutoRenewalRetrieveResponse404
]:
    """Read static calendar renewal settings

     Return wallet-backed renewal settings and the latest attempt for an owned static rental.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoRenewalStatus | OrdersAutoRenewalRetrieveResponse400 | OrdersAutoRenewalRetrieveResponse401 | OrdersAutoRenewalRetrieveResponse403 | OrdersAutoRenewalRetrieveResponse404]
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
    AutoRenewalStatus
    | OrdersAutoRenewalRetrieveResponse400
    | OrdersAutoRenewalRetrieveResponse401
    | OrdersAutoRenewalRetrieveResponse403
    | OrdersAutoRenewalRetrieveResponse404
    | None
):
    """Read static calendar renewal settings

     Return wallet-backed renewal settings and the latest attempt for an owned static rental.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoRenewalStatus | OrdersAutoRenewalRetrieveResponse400 | OrdersAutoRenewalRetrieveResponse401 | OrdersAutoRenewalRetrieveResponse403 | OrdersAutoRenewalRetrieveResponse404
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
    AutoRenewalStatus
    | OrdersAutoRenewalRetrieveResponse400
    | OrdersAutoRenewalRetrieveResponse401
    | OrdersAutoRenewalRetrieveResponse403
    | OrdersAutoRenewalRetrieveResponse404
]:
    """Read static calendar renewal settings

     Return wallet-backed renewal settings and the latest attempt for an owned static rental.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoRenewalStatus | OrdersAutoRenewalRetrieveResponse400 | OrdersAutoRenewalRetrieveResponse401 | OrdersAutoRenewalRetrieveResponse403 | OrdersAutoRenewalRetrieveResponse404]
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
    AutoRenewalStatus
    | OrdersAutoRenewalRetrieveResponse400
    | OrdersAutoRenewalRetrieveResponse401
    | OrdersAutoRenewalRetrieveResponse403
    | OrdersAutoRenewalRetrieveResponse404
    | None
):
    """Read static calendar renewal settings

     Return wallet-backed renewal settings and the latest attempt for an owned static rental.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoRenewalStatus | OrdersAutoRenewalRetrieveResponse400 | OrdersAutoRenewalRetrieveResponse401 | OrdersAutoRenewalRetrieveResponse403 | OrdersAutoRenewalRetrieveResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
