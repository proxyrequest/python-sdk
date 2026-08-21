from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.generate_proxy_request import GenerateProxyRequest
from ...models.generate_proxy_response import GenerateProxyResponse
from ...models.proxies_generate_create_response_400 import ProxiesGenerateCreateResponse400
from ...models.proxies_generate_create_response_401 import ProxiesGenerateCreateResponse401
from ...models.proxies_generate_create_response_403 import ProxiesGenerateCreateResponse403
from ...models.proxies_generate_create_response_404 import ProxiesGenerateCreateResponse404
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: GenerateProxyRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/proxies/generate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GenerateProxyResponse
    | ProxiesGenerateCreateResponse400
    | ProxiesGenerateCreateResponse401
    | ProxiesGenerateCreateResponse403
    | ProxiesGenerateCreateResponse404
    | None
):
    if response.status_code == 201:
        response_201 = GenerateProxyResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ProxiesGenerateCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProxiesGenerateCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProxiesGenerateCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProxiesGenerateCreateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GenerateProxyResponse
    | ProxiesGenerateCreateResponse400
    | ProxiesGenerateCreateResponse401
    | ProxiesGenerateCreateResponse403
    | ProxiesGenerateCreateResponse404
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
    body: GenerateProxyRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    GenerateProxyResponse
    | ProxiesGenerateCreateResponse400
    | ProxiesGenerateCreateResponse401
    | ProxiesGenerateCreateResponse403
    | ProxiesGenerateCreateResponse404
]:
    """Generate proxy credentials

     Creates ready-to-use proxy credentials for a purchased package. Use targeting to choose a location
    or provider scope, connection to choose protocol and output format, and session to control sticky
    session lifetime.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GenerateProxyRequest): Validates proxy generation request data and builds generator
            config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateProxyResponse | ProxiesGenerateCreateResponse400 | ProxiesGenerateCreateResponse401 | ProxiesGenerateCreateResponse403 | ProxiesGenerateCreateResponse404]
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
    body: GenerateProxyRequest,
    accept_language: str | Unset = UNSET,
) -> (
    GenerateProxyResponse
    | ProxiesGenerateCreateResponse400
    | ProxiesGenerateCreateResponse401
    | ProxiesGenerateCreateResponse403
    | ProxiesGenerateCreateResponse404
    | None
):
    """Generate proxy credentials

     Creates ready-to-use proxy credentials for a purchased package. Use targeting to choose a location
    or provider scope, connection to choose protocol and output format, and session to control sticky
    session lifetime.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GenerateProxyRequest): Validates proxy generation request data and builds generator
            config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateProxyResponse | ProxiesGenerateCreateResponse400 | ProxiesGenerateCreateResponse401 | ProxiesGenerateCreateResponse403 | ProxiesGenerateCreateResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GenerateProxyRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    GenerateProxyResponse
    | ProxiesGenerateCreateResponse400
    | ProxiesGenerateCreateResponse401
    | ProxiesGenerateCreateResponse403
    | ProxiesGenerateCreateResponse404
]:
    """Generate proxy credentials

     Creates ready-to-use proxy credentials for a purchased package. Use targeting to choose a location
    or provider scope, connection to choose protocol and output format, and session to control sticky
    session lifetime.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GenerateProxyRequest): Validates proxy generation request data and builds generator
            config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateProxyResponse | ProxiesGenerateCreateResponse400 | ProxiesGenerateCreateResponse401 | ProxiesGenerateCreateResponse403 | ProxiesGenerateCreateResponse404]
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
    body: GenerateProxyRequest,
    accept_language: str | Unset = UNSET,
) -> (
    GenerateProxyResponse
    | ProxiesGenerateCreateResponse400
    | ProxiesGenerateCreateResponse401
    | ProxiesGenerateCreateResponse403
    | ProxiesGenerateCreateResponse404
    | None
):
    """Generate proxy credentials

     Creates ready-to-use proxy credentials for a purchased package. Use targeting to choose a location
    or provider scope, connection to choose protocol and output format, and session to control sticky
    session lifetime.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GenerateProxyRequest): Validates proxy generation request data and builds generator
            config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateProxyResponse | ProxiesGenerateCreateResponse400 | ProxiesGenerateCreateResponse401 | ProxiesGenerateCreateResponse403 | ProxiesGenerateCreateResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
