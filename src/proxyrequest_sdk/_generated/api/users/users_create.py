from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user import User
from ...models.user_create_request import UserCreateRequest
from ...models.users_create_response_400 import UsersCreateResponse400
from ...models.users_create_response_401 import UsersCreateResponse401
from ...models.users_create_response_403 import UsersCreateResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: UserCreateRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403 | None:
    if response.status_code == 201:
        response_201 = User.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = UsersCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserCreateRequest,
    accept_language: str | Unset = UNSET,
) -> Response[User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403]:
    """Create a sub-user

     Creates a user owned by the authenticated reseller and returns the new account. The caller must be
    allowed to manage sub-users.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (UserCreateRequest): Fields accepted when a reseller or administrator creates a
            customer account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UserCreateRequest,
    accept_language: str | Unset = UNSET,
) -> User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403 | None:
    """Create a sub-user

     Creates a user owned by the authenticated reseller and returns the new account. The caller must be
    allowed to manage sub-users.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (UserCreateRequest): Fields accepted when a reseller or administrator creates a
            customer account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserCreateRequest,
    accept_language: str | Unset = UNSET,
) -> Response[User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403]:
    """Create a sub-user

     Creates a user owned by the authenticated reseller and returns the new account. The caller must be
    allowed to manage sub-users.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (UserCreateRequest): Fields accepted when a reseller or administrator creates a
            customer account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserCreateRequest,
    accept_language: str | Unset = UNSET,
) -> User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403 | None:
    """Create a sub-user

     Creates a user owned by the authenticated reseller and returns the new account. The caller must be
    allowed to manage sub-users.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (UserCreateRequest): Fields accepted when a reseller or administrator creates a
            customer account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User | UsersCreateResponse400 | UsersCreateResponse401 | UsersCreateResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
