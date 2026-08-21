from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.webhook_create_request import WebhookCreateRequest
from ...models.webhook_created import WebhookCreated
from ...models.webhooks_create_response_400 import WebhooksCreateResponse400
from ...models.webhooks_create_response_401 import WebhooksCreateResponse401
from ...models.webhooks_create_response_403 import WebhooksCreateResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: WebhookCreateRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    WebhookCreated
    | WebhooksCreateResponse400
    | WebhooksCreateResponse401
    | WebhooksCreateResponse403
    | None
):
    if response.status_code == 201:
        response_201 = WebhookCreated.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = WebhooksCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = WebhooksCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = WebhooksCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    WebhookCreated
    | WebhooksCreateResponse400
    | WebhooksCreateResponse401
    | WebhooksCreateResponse403
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
    body: WebhookCreateRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    WebhookCreated
    | WebhooksCreateResponse400
    | WebhooksCreateResponse401
    | WebhooksCreateResponse403
]:
    """Create a customer webhook

     Registers an HTTPS destination for a supported event type. Private, loopback, and otherwise unsafe
    destinations are rejected.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (WebhookCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookCreated | WebhooksCreateResponse400 | WebhooksCreateResponse401 | WebhooksCreateResponse403]
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
    body: WebhookCreateRequest,
    accept_language: str | Unset = UNSET,
) -> (
    WebhookCreated
    | WebhooksCreateResponse400
    | WebhooksCreateResponse401
    | WebhooksCreateResponse403
    | None
):
    """Create a customer webhook

     Registers an HTTPS destination for a supported event type. Private, loopback, and otherwise unsafe
    destinations are rejected.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (WebhookCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookCreated | WebhooksCreateResponse400 | WebhooksCreateResponse401 | WebhooksCreateResponse403
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookCreateRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    WebhookCreated
    | WebhooksCreateResponse400
    | WebhooksCreateResponse401
    | WebhooksCreateResponse403
]:
    """Create a customer webhook

     Registers an HTTPS destination for a supported event type. Private, loopback, and otherwise unsafe
    destinations are rejected.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (WebhookCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookCreated | WebhooksCreateResponse400 | WebhooksCreateResponse401 | WebhooksCreateResponse403]
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
    body: WebhookCreateRequest,
    accept_language: str | Unset = UNSET,
) -> (
    WebhookCreated
    | WebhooksCreateResponse400
    | WebhooksCreateResponse401
    | WebhooksCreateResponse403
    | None
):
    """Create a customer webhook

     Registers an HTTPS destination for a supported event type. Private, loopback, and otherwise unsafe
    destinations are rejected.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (WebhookCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookCreated | WebhooksCreateResponse400 | WebhooksCreateResponse401 | WebhooksCreateResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed
