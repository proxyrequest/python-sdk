from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order import Order
from ...models.reset_data_request import ResetDataRequest
from ...models.users_data_reset_create_response_400 import UsersDataResetCreateResponse400
from ...models.users_data_reset_create_response_401 import UsersDataResetCreateResponse401
from ...models.users_data_reset_create_response_403 import UsersDataResetCreateResponse403
from ...models.users_data_reset_create_response_404 import UsersDataResetCreateResponse404
from ...models.users_data_reset_create_response_409 import UsersDataResetCreateResponse409
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: ResetDataRequest,
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
        "url": "/users/{id}/data/reset".format(
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
    | UsersDataResetCreateResponse400
    | UsersDataResetCreateResponse401
    | UsersDataResetCreateResponse403
    | UsersDataResetCreateResponse404
    | UsersDataResetCreateResponse409
    | None
):
    if response.status_code == 202:
        response_202 = Order.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UsersDataResetCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersDataResetCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersDataResetCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsersDataResetCreateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UsersDataResetCreateResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Order
    | UsersDataResetCreateResponse400
    | UsersDataResetCreateResponse401
    | UsersDataResetCreateResponse403
    | UsersDataResetCreateResponse404
    | UsersDataResetCreateResponse409
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
    body: ResetDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | UsersDataResetCreateResponse400
    | UsersDataResetCreateResponse401
    | UsersDataResetCreateResponse403
    | UsersDataResetCreateResponse404
    | UsersDataResetCreateResponse409
]:
    """Reset a user's remaining data

     Atomically resets remaining data to zero for package_id, including zero or negative balances. Supply
    package_id only; data is not accepted. System administrators may reset any user; other accounts may
    reset only their direct children. Purchased root orders have their ledger balances cleared; virtual
    child orders have their quota set to usage without changing the parent's pool. Usage history and
    invoices are preserved. Unlimited packages are rejected. Use Idempotency-Key for safe retries so a
    repeated request cannot clear a subsequent top-up.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (ResetDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | UsersDataResetCreateResponse400 | UsersDataResetCreateResponse401 | UsersDataResetCreateResponse403 | UsersDataResetCreateResponse404 | UsersDataResetCreateResponse409]
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
    body: ResetDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | UsersDataResetCreateResponse400
    | UsersDataResetCreateResponse401
    | UsersDataResetCreateResponse403
    | UsersDataResetCreateResponse404
    | UsersDataResetCreateResponse409
    | None
):
    """Reset a user's remaining data

     Atomically resets remaining data to zero for package_id, including zero or negative balances. Supply
    package_id only; data is not accepted. System administrators may reset any user; other accounts may
    reset only their direct children. Purchased root orders have their ledger balances cleared; virtual
    child orders have their quota set to usage without changing the parent's pool. Usage history and
    invoices are preserved. Unlimited packages are rejected. Use Idempotency-Key for safe retries so a
    repeated request cannot clear a subsequent top-up.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (ResetDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | UsersDataResetCreateResponse400 | UsersDataResetCreateResponse401 | UsersDataResetCreateResponse403 | UsersDataResetCreateResponse404 | UsersDataResetCreateResponse409
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
    body: ResetDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | UsersDataResetCreateResponse400
    | UsersDataResetCreateResponse401
    | UsersDataResetCreateResponse403
    | UsersDataResetCreateResponse404
    | UsersDataResetCreateResponse409
]:
    """Reset a user's remaining data

     Atomically resets remaining data to zero for package_id, including zero or negative balances. Supply
    package_id only; data is not accepted. System administrators may reset any user; other accounts may
    reset only their direct children. Purchased root orders have their ledger balances cleared; virtual
    child orders have their quota set to usage without changing the parent's pool. Usage history and
    invoices are preserved. Unlimited packages are rejected. Use Idempotency-Key for safe retries so a
    repeated request cannot clear a subsequent top-up.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (ResetDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | UsersDataResetCreateResponse400 | UsersDataResetCreateResponse401 | UsersDataResetCreateResponse403 | UsersDataResetCreateResponse404 | UsersDataResetCreateResponse409]
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
    body: ResetDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | UsersDataResetCreateResponse400
    | UsersDataResetCreateResponse401
    | UsersDataResetCreateResponse403
    | UsersDataResetCreateResponse404
    | UsersDataResetCreateResponse409
    | None
):
    """Reset a user's remaining data

     Atomically resets remaining data to zero for package_id, including zero or negative balances. Supply
    package_id only; data is not accepted. System administrators may reset any user; other accounts may
    reset only their direct children. Purchased root orders have their ledger balances cleared; virtual
    child orders have their quota set to usage without changing the parent's pool. Usage history and
    invoices are preserved. Unlimited packages are rejected. Use Idempotency-Key for safe retries so a
    repeated request cannot clear a subsequent top-up.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (ResetDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | UsersDataResetCreateResponse400 | UsersDataResetCreateResponse401 | UsersDataResetCreateResponse403 | UsersDataResetCreateResponse404 | UsersDataResetCreateResponse409
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
