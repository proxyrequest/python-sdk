from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice import Invoice
from ...models.orders_renew_create_response_400 import OrdersRenewCreateResponse400
from ...models.orders_renew_create_response_401 import OrdersRenewCreateResponse401
from ...models.orders_renew_create_response_403 import OrdersRenewCreateResponse403
from ...models.orders_renew_create_response_404 import OrdersRenewCreateResponse404
from ...models.orders_renew_create_response_502 import OrdersRenewCreateResponse502
from ...models.renewal_request_request import RenewalRequestRequest
from ...models.static_mutation_error import StaticMutationError
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: RenewalRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/orders/{id}/renew".format(
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
    Invoice
    | OrdersRenewCreateResponse400
    | OrdersRenewCreateResponse401
    | OrdersRenewCreateResponse403
    | OrdersRenewCreateResponse404
    | OrdersRenewCreateResponse502
    | StaticMutationError
    | None
):
    if response.status_code == 200:
        response_200 = Invoice.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Invoice.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = OrdersRenewCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersRenewCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersRenewCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersRenewCreateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = StaticMutationError.from_dict(response.json())

        return response_409

    if response.status_code == 502:
        response_502 = OrdersRenewCreateResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Invoice
    | OrdersRenewCreateResponse400
    | OrdersRenewCreateResponse401
    | OrdersRenewCreateResponse403
    | OrdersRenewCreateResponse404
    | OrdersRenewCreateResponse502
    | StaticMutationError
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
    body: RenewalRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    Invoice
    | OrdersRenewCreateResponse400
    | OrdersRenewCreateResponse401
    | OrdersRenewCreateResponse403
    | OrdersRenewCreateResponse404
    | OrdersRenewCreateResponse502
    | StaticMutationError
]:
    """Renew an order

     Create an invoice on this order for selected IPs or all eligible IPs. The idempotency key prevents
    repeated charges.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (RenewalRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invoice | OrdersRenewCreateResponse400 | OrdersRenewCreateResponse401 | OrdersRenewCreateResponse403 | OrdersRenewCreateResponse404 | OrdersRenewCreateResponse502 | StaticMutationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
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
    body: RenewalRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    Invoice
    | OrdersRenewCreateResponse400
    | OrdersRenewCreateResponse401
    | OrdersRenewCreateResponse403
    | OrdersRenewCreateResponse404
    | OrdersRenewCreateResponse502
    | StaticMutationError
    | None
):
    """Renew an order

     Create an invoice on this order for selected IPs or all eligible IPs. The idempotency key prevents
    repeated charges.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (RenewalRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invoice | OrdersRenewCreateResponse400 | OrdersRenewCreateResponse401 | OrdersRenewCreateResponse403 | OrdersRenewCreateResponse404 | OrdersRenewCreateResponse502 | StaticMutationError
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: RenewalRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    Invoice
    | OrdersRenewCreateResponse400
    | OrdersRenewCreateResponse401
    | OrdersRenewCreateResponse403
    | OrdersRenewCreateResponse404
    | OrdersRenewCreateResponse502
    | StaticMutationError
]:
    """Renew an order

     Create an invoice on this order for selected IPs or all eligible IPs. The idempotency key prevents
    repeated charges.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (RenewalRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invoice | OrdersRenewCreateResponse400 | OrdersRenewCreateResponse401 | OrdersRenewCreateResponse403 | OrdersRenewCreateResponse404 | OrdersRenewCreateResponse502 | StaticMutationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: RenewalRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    Invoice
    | OrdersRenewCreateResponse400
    | OrdersRenewCreateResponse401
    | OrdersRenewCreateResponse403
    | OrdersRenewCreateResponse404
    | OrdersRenewCreateResponse502
    | StaticMutationError
    | None
):
    """Renew an order

     Create an invoice on this order for selected IPs or all eligible IPs. The idempotency key prevents
    repeated charges.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (RenewalRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invoice | OrdersRenewCreateResponse400 | OrdersRenewCreateResponse401 | OrdersRenewCreateResponse403 | OrdersRenewCreateResponse404 | OrdersRenewCreateResponse502 | StaticMutationError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
