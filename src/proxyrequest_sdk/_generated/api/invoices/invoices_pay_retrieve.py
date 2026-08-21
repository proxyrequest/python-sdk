from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoices_pay_retrieve_response_400 import InvoicesPayRetrieveResponse400
from ...models.invoices_pay_retrieve_response_401 import InvoicesPayRetrieveResponse401
from ...models.invoices_pay_retrieve_response_403 import InvoicesPayRetrieveResponse403
from ...models.invoices_pay_retrieve_response_404 import InvoicesPayRetrieveResponse404
from ...models.payment_link_response import PaymentLinkResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/invoices/{id}/pay".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InvoicesPayRetrieveResponse400
    | InvoicesPayRetrieveResponse401
    | InvoicesPayRetrieveResponse403
    | InvoicesPayRetrieveResponse404
    | PaymentLinkResponse
    | None
):
    if response.status_code == 200:
        response_200 = PaymentLinkResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvoicesPayRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InvoicesPayRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = InvoicesPayRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InvoicesPayRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InvoicesPayRetrieveResponse400
    | InvoicesPayRetrieveResponse401
    | InvoicesPayRetrieveResponse403
    | InvoicesPayRetrieveResponse404
    | PaymentLinkResponse
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
    accept_language: str | Unset = UNSET,
) -> Response[
    InvoicesPayRetrieveResponse400
    | InvoicesPayRetrieveResponse401
    | InvoicesPayRetrieveResponse403
    | InvoicesPayRetrieveResponse404
    | PaymentLinkResponse
]:
    """Get an invoice payment link

     Returns the hosted checkout URL for a pending invoice. Paid, cancelled, or expired invoices cannot
    produce a new payment link.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicesPayRetrieveResponse400 | InvoicesPayRetrieveResponse401 | InvoicesPayRetrieveResponse403 | InvoicesPayRetrieveResponse404 | PaymentLinkResponse]
    """

    kwargs = _get_kwargs(
        id=id,
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
    accept_language: str | Unset = UNSET,
) -> (
    InvoicesPayRetrieveResponse400
    | InvoicesPayRetrieveResponse401
    | InvoicesPayRetrieveResponse403
    | InvoicesPayRetrieveResponse404
    | PaymentLinkResponse
    | None
):
    """Get an invoice payment link

     Returns the hosted checkout URL for a pending invoice. Paid, cancelled, or expired invoices cannot
    produce a new payment link.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicesPayRetrieveResponse400 | InvoicesPayRetrieveResponse401 | InvoicesPayRetrieveResponse403 | InvoicesPayRetrieveResponse404 | PaymentLinkResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> Response[
    InvoicesPayRetrieveResponse400
    | InvoicesPayRetrieveResponse401
    | InvoicesPayRetrieveResponse403
    | InvoicesPayRetrieveResponse404
    | PaymentLinkResponse
]:
    """Get an invoice payment link

     Returns the hosted checkout URL for a pending invoice. Paid, cancelled, or expired invoices cannot
    produce a new payment link.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicesPayRetrieveResponse400 | InvoicesPayRetrieveResponse401 | InvoicesPayRetrieveResponse403 | InvoicesPayRetrieveResponse404 | PaymentLinkResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    InvoicesPayRetrieveResponse400
    | InvoicesPayRetrieveResponse401
    | InvoicesPayRetrieveResponse403
    | InvoicesPayRetrieveResponse404
    | PaymentLinkResponse
    | None
):
    """Get an invoice payment link

     Returns the hosted checkout URL for a pending invoice. Paid, cancelled, or expired invoices cannot
    produce a new payment link.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicesPayRetrieveResponse400 | InvoicesPayRetrieveResponse401 | InvoicesPayRetrieveResponse403 | InvoicesPayRetrieveResponse404 | PaymentLinkResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            accept_language=accept_language,
        )
    ).parsed
