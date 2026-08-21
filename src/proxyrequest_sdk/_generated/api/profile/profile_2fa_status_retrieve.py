from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.enabled_response import EnabledResponse
from ...models.profile_2_fa_status_retrieve_response_400 import Profile2FaStatusRetrieveResponse400
from ...models.profile_2_fa_status_retrieve_response_401 import Profile2FaStatusRetrieveResponse401
from ...models.profile_2_fa_status_retrieve_response_403 import Profile2FaStatusRetrieveResponse403
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
        "url": "/profile/2fa/status",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EnabledResponse
    | Profile2FaStatusRetrieveResponse400
    | Profile2FaStatusRetrieveResponse401
    | Profile2FaStatusRetrieveResponse403
    | None
):
    if response.status_code == 200:
        response_200 = EnabledResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Profile2FaStatusRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Profile2FaStatusRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Profile2FaStatusRetrieveResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EnabledResponse
    | Profile2FaStatusRetrieveResponse400
    | Profile2FaStatusRetrieveResponse401
    | Profile2FaStatusRetrieveResponse403
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
    EnabledResponse
    | Profile2FaStatusRetrieveResponse400
    | Profile2FaStatusRetrieveResponse401
    | Profile2FaStatusRetrieveResponse403
]:
    """Get two-factor status

     Returns whether TOTP two-factor authentication is enabled for the authenticated account.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnabledResponse | Profile2FaStatusRetrieveResponse400 | Profile2FaStatusRetrieveResponse401 | Profile2FaStatusRetrieveResponse403]
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
    EnabledResponse
    | Profile2FaStatusRetrieveResponse400
    | Profile2FaStatusRetrieveResponse401
    | Profile2FaStatusRetrieveResponse403
    | None
):
    """Get two-factor status

     Returns whether TOTP two-factor authentication is enabled for the authenticated account.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnabledResponse | Profile2FaStatusRetrieveResponse400 | Profile2FaStatusRetrieveResponse401 | Profile2FaStatusRetrieveResponse403
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
    EnabledResponse
    | Profile2FaStatusRetrieveResponse400
    | Profile2FaStatusRetrieveResponse401
    | Profile2FaStatusRetrieveResponse403
]:
    """Get two-factor status

     Returns whether TOTP two-factor authentication is enabled for the authenticated account.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnabledResponse | Profile2FaStatusRetrieveResponse400 | Profile2FaStatusRetrieveResponse401 | Profile2FaStatusRetrieveResponse403]
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
    EnabledResponse
    | Profile2FaStatusRetrieveResponse400
    | Profile2FaStatusRetrieveResponse401
    | Profile2FaStatusRetrieveResponse403
    | None
):
    """Get two-factor status

     Returns whether TOTP two-factor authentication is enabled for the authenticated account.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnabledResponse | Profile2FaStatusRetrieveResponse400 | Profile2FaStatusRetrieveResponse401 | Profile2FaStatusRetrieveResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
        )
    ).parsed
