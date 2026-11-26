from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_renew_quote_create_response_400 import OrdersRenewQuoteCreateResponse400
from ...models.orders_renew_quote_create_response_401 import OrdersRenewQuoteCreateResponse401
from ...models.orders_renew_quote_create_response_403 import OrdersRenewQuoteCreateResponse403
from ...models.orders_renew_quote_create_response_404 import OrdersRenewQuoteCreateResponse404
from ...models.renewal_quote import RenewalQuote
from ...models.renewal_selection_request import RenewalSelectionRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: RenewalSelectionRequest,
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
        "url": "/orders/{id}/renew/quote".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OrdersRenewQuoteCreateResponse400
    | OrdersRenewQuoteCreateResponse401
    | OrdersRenewQuoteCreateResponse403
    | OrdersRenewQuoteCreateResponse404
    | RenewalQuote
    | None
):
    if response.status_code == 200:
        response_200 = RenewalQuote.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersRenewQuoteCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersRenewQuoteCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersRenewQuoteCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersRenewQuoteCreateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrdersRenewQuoteCreateResponse400
    | OrdersRenewQuoteCreateResponse401
    | OrdersRenewQuoteCreateResponse403
    | OrdersRenewQuoteCreateResponse404
    | RenewalQuote
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
    body: RenewalSelectionRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersRenewQuoteCreateResponse400
    | OrdersRenewQuoteCreateResponse401
    | OrdersRenewQuoteCreateResponse403
    | OrdersRenewQuoteCreateResponse404
    | RenewalQuote
]:
    """Quote order renewal

     Preview the complete price for a renewal, including billing adjustments, without creating an
    invoice.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (RenewalSelectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersRenewQuoteCreateResponse400 | OrdersRenewQuoteCreateResponse401 | OrdersRenewQuoteCreateResponse403 | OrdersRenewQuoteCreateResponse404 | RenewalQuote]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: RenewalSelectionRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersRenewQuoteCreateResponse400
    | OrdersRenewQuoteCreateResponse401
    | OrdersRenewQuoteCreateResponse403
    | OrdersRenewQuoteCreateResponse404
    | RenewalQuote
    | None
):
    """Quote order renewal

     Preview the complete price for a renewal, including billing adjustments, without creating an
    invoice.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (RenewalSelectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersRenewQuoteCreateResponse400 | OrdersRenewQuoteCreateResponse401 | OrdersRenewQuoteCreateResponse403 | OrdersRenewQuoteCreateResponse404 | RenewalQuote
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: RenewalSelectionRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersRenewQuoteCreateResponse400
    | OrdersRenewQuoteCreateResponse401
    | OrdersRenewQuoteCreateResponse403
    | OrdersRenewQuoteCreateResponse404
    | RenewalQuote
]:
    """Quote order renewal

     Preview the complete price for a renewal, including billing adjustments, without creating an
    invoice.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (RenewalSelectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersRenewQuoteCreateResponse400 | OrdersRenewQuoteCreateResponse401 | OrdersRenewQuoteCreateResponse403 | OrdersRenewQuoteCreateResponse404 | RenewalQuote]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: RenewalSelectionRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersRenewQuoteCreateResponse400
    | OrdersRenewQuoteCreateResponse401
    | OrdersRenewQuoteCreateResponse403
    | OrdersRenewQuoteCreateResponse404
    | RenewalQuote
    | None
):
    """Quote order renewal

     Preview the complete price for a renewal, including billing adjustments, without creating an
    invoice.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (RenewalSelectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersRenewQuoteCreateResponse400 | OrdersRenewQuoteCreateResponse401 | OrdersRenewQuoteCreateResponse403 | OrdersRenewQuoteCreateResponse404 | RenewalQuote
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
