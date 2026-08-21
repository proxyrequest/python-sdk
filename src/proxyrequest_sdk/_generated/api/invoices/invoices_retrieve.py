from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice import Invoice
from ...models.invoices_retrieve_response_400 import InvoicesRetrieveResponse400
from ...models.invoices_retrieve_response_401 import InvoicesRetrieveResponse401
from ...models.invoices_retrieve_response_403 import InvoicesRetrieveResponse403
from ...models.invoices_retrieve_response_404 import InvoicesRetrieveResponse404
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
        "url": "/invoices/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Invoice
    | InvoicesRetrieveResponse400
    | InvoicesRetrieveResponse401
    | InvoicesRetrieveResponse403
    | InvoicesRetrieveResponse404
    | None
):
    if response.status_code == 200:
        response_200 = Invoice.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvoicesRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InvoicesRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = InvoicesRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InvoicesRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Invoice
    | InvoicesRetrieveResponse400
    | InvoicesRetrieveResponse401
    | InvoicesRetrieveResponse403
    | InvoicesRetrieveResponse404
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
    Invoice
    | InvoicesRetrieveResponse400
    | InvoicesRetrieveResponse401
    | InvoicesRetrieveResponse403
    | InvoicesRetrieveResponse404
]:
    """Get an invoice

     Returns billing, package, payment, and status details for one invoice visible to the authenticated
    account.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invoice | InvoicesRetrieveResponse400 | InvoicesRetrieveResponse401 | InvoicesRetrieveResponse403 | InvoicesRetrieveResponse404]
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
    Invoice
    | InvoicesRetrieveResponse400
    | InvoicesRetrieveResponse401
    | InvoicesRetrieveResponse403
    | InvoicesRetrieveResponse404
    | None
):
    """Get an invoice

     Returns billing, package, payment, and status details for one invoice visible to the authenticated
    account.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invoice | InvoicesRetrieveResponse400 | InvoicesRetrieveResponse401 | InvoicesRetrieveResponse403 | InvoicesRetrieveResponse404
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
    Invoice
    | InvoicesRetrieveResponse400
    | InvoicesRetrieveResponse401
    | InvoicesRetrieveResponse403
    | InvoicesRetrieveResponse404
]:
    """Get an invoice

     Returns billing, package, payment, and status details for one invoice visible to the authenticated
    account.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invoice | InvoicesRetrieveResponse400 | InvoicesRetrieveResponse401 | InvoicesRetrieveResponse403 | InvoicesRetrieveResponse404]
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
    Invoice
    | InvoicesRetrieveResponse400
    | InvoicesRetrieveResponse401
    | InvoicesRetrieveResponse403
    | InvoicesRetrieveResponse404
    | None
):
    """Get an invoice

     Returns billing, package, payment, and status details for one invoice visible to the authenticated
    account.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invoice | InvoicesRetrieveResponse400 | InvoicesRetrieveResponse401 | InvoicesRetrieveResponse403 | InvoicesRetrieveResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            accept_language=accept_language,
        )
    ).parsed
