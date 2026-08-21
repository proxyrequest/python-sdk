from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user import User
from ...models.users_retrieve_response_400 import UsersRetrieveResponse400
from ...models.users_retrieve_response_401 import UsersRetrieveResponse401
from ...models.users_retrieve_response_403 import UsersRetrieveResponse403
from ...models.users_retrieve_response_404 import UsersRetrieveResponse404
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    User
    | UsersRetrieveResponse400
    | UsersRetrieveResponse401
    | UsersRetrieveResponse403
    | UsersRetrieveResponse404
    | None
):
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UsersRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsersRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    User
    | UsersRetrieveResponse400
    | UsersRetrieveResponse401
    | UsersRetrieveResponse403
    | UsersRetrieveResponse404
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
    accept_language: str | Unset = UNSET,
) -> Response[
    User
    | UsersRetrieveResponse400
    | UsersRetrieveResponse401
    | UsersRetrieveResponse403
    | UsersRetrieveResponse404
]:
    """Get a user

     Returns a user that is visible within the caller's account scope.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User | UsersRetrieveResponse400 | UsersRetrieveResponse401 | UsersRetrieveResponse403 | UsersRetrieveResponse404]
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
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    User
    | UsersRetrieveResponse400
    | UsersRetrieveResponse401
    | UsersRetrieveResponse403
    | UsersRetrieveResponse404
    | None
):
    """Get a user

     Returns a user that is visible within the caller's account scope.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User | UsersRetrieveResponse400 | UsersRetrieveResponse401 | UsersRetrieveResponse403 | UsersRetrieveResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> Response[
    User
    | UsersRetrieveResponse400
    | UsersRetrieveResponse401
    | UsersRetrieveResponse403
    | UsersRetrieveResponse404
]:
    """Get a user

     Returns a user that is visible within the caller's account scope.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User | UsersRetrieveResponse400 | UsersRetrieveResponse401 | UsersRetrieveResponse403 | UsersRetrieveResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    User
    | UsersRetrieveResponse400
    | UsersRetrieveResponse401
    | UsersRetrieveResponse403
    | UsersRetrieveResponse404
    | None
):
    """Get a user

     Returns a user that is visible within the caller's account scope.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User | UsersRetrieveResponse400 | UsersRetrieveResponse401 | UsersRetrieveResponse403 | UsersRetrieveResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            accept_language=accept_language,
        )
    ).parsed
