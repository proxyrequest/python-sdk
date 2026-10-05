from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.google_connect_request_request import GoogleConnectRequestRequest
from ...models.profile_connect_google_response_400 import ProfileConnectGoogleResponse400
from ...models.profile_connect_google_response_401 import ProfileConnectGoogleResponse401
from ...models.profile_connect_google_response_403 import ProfileConnectGoogleResponse403
from ...models.social_account_state import SocialAccountState
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: GoogleConnectRequestRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/profile/social-accounts/google",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfileConnectGoogleResponse400
    | ProfileConnectGoogleResponse401
    | ProfileConnectGoogleResponse403
    | list[SocialAccountState]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SocialAccountState.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ProfileConnectGoogleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfileConnectGoogleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProfileConnectGoogleResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfileConnectGoogleResponse400
    | ProfileConnectGoogleResponse401
    | ProfileConnectGoogleResponse403
    | list[SocialAccountState]
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GoogleConnectRequestRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    ProfileConnectGoogleResponse400
    | ProfileConnectGoogleResponse401
    | ProfileConnectGoogleResponse403
    | list[SocialAccountState]
]:
    """Connect Google to the signed-in account

     Connect a verified Google identity to the signed-in account after confirming its password.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GoogleConnectRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileConnectGoogleResponse400 | ProfileConnectGoogleResponse401 | ProfileConnectGoogleResponse403 | list[SocialAccountState]]
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
    body: GoogleConnectRequestRequest,
    accept_language: str | Unset = UNSET,
) -> (
    ProfileConnectGoogleResponse400
    | ProfileConnectGoogleResponse401
    | ProfileConnectGoogleResponse403
    | list[SocialAccountState]
    | None
):
    """Connect Google to the signed-in account

     Connect a verified Google identity to the signed-in account after confirming its password.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GoogleConnectRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileConnectGoogleResponse400 | ProfileConnectGoogleResponse401 | ProfileConnectGoogleResponse403 | list[SocialAccountState]
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GoogleConnectRequestRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    ProfileConnectGoogleResponse400
    | ProfileConnectGoogleResponse401
    | ProfileConnectGoogleResponse403
    | list[SocialAccountState]
]:
    """Connect Google to the signed-in account

     Connect a verified Google identity to the signed-in account after confirming its password.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GoogleConnectRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileConnectGoogleResponse400 | ProfileConnectGoogleResponse401 | ProfileConnectGoogleResponse403 | list[SocialAccountState]]
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
    body: GoogleConnectRequestRequest,
    accept_language: str | Unset = UNSET,
) -> (
    ProfileConnectGoogleResponse400
    | ProfileConnectGoogleResponse401
    | ProfileConnectGoogleResponse403
    | list[SocialAccountState]
    | None
):
    """Connect Google to the signed-in account

     Connect a verified Google identity to the signed-in account after confirming its password.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GoogleConnectRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileConnectGoogleResponse400 | ProfileConnectGoogleResponse401 | ProfileConnectGoogleResponse403 | list[SocialAccountState]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
