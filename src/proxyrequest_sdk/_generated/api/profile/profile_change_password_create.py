from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.change_password_request import ChangePasswordRequest
from ...models.message_response import MessageResponse
from ...models.profile_change_password_create_response_400 import (
    ProfileChangePasswordCreateResponse400,
)
from ...models.profile_change_password_create_response_401 import (
    ProfileChangePasswordCreateResponse401,
)
from ...models.profile_change_password_create_response_403 import (
    ProfileChangePasswordCreateResponse403,
)
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: ChangePasswordRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/profile/change-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    MessageResponse
    | ProfileChangePasswordCreateResponse400
    | ProfileChangePasswordCreateResponse401
    | ProfileChangePasswordCreateResponse403
    | None
):
    if response.status_code == 200:
        response_200 = MessageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfileChangePasswordCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfileChangePasswordCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProfileChangePasswordCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    MessageResponse
    | ProfileChangePasswordCreateResponse400
    | ProfileChangePasswordCreateResponse401
    | ProfileChangePasswordCreateResponse403
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
    body: ChangePasswordRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    MessageResponse
    | ProfileChangePasswordCreateResponse400
    | ProfileChangePasswordCreateResponse401
    | ProfileChangePasswordCreateResponse403
]:
    """Change the account password

     Verifies the current password, applies the new password, and keeps the current authenticated session
    active.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (ChangePasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageResponse | ProfileChangePasswordCreateResponse400 | ProfileChangePasswordCreateResponse401 | ProfileChangePasswordCreateResponse403]
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
    body: ChangePasswordRequest,
    accept_language: str | Unset = UNSET,
) -> (
    MessageResponse
    | ProfileChangePasswordCreateResponse400
    | ProfileChangePasswordCreateResponse401
    | ProfileChangePasswordCreateResponse403
    | None
):
    """Change the account password

     Verifies the current password, applies the new password, and keeps the current authenticated session
    active.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (ChangePasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageResponse | ProfileChangePasswordCreateResponse400 | ProfileChangePasswordCreateResponse401 | ProfileChangePasswordCreateResponse403
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChangePasswordRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    MessageResponse
    | ProfileChangePasswordCreateResponse400
    | ProfileChangePasswordCreateResponse401
    | ProfileChangePasswordCreateResponse403
]:
    """Change the account password

     Verifies the current password, applies the new password, and keeps the current authenticated session
    active.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (ChangePasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageResponse | ProfileChangePasswordCreateResponse400 | ProfileChangePasswordCreateResponse401 | ProfileChangePasswordCreateResponse403]
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
    body: ChangePasswordRequest,
    accept_language: str | Unset = UNSET,
) -> (
    MessageResponse
    | ProfileChangePasswordCreateResponse400
    | ProfileChangePasswordCreateResponse401
    | ProfileChangePasswordCreateResponse403
    | None
):
    """Change the account password

     Verifies the current password, applies the new password, and keeps the current authenticated session
    active.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (ChangePasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageResponse | ProfileChangePasswordCreateResponse400 | ProfileChangePasswordCreateResponse401 | ProfileChangePasswordCreateResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
