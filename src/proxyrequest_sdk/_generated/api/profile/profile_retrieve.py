from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.profile_retrieve_response_400 import ProfileRetrieveResponse400
from ...models.profile_retrieve_response_401 import ProfileRetrieveResponse401
from ...models.profile_retrieve_response_403 import ProfileRetrieveResponse403
from ...models.user import User
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/profile",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfileRetrieveResponse400
    | ProfileRetrieveResponse401
    | ProfileRetrieveResponse403
    | User
    | None
):
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfileRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfileRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProfileRetrieveResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfileRetrieveResponse400 | ProfileRetrieveResponse401 | ProfileRetrieveResponse403 | User
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
    accept_language: str | Unset = UNSET,
) -> Response[
    ProfileRetrieveResponse400 | ProfileRetrieveResponse401 | ProfileRetrieveResponse403 | User
]:
    """Get the current profile

     Returns the authenticated account, including contact details and the security state needed by
    account settings screens.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileRetrieveResponse400 | ProfileRetrieveResponse401 | ProfileRetrieveResponse403 | User]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    ProfileRetrieveResponse400
    | ProfileRetrieveResponse401
    | ProfileRetrieveResponse403
    | User
    | None
):
    """Get the current profile

     Returns the authenticated account, including contact details and the security state needed by
    account settings screens.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileRetrieveResponse400 | ProfileRetrieveResponse401 | ProfileRetrieveResponse403 | User
    """

    return sync_detailed(
        client=client,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> Response[
    ProfileRetrieveResponse400 | ProfileRetrieveResponse401 | ProfileRetrieveResponse403 | User
]:
    """Get the current profile

     Returns the authenticated account, including contact details and the security state needed by
    account settings screens.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileRetrieveResponse400 | ProfileRetrieveResponse401 | ProfileRetrieveResponse403 | User]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    ProfileRetrieveResponse400
    | ProfileRetrieveResponse401
    | ProfileRetrieveResponse403
    | User
    | None
):
    """Get the current profile

     Returns the authenticated account, including contact details and the security state needed by
    account settings screens.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileRetrieveResponse400 | ProfileRetrieveResponse401 | ProfileRetrieveResponse403 | User
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
        )
    ).parsed
