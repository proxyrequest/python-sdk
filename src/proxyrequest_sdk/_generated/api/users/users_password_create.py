from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user import User
from ...models.user_password_reset_request import UserPasswordResetRequest
from ...models.users_password_create_response_400 import UsersPasswordCreateResponse400
from ...models.users_password_create_response_401 import UsersPasswordCreateResponse401
from ...models.users_password_create_response_403 import UsersPasswordCreateResponse403
from ...models.users_password_create_response_404 import UsersPasswordCreateResponse404
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: UserPasswordResetRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/{id}/password".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    User
    | UsersPasswordCreateResponse400
    | UsersPasswordCreateResponse401
    | UsersPasswordCreateResponse403
    | UsersPasswordCreateResponse404
    | None
):
    if response.status_code == 202:
        response_202 = User.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UsersPasswordCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersPasswordCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersPasswordCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsersPasswordCreateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    User
    | UsersPasswordCreateResponse400
    | UsersPasswordCreateResponse401
    | UsersPasswordCreateResponse403
    | UsersPasswordCreateResponse404
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
    body: UserPasswordResetRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    User
    | UsersPasswordCreateResponse400
    | UsersPasswordCreateResponse401
    | UsersPasswordCreateResponse403
    | UsersPasswordCreateResponse404
]:
    """Rotate a sub-user proxy password

     Rotates the proxy password for the selected user. When package-based authentication is enabled, send
    package_id to select the affected order.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (UserPasswordResetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User | UsersPasswordCreateResponse400 | UsersPasswordCreateResponse401 | UsersPasswordCreateResponse403 | UsersPasswordCreateResponse404]
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
    body: UserPasswordResetRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    User
    | UsersPasswordCreateResponse400
    | UsersPasswordCreateResponse401
    | UsersPasswordCreateResponse403
    | UsersPasswordCreateResponse404
    | None
):
    """Rotate a sub-user proxy password

     Rotates the proxy password for the selected user. When package-based authentication is enabled, send
    package_id to select the affected order.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (UserPasswordResetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User | UsersPasswordCreateResponse400 | UsersPasswordCreateResponse401 | UsersPasswordCreateResponse403 | UsersPasswordCreateResponse404
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
    body: UserPasswordResetRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    User
    | UsersPasswordCreateResponse400
    | UsersPasswordCreateResponse401
    | UsersPasswordCreateResponse403
    | UsersPasswordCreateResponse404
]:
    """Rotate a sub-user proxy password

     Rotates the proxy password for the selected user. When package-based authentication is enabled, send
    package_id to select the affected order.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (UserPasswordResetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User | UsersPasswordCreateResponse400 | UsersPasswordCreateResponse401 | UsersPasswordCreateResponse403 | UsersPasswordCreateResponse404]
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
    body: UserPasswordResetRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    User
    | UsersPasswordCreateResponse400
    | UsersPasswordCreateResponse401
    | UsersPasswordCreateResponse403
    | UsersPasswordCreateResponse404
    | None
):
    """Rotate a sub-user proxy password

     Rotates the proxy password for the selected user. When package-based authentication is enabled, send
    package_id to select the affected order.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (UserPasswordResetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User | UsersPasswordCreateResponse400 | UsersPasswordCreateResponse401 | UsersPasswordCreateResponse403 | UsersPasswordCreateResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
