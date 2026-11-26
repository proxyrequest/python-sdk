from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.intent_request import IntentRequest
from ...models.orders_purchase_quote_create_response_400 import OrdersPurchaseQuoteCreateResponse400
from ...models.orders_purchase_quote_create_response_401 import OrdersPurchaseQuoteCreateResponse401
from ...models.orders_purchase_quote_create_response_403 import OrdersPurchaseQuoteCreateResponse403
from ...models.rental_quote import RentalQuote
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: IntentRequest | Unset = UNSET,
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
        "url": "/orders/purchase/quote",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OrdersPurchaseQuoteCreateResponse400
    | OrdersPurchaseQuoteCreateResponse401
    | OrdersPurchaseQuoteCreateResponse403
    | RentalQuote
    | None
):
    if response.status_code == 200:
        response_200 = RentalQuote.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersPurchaseQuoteCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersPurchaseQuoteCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersPurchaseQuoteCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrdersPurchaseQuoteCreateResponse400
    | OrdersPurchaseQuoteCreateResponse401
    | OrdersPurchaseQuoteCreateResponse403
    | RentalQuote
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
    body: IntentRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersPurchaseQuoteCreateResponse400
    | OrdersPurchaseQuoteCreateResponse401
    | OrdersPurchaseQuoteCreateResponse403
    | RentalQuote
]:
    """Quote a static rental selection

     Calculate one all-units quantity tier across all items in one package and term without reserving or
    charging. Overlapping geographic and operator scopes cannot double-count inventory. Supports the
    compatible single-location form. Proxy location is separate from billing country.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (IntentRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersPurchaseQuoteCreateResponse400 | OrdersPurchaseQuoteCreateResponse401 | OrdersPurchaseQuoteCreateResponse403 | RentalQuote]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: IntentRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersPurchaseQuoteCreateResponse400
    | OrdersPurchaseQuoteCreateResponse401
    | OrdersPurchaseQuoteCreateResponse403
    | RentalQuote
    | None
):
    """Quote a static rental selection

     Calculate one all-units quantity tier across all items in one package and term without reserving or
    charging. Overlapping geographic and operator scopes cannot double-count inventory. Supports the
    compatible single-location form. Proxy location is separate from billing country.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (IntentRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersPurchaseQuoteCreateResponse400 | OrdersPurchaseQuoteCreateResponse401 | OrdersPurchaseQuoteCreateResponse403 | RentalQuote
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IntentRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersPurchaseQuoteCreateResponse400
    | OrdersPurchaseQuoteCreateResponse401
    | OrdersPurchaseQuoteCreateResponse403
    | RentalQuote
]:
    """Quote a static rental selection

     Calculate one all-units quantity tier across all items in one package and term without reserving or
    charging. Overlapping geographic and operator scopes cannot double-count inventory. Supports the
    compatible single-location form. Proxy location is separate from billing country.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (IntentRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersPurchaseQuoteCreateResponse400 | OrdersPurchaseQuoteCreateResponse401 | OrdersPurchaseQuoteCreateResponse403 | RentalQuote]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: IntentRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersPurchaseQuoteCreateResponse400
    | OrdersPurchaseQuoteCreateResponse401
    | OrdersPurchaseQuoteCreateResponse403
    | RentalQuote
    | None
):
    """Quote a static rental selection

     Calculate one all-units quantity tier across all items in one package and term without reserving or
    charging. Overlapping geographic and operator scopes cannot double-count inventory. Supports the
    compatible single-location form. Proxy location is separate from billing country.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (IntentRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersPurchaseQuoteCreateResponse400 | OrdersPurchaseQuoteCreateResponse401 | OrdersPurchaseQuoteCreateResponse403 | RentalQuote
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
