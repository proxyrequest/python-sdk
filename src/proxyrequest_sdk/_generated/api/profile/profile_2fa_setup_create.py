from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.profile_2_fa_setup_create_response_400 import Profile2FaSetupCreateResponse400
from ...models.profile_2_fa_setup_create_response_401 import Profile2FaSetupCreateResponse401
from ...models.profile_2_fa_setup_create_response_403 import Profile2FaSetupCreateResponse403
from ...models.two_factor_setup_request_request import TwoFactorSetupRequestRequest
from ...models.two_factor_setup_response import TwoFactorSetupResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: TwoFactorSetupRequestRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/profile/2fa/setup",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Profile2FaSetupCreateResponse400
    | Profile2FaSetupCreateResponse401
    | Profile2FaSetupCreateResponse403
    | TwoFactorSetupResponse
    | None
):
    if response.status_code == 200:
        response_200 = TwoFactorSetupResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Profile2FaSetupCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Profile2FaSetupCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Profile2FaSetupCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Profile2FaSetupCreateResponse400
    | Profile2FaSetupCreateResponse401
    | Profile2FaSetupCreateResponse403
    | TwoFactorSetupResponse
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
    body: TwoFactorSetupRequestRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Profile2FaSetupCreateResponse400
    | Profile2FaSetupCreateResponse401
    | Profile2FaSetupCreateResponse403
    | TwoFactorSetupResponse
]:
    """Prepare two-factor authentication

     Confirms the primary factor and prepares a pending secret without disabling current protection.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (TwoFactorSetupRequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Profile2FaSetupCreateResponse400 | Profile2FaSetupCreateResponse401 | Profile2FaSetupCreateResponse403 | TwoFactorSetupResponse]
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
    body: TwoFactorSetupRequestRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Profile2FaSetupCreateResponse400
    | Profile2FaSetupCreateResponse401
    | Profile2FaSetupCreateResponse403
    | TwoFactorSetupResponse
    | None
):
    """Prepare two-factor authentication

     Confirms the primary factor and prepares a pending secret without disabling current protection.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (TwoFactorSetupRequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Profile2FaSetupCreateResponse400 | Profile2FaSetupCreateResponse401 | Profile2FaSetupCreateResponse403 | TwoFactorSetupResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TwoFactorSetupRequestRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Profile2FaSetupCreateResponse400
    | Profile2FaSetupCreateResponse401
    | Profile2FaSetupCreateResponse403
    | TwoFactorSetupResponse
]:
    """Prepare two-factor authentication

     Confirms the primary factor and prepares a pending secret without disabling current protection.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (TwoFactorSetupRequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Profile2FaSetupCreateResponse400 | Profile2FaSetupCreateResponse401 | Profile2FaSetupCreateResponse403 | TwoFactorSetupResponse]
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
    body: TwoFactorSetupRequestRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Profile2FaSetupCreateResponse400
    | Profile2FaSetupCreateResponse401
    | Profile2FaSetupCreateResponse403
    | TwoFactorSetupResponse
    | None
):
    """Prepare two-factor authentication

     Confirms the primary factor and prepares a pending secret without disabling current protection.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (TwoFactorSetupRequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Profile2FaSetupCreateResponse400 | Profile2FaSetupCreateResponse401 | Profile2FaSetupCreateResponse403 | TwoFactorSetupResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
