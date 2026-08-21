from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.sign_up_request import SignUpRequest
from ...models.signup_create_response_400 import SignupCreateResponse400
from ...models.signup_create_response_403 import SignupCreateResponse403
from ...models.token_pair_response import TokenPairResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: SignUpRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/signup",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse | None:
    if response.status_code == 201:
        response_201 = TokenPairResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = SignupCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = SignupCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SignUpRequest,
    accept_language: str | Unset = UNSET,
) -> Response[SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse]:
    """Create a customer account

     Creates an account after validating the email, password, and Cloudflare Turnstile token. Referral
    and affiliate codes are optional.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (SignUpRequest): Comprehensive user registration with enhanced validation, security
            measures, and referral/affiliate code handling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse]
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
    body: SignUpRequest,
    accept_language: str | Unset = UNSET,
) -> SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse | None:
    """Create a customer account

     Creates an account after validating the email, password, and Cloudflare Turnstile token. Referral
    and affiliate codes are optional.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (SignUpRequest): Comprehensive user registration with enhanced validation, security
            measures, and referral/affiliate code handling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SignUpRequest,
    accept_language: str | Unset = UNSET,
) -> Response[SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse]:
    """Create a customer account

     Creates an account after validating the email, password, and Cloudflare Turnstile token. Referral
    and affiliate codes are optional.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (SignUpRequest): Comprehensive user registration with enhanced validation, security
            measures, and referral/affiliate code handling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse]
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
    body: SignUpRequest,
    accept_language: str | Unset = UNSET,
) -> SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse | None:
    """Create a customer account

     Creates an account after validating the email, password, and Cloudflare Turnstile token. Referral
    and affiliate codes are optional.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (SignUpRequest): Comprehensive user registration with enhanced validation, security
            measures, and referral/affiliate code handling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SignupCreateResponse400 | SignupCreateResponse403 | TokenPairResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
