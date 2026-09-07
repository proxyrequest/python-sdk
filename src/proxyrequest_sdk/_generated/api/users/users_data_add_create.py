from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.add_data_request import AddDataRequest
from ...models.order import Order
from ...models.users_data_add_create_response_400 import UsersDataAddCreateResponse400
from ...models.users_data_add_create_response_401 import UsersDataAddCreateResponse401
from ...models.users_data_add_create_response_403 import UsersDataAddCreateResponse403
from ...models.users_data_add_create_response_404 import UsersDataAddCreateResponse404
from ...models.users_data_add_create_response_409 import UsersDataAddCreateResponse409
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: AddDataRequest,
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
        "url": "/users/{id}/data/add".format(
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
    | UsersDataAddCreateResponse400
    | UsersDataAddCreateResponse401
    | UsersDataAddCreateResponse403
    | UsersDataAddCreateResponse404
    | UsersDataAddCreateResponse409
    | None
):
    if response.status_code == 202:
        response_202 = Order.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UsersDataAddCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersDataAddCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersDataAddCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsersDataAddCreateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UsersDataAddCreateResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Order
    | UsersDataAddCreateResponse400
    | UsersDataAddCreateResponse401
    | UsersDataAddCreateResponse403
    | UsersDataAddCreateResponse404
    | UsersDataAddCreateResponse409
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
    body: AddDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | UsersDataAddCreateResponse400
    | UsersDataAddCreateResponse401
    | UsersDataAddCreateResponse403
    | UsersDataAddCreateResponse404
    | UsersDataAddCreateResponse409
]:
    """Add data to a sub-user order

     Adds the requested number of bytes to the selected sub-user's order for the supplied package and
    returns the updated order.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (AddDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | UsersDataAddCreateResponse400 | UsersDataAddCreateResponse401 | UsersDataAddCreateResponse403 | UsersDataAddCreateResponse404 | UsersDataAddCreateResponse409]
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
    body: AddDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | UsersDataAddCreateResponse400
    | UsersDataAddCreateResponse401
    | UsersDataAddCreateResponse403
    | UsersDataAddCreateResponse404
    | UsersDataAddCreateResponse409
    | None
):
    """Add data to a sub-user order

     Adds the requested number of bytes to the selected sub-user's order for the supplied package and
    returns the updated order.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (AddDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | UsersDataAddCreateResponse400 | UsersDataAddCreateResponse401 | UsersDataAddCreateResponse403 | UsersDataAddCreateResponse404 | UsersDataAddCreateResponse409
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
    body: AddDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | UsersDataAddCreateResponse400
    | UsersDataAddCreateResponse401
    | UsersDataAddCreateResponse403
    | UsersDataAddCreateResponse404
    | UsersDataAddCreateResponse409
]:
    """Add data to a sub-user order

     Adds the requested number of bytes to the selected sub-user's order for the supplied package and
    returns the updated order.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (AddDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | UsersDataAddCreateResponse400 | UsersDataAddCreateResponse401 | UsersDataAddCreateResponse403 | UsersDataAddCreateResponse404 | UsersDataAddCreateResponse409]
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
    body: AddDataRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | UsersDataAddCreateResponse400
    | UsersDataAddCreateResponse401
    | UsersDataAddCreateResponse403
    | UsersDataAddCreateResponse404
    | UsersDataAddCreateResponse409
    | None
):
    """Add data to a sub-user order

     Adds the requested number of bytes to the selected sub-user's order for the supplied package and
    returns the updated order.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        body (AddDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | UsersDataAddCreateResponse400 | UsersDataAddCreateResponse401 | UsersDataAddCreateResponse403 | UsersDataAddCreateResponse404 | UsersDataAddCreateResponse409
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
