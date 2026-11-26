from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_purchase_quote_request_request import InvoicePurchaseQuoteRequestRequest
from ...models.invoices_quote_create_response_400 import InvoicesQuoteCreateResponse400
from ...models.invoices_quote_create_response_401 import InvoicesQuoteCreateResponse401
from ...models.invoices_quote_create_response_403 import InvoicesQuoteCreateResponse403
from ...models.purchase_quote_response import PurchaseQuoteResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: InvoicePurchaseQuoteRequestRequest,
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
        "url": "/invoices/quote",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InvoicesQuoteCreateResponse400
    | InvoicesQuoteCreateResponse401
    | InvoicesQuoteCreateResponse403
    | PurchaseQuoteResponse
    | None
):
    if response.status_code == 200:
        response_200 = PurchaseQuoteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvoicesQuoteCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InvoicesQuoteCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = InvoicesQuoteCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InvoicesQuoteCreateResponse400
    | InvoicesQuoteCreateResponse401
    | InvoicesQuoteCreateResponse403
    | PurchaseQuoteResponse
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
    body: InvoicePurchaseQuoteRequestRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    InvoicesQuoteCreateResponse400
    | InvoicesQuoteCreateResponse401
    | InvoicesQuoteCreateResponse403
    | PurchaseQuoteResponse
]:
    """Quote a purchase without creating an invoice

     Calculate a purchase without creating an invoice or charging money. For bandwidth access, select
    pricing_plan_id. Same speed extends the remaining term; higher speed credits unused paid periods and
    starts a new term. Downgrades require expired access. An upgrade must use wallet payment and the
    returned quote_token within 60 seconds. If unused credit exceeds the new price, select a longer
    term. Prices and credits are integer minor currency units; each day is 24 hours.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (InvoicePurchaseQuoteRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicesQuoteCreateResponse400 | InvoicesQuoteCreateResponse401 | InvoicesQuoteCreateResponse403 | PurchaseQuoteResponse]
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
    body: InvoicePurchaseQuoteRequestRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    InvoicesQuoteCreateResponse400
    | InvoicesQuoteCreateResponse401
    | InvoicesQuoteCreateResponse403
    | PurchaseQuoteResponse
    | None
):
    """Quote a purchase without creating an invoice

     Calculate a purchase without creating an invoice or charging money. For bandwidth access, select
    pricing_plan_id. Same speed extends the remaining term; higher speed credits unused paid periods and
    starts a new term. Downgrades require expired access. An upgrade must use wallet payment and the
    returned quote_token within 60 seconds. If unused credit exceeds the new price, select a longer
    term. Prices and credits are integer minor currency units; each day is 24 hours.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (InvoicePurchaseQuoteRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicesQuoteCreateResponse400 | InvoicesQuoteCreateResponse401 | InvoicesQuoteCreateResponse403 | PurchaseQuoteResponse
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
    body: InvoicePurchaseQuoteRequestRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    InvoicesQuoteCreateResponse400
    | InvoicesQuoteCreateResponse401
    | InvoicesQuoteCreateResponse403
    | PurchaseQuoteResponse
]:
    """Quote a purchase without creating an invoice

     Calculate a purchase without creating an invoice or charging money. For bandwidth access, select
    pricing_plan_id. Same speed extends the remaining term; higher speed credits unused paid periods and
    starts a new term. Downgrades require expired access. An upgrade must use wallet payment and the
    returned quote_token within 60 seconds. If unused credit exceeds the new price, select a longer
    term. Prices and credits are integer minor currency units; each day is 24 hours.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (InvoicePurchaseQuoteRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicesQuoteCreateResponse400 | InvoicesQuoteCreateResponse401 | InvoicesQuoteCreateResponse403 | PurchaseQuoteResponse]
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
    body: InvoicePurchaseQuoteRequestRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    InvoicesQuoteCreateResponse400
    | InvoicesQuoteCreateResponse401
    | InvoicesQuoteCreateResponse403
    | PurchaseQuoteResponse
    | None
):
    """Quote a purchase without creating an invoice

     Calculate a purchase without creating an invoice or charging money. For bandwidth access, select
    pricing_plan_id. Same speed extends the remaining term; higher speed credits unused paid periods and
    starts a new term. Downgrades require expired access. An upgrade must use wallet payment and the
    returned quote_token within 60 seconds. If unused credit exceeds the new price, select a longer
    term. Prices and credits are integer minor currency units; each day is 24 hours.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (InvoicePurchaseQuoteRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicesQuoteCreateResponse400 | InvoicesQuoteCreateResponse401 | InvoicesQuoteCreateResponse403 | PurchaseQuoteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
