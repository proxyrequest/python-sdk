from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order import Order
from ...models.orders_partial_update_response_400 import OrdersPartialUpdateResponse400
from ...models.orders_partial_update_response_401 import OrdersPartialUpdateResponse401
from ...models.orders_partial_update_response_403 import OrdersPartialUpdateResponse403
from ...models.orders_partial_update_response_404 import OrdersPartialUpdateResponse404
from ...models.patched_order_auto_renewal_request import PatchedOrderAutoRenewalRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: PatchedOrderAutoRenewalRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/orders/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Order
    | OrdersPartialUpdateResponse400
    | OrdersPartialUpdateResponse401
    | OrdersPartialUpdateResponse403
    | OrdersPartialUpdateResponse404
    | None
):
    if response.status_code == 200:
        response_200 = Order.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersPartialUpdateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersPartialUpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersPartialUpdateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersPartialUpdateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Order
    | OrdersPartialUpdateResponse400
    | OrdersPartialUpdateResponse401
    | OrdersPartialUpdateResponse403
    | OrdersPartialUpdateResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedOrderAutoRenewalRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | OrdersPartialUpdateResponse400
    | OrdersPartialUpdateResponse401
    | OrdersPartialUpdateResponse403
    | OrdersPartialUpdateResponse404
]:
    """Update order auto-renewal

     Updates only the auto-renewal threshold and top-up amount for an active order owned by the
    authenticated account. Set both values to zero to disable it.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedOrderAutoRenewalRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | OrdersPartialUpdateResponse400 | OrdersPartialUpdateResponse401 | OrdersPartialUpdateResponse403 | OrdersPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedOrderAutoRenewalRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | OrdersPartialUpdateResponse400
    | OrdersPartialUpdateResponse401
    | OrdersPartialUpdateResponse403
    | OrdersPartialUpdateResponse404
    | None
):
    """Update order auto-renewal

     Updates only the auto-renewal threshold and top-up amount for an active order owned by the
    authenticated account. Set both values to zero to disable it.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedOrderAutoRenewalRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | OrdersPartialUpdateResponse400 | OrdersPartialUpdateResponse401 | OrdersPartialUpdateResponse403 | OrdersPartialUpdateResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedOrderAutoRenewalRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | OrdersPartialUpdateResponse400
    | OrdersPartialUpdateResponse401
    | OrdersPartialUpdateResponse403
    | OrdersPartialUpdateResponse404
]:
    """Update order auto-renewal

     Updates only the auto-renewal threshold and top-up amount for an active order owned by the
    authenticated account. Set both values to zero to disable it.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedOrderAutoRenewalRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | OrdersPartialUpdateResponse400 | OrdersPartialUpdateResponse401 | OrdersPartialUpdateResponse403 | OrdersPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedOrderAutoRenewalRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | OrdersPartialUpdateResponse400
    | OrdersPartialUpdateResponse401
    | OrdersPartialUpdateResponse403
    | OrdersPartialUpdateResponse404
    | None
):
    """Update order auto-renewal

     Updates only the auto-renewal threshold and top-up amount for an active order owned by the
    authenticated account. Set both values to zero to disable it.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedOrderAutoRenewalRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | OrdersPartialUpdateResponse400 | OrdersPartialUpdateResponse401 | OrdersPartialUpdateResponse403 | OrdersPartialUpdateResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
