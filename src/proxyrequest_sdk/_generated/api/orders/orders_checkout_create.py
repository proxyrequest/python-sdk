from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice import Invoice
from ...models.orders_checkout_create_response_400 import OrdersCheckoutCreateResponse400
from ...models.orders_checkout_create_response_401 import OrdersCheckoutCreateResponse401
from ...models.orders_checkout_create_response_403 import OrdersCheckoutCreateResponse403
from ...models.orders_checkout_create_response_404 import OrdersCheckoutCreateResponse404
from ...models.orders_checkout_create_response_502 import OrdersCheckoutCreateResponse502
from ...models.static_checkout_request import StaticCheckoutRequest
from ...models.static_mutation_error import StaticMutationError
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: StaticCheckoutRequest,
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
        "url": "/orders/{id}/checkout".format(
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
    | OrdersCheckoutCreateResponse400
    | OrdersCheckoutCreateResponse401
    | OrdersCheckoutCreateResponse403
    | OrdersCheckoutCreateResponse404
    | OrdersCheckoutCreateResponse502
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
        response_400 = OrdersCheckoutCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersCheckoutCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersCheckoutCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersCheckoutCreateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = StaticMutationError.from_dict(response.json())

        return response_409

    if response.status_code == 502:
        response_502 = OrdersCheckoutCreateResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Invoice
    | OrdersCheckoutCreateResponse400
    | OrdersCheckoutCreateResponse401
    | OrdersCheckoutCreateResponse403
    | OrdersCheckoutCreateResponse404
    | OrdersCheckoutCreateResponse502
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
    body: StaticCheckoutRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    Invoice
    | OrdersCheckoutCreateResponse400
    | OrdersCheckoutCreateResponse401
    | OrdersCheckoutCreateResponse403
    | OrdersCheckoutCreateResponse404
    | OrdersCheckoutCreateResponse502
    | StaticMutationError
]:
    """Check out a rental reservation

     Create one shared billing invoice for this reservation using the selected gateway, coupon and
    billing details. A repeated request returns the existing invoice.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (StaticCheckoutRequest): Invoice transport validation with an explicitly composed
            application command.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invoice | OrdersCheckoutCreateResponse400 | OrdersCheckoutCreateResponse401 | OrdersCheckoutCreateResponse403 | OrdersCheckoutCreateResponse404 | OrdersCheckoutCreateResponse502 | StaticMutationError]
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
    body: StaticCheckoutRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    Invoice
    | OrdersCheckoutCreateResponse400
    | OrdersCheckoutCreateResponse401
    | OrdersCheckoutCreateResponse403
    | OrdersCheckoutCreateResponse404
    | OrdersCheckoutCreateResponse502
    | StaticMutationError
    | None
):
    """Check out a rental reservation

     Create one shared billing invoice for this reservation using the selected gateway, coupon and
    billing details. A repeated request returns the existing invoice.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (StaticCheckoutRequest): Invoice transport validation with an explicitly composed
            application command.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invoice | OrdersCheckoutCreateResponse400 | OrdersCheckoutCreateResponse401 | OrdersCheckoutCreateResponse403 | OrdersCheckoutCreateResponse404 | OrdersCheckoutCreateResponse502 | StaticMutationError
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
    body: StaticCheckoutRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    Invoice
    | OrdersCheckoutCreateResponse400
    | OrdersCheckoutCreateResponse401
    | OrdersCheckoutCreateResponse403
    | OrdersCheckoutCreateResponse404
    | OrdersCheckoutCreateResponse502
    | StaticMutationError
]:
    """Check out a rental reservation

     Create one shared billing invoice for this reservation using the selected gateway, coupon and
    billing details. A repeated request returns the existing invoice.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (StaticCheckoutRequest): Invoice transport validation with an explicitly composed
            application command.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Invoice | OrdersCheckoutCreateResponse400 | OrdersCheckoutCreateResponse401 | OrdersCheckoutCreateResponse403 | OrdersCheckoutCreateResponse404 | OrdersCheckoutCreateResponse502 | StaticMutationError]
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
    body: StaticCheckoutRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    Invoice
    | OrdersCheckoutCreateResponse400
    | OrdersCheckoutCreateResponse401
    | OrdersCheckoutCreateResponse403
    | OrdersCheckoutCreateResponse404
    | OrdersCheckoutCreateResponse502
    | StaticMutationError
    | None
):
    """Check out a rental reservation

     Create one shared billing invoice for this reservation using the selected gateway, coupon and
    billing details. A repeated request returns the existing invoice.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (StaticCheckoutRequest): Invoice transport validation with an explicitly composed
            application command.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Invoice | OrdersCheckoutCreateResponse400 | OrdersCheckoutCreateResponse401 | OrdersCheckoutCreateResponse403 | OrdersCheckoutCreateResponse404 | OrdersCheckoutCreateResponse502 | StaticMutationError
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
