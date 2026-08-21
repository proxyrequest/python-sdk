from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order import Order
from ...models.subtract_data_request import SubtractDataRequest
from ...models.users_data_subtract_create_response_400 import UsersDataSubtractCreateResponse400
from ...models.users_data_subtract_create_response_401 import UsersDataSubtractCreateResponse401
from ...models.users_data_subtract_create_response_403 import UsersDataSubtractCreateResponse403
from ...models.users_data_subtract_create_response_404 import UsersDataSubtractCreateResponse404
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: SubtractDataRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
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
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: SubtractDataRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
]:
    """Subtract data from a sub-user order

     Subtracts the requested number of bytes from the selected sub-user's order for the supplied package
    and returns the updated order.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (SubtractDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | UsersDataSubtractCreateResponse400 | UsersDataSubtractCreateResponse401 | UsersDataSubtractCreateResponse403 | UsersDataSubtractCreateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
    | None
):
    """Subtract data from a sub-user order

     Subtracts the requested number of bytes from the selected sub-user's order for the supplied package
    and returns the updated order.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (SubtractDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | UsersDataSubtractCreateResponse400 | UsersDataSubtractCreateResponse401 | UsersDataSubtractCreateResponse403 | UsersDataSubtractCreateResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: SubtractDataRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
]:
    """Subtract data from a sub-user order

     Subtracts the requested number of bytes from the selected sub-user's order for the supplied package
    and returns the updated order.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (SubtractDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Order | UsersDataSubtractCreateResponse400 | UsersDataSubtractCreateResponse401 | UsersDataSubtractCreateResponse403 | UsersDataSubtractCreateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: SubtractDataRequest,
    accept_language: str | Unset = UNSET,
) -> (
    Order
    | UsersDataSubtractCreateResponse400
    | UsersDataSubtractCreateResponse401
    | UsersDataSubtractCreateResponse403
    | UsersDataSubtractCreateResponse404
    | None
):
    """Subtract data from a sub-user order

     Subtracts the requested number of bytes from the selected sub-user's order for the supplied package
    and returns the updated order.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (SubtractDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Order | UsersDataSubtractCreateResponse400 | UsersDataSubtractCreateResponse401 | UsersDataSubtractCreateResponse403 | UsersDataSubtractCreateResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
