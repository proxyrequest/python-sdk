from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice import Invoice
from ...models.invoice_create_request import InvoiceCreateRequest
from ...models.invoices_create_response_400 import InvoicesCreateResponse400
from ...models.invoices_create_response_401 import InvoicesCreateResponse401
from ...models.invoices_create_response_403 import InvoicesCreateResponse403
from ...models.invoices_create_response_409 import InvoicesCreateResponse409
from ...models.invoices_create_response_502 import InvoicesCreateResponse502
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: InvoiceCreateRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/invoices",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Invoice
    | InvoicesCreateResponse400
    | InvoicesCreateResponse401
    | InvoicesCreateResponse403
    | InvoicesCreateResponse409
    | InvoicesCreateResponse502
    | None
):
    if response.status_code == 201:
        response_201 = Invoice.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = InvoicesCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InvoicesCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = InvoicesCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = InvoicesCreateResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 502:
        response_502 = InvoicesCreateResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Invoice
    | InvoicesCreateResponse400
    | InvoicesCreateResponse401
    | InvoicesCreateResponse403
    | InvoicesCreateResponse409
    | InvoicesCreateResponse502
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
    body: InvoiceCreateRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Invoice
    | InvoicesCreateResponse400
    | InvoicesCreateResponse401
    | InvoicesCreateResponse403
    | InvoicesCreateResponse409
    | InvoicesCreateResponse502
]:
    """Create an invoice

     Calculates package pricing, creates a pending invoice, and initializes the selected payment provider
    when required.

    Args:
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (InvoiceCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invoice | InvoicesCreateResponse400 | InvoicesCreateResponse401 | InvoicesCreateResponse403 | InvoicesCreateResponse409 | InvoicesCreateResponse502]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InvoiceCreateRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Invoice
    | InvoicesCreateResponse400
    | InvoicesCreateResponse401
    | InvoicesCreateResponse403
    | InvoicesCreateResponse409
    | InvoicesCreateResponse502
    | None
):
    """Create an invoice

     Calculates package pricing, creates a pending invoice, and initializes the selected payment provider
    when required.

    Args:
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (InvoiceCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invoice | InvoicesCreateResponse400 | InvoicesCreateResponse401 | InvoicesCreateResponse403 | InvoicesCreateResponse409 | InvoicesCreateResponse502
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InvoiceCreateRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Invoice
    | InvoicesCreateResponse400
    | InvoicesCreateResponse401
    | InvoicesCreateResponse403
    | InvoicesCreateResponse409
    | InvoicesCreateResponse502
]:
    """Create an invoice

     Calculates package pricing, creates a pending invoice, and initializes the selected payment provider
    when required.

    Args:
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (InvoiceCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invoice | InvoicesCreateResponse400 | InvoicesCreateResponse401 | InvoicesCreateResponse403 | InvoicesCreateResponse409 | InvoicesCreateResponse502]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InvoiceCreateRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Invoice
    | InvoicesCreateResponse400
    | InvoicesCreateResponse401
    | InvoicesCreateResponse403
    | InvoicesCreateResponse409
    | InvoicesCreateResponse502
    | None
):
    """Create an invoice

     Calculates package pricing, creates a pending invoice, and initializes the selected payment provider
    when required.

    Args:
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (InvoiceCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invoice | InvoicesCreateResponse400 | InvoicesCreateResponse401 | InvoicesCreateResponse403 | InvoicesCreateResponse409 | InvoicesCreateResponse502
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            accept_language=accept_language,
        )
    ).parsed
