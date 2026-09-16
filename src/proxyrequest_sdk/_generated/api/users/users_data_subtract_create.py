from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order import Order
from ...models.subtract_data_request import SubtractDataRequest
from ...models.users_data_subtract_create_response_400 import UsersDataSubtractCreateResponse400
from ...models.users_data_subtract_create_response_401 import UsersDataSubtractCreateResponse401
from ...models.users_data_subtract_create_response_403 import UsersDataSubtractCreateResponse403
from ...models.users_data_subtract_create_response_404 import UsersDataSubtractCreateResponse404
from ...models.users_data_subtract_create_response_409 import UsersDataSubtractCreateResponse409
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: SubtractDataRequest,
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
        "url": "/users/{id}/data/subtract".format(
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
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
    | UsersDataSubtractCreateResponse409
    | None
):
    if response.status_code == 202:
        response_202 = Order.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UsersDataSubtractCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersDataSubtractCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersDataSubtractCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsersDataSubtractCreateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UsersDataSubtractCreateResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
    | UsersDataSubtractCreateResponse409
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
    body: SubtractDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
    | UsersDataSubtractCreateResponse409
]:
    """Subtract data from a sub-user order

     Subtracts data from the assigned quota of a managed virtual child order in integer bytes for
    package_id. Both fields are required. This is not a refund or a transfer back into the parent's
    ledger, and does not erase data_spent. The amount cannot exceed the total assigned data; reducing
    the quota below usage can stop the child's access. An independently purchased order is not managed
    through this allocation endpoint. Use Idempotency-Key for safe retries.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (SubtractDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | UsersDataSubtractCreateResponse400 | UsersDataSubtractCreateResponse401 | UsersDataSubtractCreateResponse403 | UsersDataSubtractCreateResponse404 | UsersDataSubtractCreateResponse409]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: SubtractDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
    | UsersDataSubtractCreateResponse409
    | None
):
    """Subtract data from a sub-user order

     Subtracts data from the assigned quota of a managed virtual child order in integer bytes for
    package_id. Both fields are required. This is not a refund or a transfer back into the parent's
    ledger, and does not erase data_spent. The amount cannot exceed the total assigned data; reducing
    the quota below usage can stop the child's access. An independently purchased order is not managed
    through this allocation endpoint. Use Idempotency-Key for safe retries.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (SubtractDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | UsersDataSubtractCreateResponse400 | UsersDataSubtractCreateResponse401 | UsersDataSubtractCreateResponse403 | UsersDataSubtractCreateResponse404 | UsersDataSubtractCreateResponse409
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: SubtractDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
    | UsersDataSubtractCreateResponse409
]:
    """Subtract data from a sub-user order

     Subtracts data from the assigned quota of a managed virtual child order in integer bytes for
    package_id. Both fields are required. This is not a refund or a transfer back into the parent's
    ledger, and does not erase data_spent. The amount cannot exceed the total assigned data; reducing
    the quota below usage can stop the child's access. An independently purchased order is not managed
    through this allocation endpoint. Use Idempotency-Key for safe retries.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (SubtractDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | UsersDataSubtractCreateResponse400 | UsersDataSubtractCreateResponse401 | UsersDataSubtractCreateResponse403 | UsersDataSubtractCreateResponse404 | UsersDataSubtractCreateResponse409]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: SubtractDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
    | UsersDataSubtractCreateResponse409
    | None
):
    """Subtract data from a sub-user order

     Subtracts data from the assigned quota of a managed virtual child order in integer bytes for
    package_id. Both fields are required. This is not a refund or a transfer back into the parent's
    ledger, and does not erase data_spent. The amount cannot exceed the total assigned data; reducing
    the quota below usage can stop the child's access. An independently purchased order is not managed
    through this allocation endpoint. Use Idempotency-Key for safe retries.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (SubtractDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | UsersDataSubtractCreateResponse400 | UsersDataSubtractCreateResponse401 | UsersDataSubtractCreateResponse403 | UsersDataSubtractCreateResponse404 | UsersDataSubtractCreateResponse409
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            accept_language=accept_language,
        )
    ).parsed
