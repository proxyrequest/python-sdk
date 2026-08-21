from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoices_list_payment_gateway import InvoicesListPaymentGateway
from ...models.invoices_list_response_400 import InvoicesListResponse400
from ...models.invoices_list_response_401 import InvoicesListResponse401
from ...models.invoices_list_response_403 import InvoicesListResponse403
from ...models.invoices_list_status import InvoicesListStatus
from ...models.invoices_list_type import InvoicesListType
from ...models.paginated_invoice_list import PaginatedInvoiceList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    gateway: InvoicesListPaymentGateway | Unset = UNSET,
    internal_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: InvoicesListStatus | Unset = UNSET,
    type_: InvoicesListType | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    json_gateway: str | Unset = UNSET
    if not isinstance(gateway, Unset):
        json_gateway = gateway.value

    params["gateway"] = json_gateway

    params["internal_id"] = internal_id

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["package__id"] = package_id

    params["search"] = search

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["user__email"] = user_email

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["user__id"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/invoices",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InvoicesListResponse400
    | InvoicesListResponse401
    | InvoicesListResponse403
    | PaginatedInvoiceList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedInvoiceList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvoicesListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InvoicesListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = InvoicesListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InvoicesListResponse400
    | InvoicesListResponse401
    | InvoicesListResponse403
    | PaginatedInvoiceList
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    gateway: InvoicesListPaymentGateway | Unset = UNSET,
    internal_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: InvoicesListStatus | Unset = UNSET,
    type_: InvoicesListType | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    InvoicesListResponse400
    | InvoicesListResponse401
    | InvoicesListResponse403
    | PaginatedInvoiceList
]:
    """List invoices

     Returns invoices visible to the authenticated account. Resellers and administrators can filter by an
    accessible user.

    Args:
        gateway (InvoicesListPaymentGateway | Unset):
        internal_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (str | Unset):
        search (str | Unset):
        status (InvoicesListStatus | Unset):
        type_ (InvoicesListType | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicesListResponse400 | InvoicesListResponse401 | InvoicesListResponse403 | PaginatedInvoiceList]
    """

    kwargs = _get_kwargs(
        gateway=gateway,
        internal_id=internal_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
        status=status,
        type_=type_,
        user_email=user_email,
        user_id=user_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    gateway: InvoicesListPaymentGateway | Unset = UNSET,
    internal_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: InvoicesListStatus | Unset = UNSET,
    type_: InvoicesListType | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    InvoicesListResponse400
    | InvoicesListResponse401
    | InvoicesListResponse403
    | PaginatedInvoiceList
    | None
):
    """List invoices

     Returns invoices visible to the authenticated account. Resellers and administrators can filter by an
    accessible user.

    Args:
        gateway (InvoicesListPaymentGateway | Unset):
        internal_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (str | Unset):
        search (str | Unset):
        status (InvoicesListStatus | Unset):
        type_ (InvoicesListType | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicesListResponse400 | InvoicesListResponse401 | InvoicesListResponse403 | PaginatedInvoiceList
    """

    return sync_detailed(
        client=client,
        gateway=gateway,
        internal_id=internal_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
        status=status,
        type_=type_,
        user_email=user_email,
        user_id=user_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    gateway: InvoicesListPaymentGateway | Unset = UNSET,
    internal_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: InvoicesListStatus | Unset = UNSET,
    type_: InvoicesListType | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    InvoicesListResponse400
    | InvoicesListResponse401
    | InvoicesListResponse403
    | PaginatedInvoiceList
]:
    """List invoices

     Returns invoices visible to the authenticated account. Resellers and administrators can filter by an
    accessible user.

    Args:
        gateway (InvoicesListPaymentGateway | Unset):
        internal_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (str | Unset):
        search (str | Unset):
        status (InvoicesListStatus | Unset):
        type_ (InvoicesListType | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicesListResponse400 | InvoicesListResponse401 | InvoicesListResponse403 | PaginatedInvoiceList]
    """

    kwargs = _get_kwargs(
        gateway=gateway,
        internal_id=internal_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
        status=status,
        type_=type_,
        user_email=user_email,
        user_id=user_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    gateway: InvoicesListPaymentGateway | Unset = UNSET,
    internal_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: InvoicesListStatus | Unset = UNSET,
    type_: InvoicesListType | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    InvoicesListResponse400
    | InvoicesListResponse401
    | InvoicesListResponse403
    | PaginatedInvoiceList
    | None
):
    """List invoices

     Returns invoices visible to the authenticated account. Resellers and administrators can filter by an
    accessible user.

    Args:
        gateway (InvoicesListPaymentGateway | Unset):
        internal_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (str | Unset):
        search (str | Unset):
        status (InvoicesListStatus | Unset):
        type_ (InvoicesListType | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicesListResponse400 | InvoicesListResponse401 | InvoicesListResponse403 | PaginatedInvoiceList
    """

    return (
        await asyncio_detailed(
            client=client,
            gateway=gateway,
            internal_id=internal_id,
            limit=limit,
            offset=offset,
            ordering=ordering,
            package_id=package_id,
            search=search,
            status=status,
            type_=type_,
            user_email=user_email,
            user_id=user_id,
            accept_language=accept_language,
        )
    ).parsed
