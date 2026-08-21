from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patched_profile_update_request import PatchedProfileUpdateRequest
from ...models.profile_partial_update_response_400 import ProfilePartialUpdateResponse400
from ...models.profile_partial_update_response_401 import ProfilePartialUpdateResponse401
from ...models.profile_partial_update_response_403 import ProfilePartialUpdateResponse403
from ...models.user import User
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: PatchedProfileUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/profile",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfilePartialUpdateResponse400
    | ProfilePartialUpdateResponse401
    | ProfilePartialUpdateResponse403
    | User
    | None
):
    if response.status_code == 202:
        response_202 = User.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ProfilePartialUpdateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfilePartialUpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProfilePartialUpdateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfilePartialUpdateResponse400
    | ProfilePartialUpdateResponse401
    | ProfilePartialUpdateResponse403
    | User
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
    body: PatchedProfileUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    ProfilePartialUpdateResponse400
    | ProfilePartialUpdateResponse401
    | ProfilePartialUpdateResponse403
    | User
]:
    """Update the current profile

     Updates the supplied profile fields and returns the latest account state. Fields omitted from the
    request are left unchanged.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedProfileUpdateRequest | Unset): for updating user profile information with
            comprehensive validation. Handles personal profile data, company information, security
            settings, and password changes. All fields are optional, but at least one field must be
            provided for the update to be valid. Includes validation for domain patterns with support
            for wildcards (*.example.com) and subdomains.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfilePartialUpdateResponse400 | ProfilePartialUpdateResponse401 | ProfilePartialUpdateResponse403 | User]
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
    body: PatchedProfileUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    ProfilePartialUpdateResponse400
    | ProfilePartialUpdateResponse401
    | ProfilePartialUpdateResponse403
    | User
    | None
):
    """Update the current profile

     Updates the supplied profile fields and returns the latest account state. Fields omitted from the
    request are left unchanged.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedProfileUpdateRequest | Unset): for updating user profile information with
            comprehensive validation. Handles personal profile data, company information, security
            settings, and password changes. All fields are optional, but at least one field must be
            provided for the update to be valid. Includes validation for domain patterns with support
            for wildcards (*.example.com) and subdomains.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfilePartialUpdateResponse400 | ProfilePartialUpdateResponse401 | ProfilePartialUpdateResponse403 | User
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchedProfileUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    ProfilePartialUpdateResponse400
    | ProfilePartialUpdateResponse401
    | ProfilePartialUpdateResponse403
    | User
]:
    """Update the current profile

     Updates the supplied profile fields and returns the latest account state. Fields omitted from the
    request are left unchanged.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedProfileUpdateRequest | Unset): for updating user profile information with
            comprehensive validation. Handles personal profile data, company information, security
            settings, and password changes. All fields are optional, but at least one field must be
            provided for the update to be valid. Includes validation for domain patterns with support
            for wildcards (*.example.com) and subdomains.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfilePartialUpdateResponse400 | ProfilePartialUpdateResponse401 | ProfilePartialUpdateResponse403 | User]
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
    body: PatchedProfileUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    ProfilePartialUpdateResponse400
    | ProfilePartialUpdateResponse401
    | ProfilePartialUpdateResponse403
    | User
    | None
):
    """Update the current profile

     Updates the supplied profile fields and returns the latest account state. Fields omitted from the
    request are left unchanged.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedProfileUpdateRequest | Unset): for updating user profile information with
            comprehensive validation. Handles personal profile data, company information, security
            settings, and password changes. All fields are optional, but at least one field must be
            provided for the update to be valid. Includes validation for domain patterns with support
            for wildcards (*.example.com) and subdomains.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfilePartialUpdateResponse400 | ProfilePartialUpdateResponse401 | ProfilePartialUpdateResponse403 | User
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
