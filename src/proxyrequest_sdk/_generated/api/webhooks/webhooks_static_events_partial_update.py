from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patched_static_webhook_subscription_request import (
    PatchedStaticWebhookSubscriptionRequest,
)
from ...models.static_webhook_subscription import StaticWebhookSubscription
from ...models.webhooks_static_events_partial_update_response_400 import (
    WebhooksStaticEventsPartialUpdateResponse400,
)
from ...models.webhooks_static_events_partial_update_response_401 import (
    WebhooksStaticEventsPartialUpdateResponse401,
)
from ...models.webhooks_static_events_partial_update_response_403 import (
    WebhooksStaticEventsPartialUpdateResponse403,
)
from ...models.webhooks_static_events_partial_update_response_404 import (
    WebhooksStaticEventsPartialUpdateResponse404,
)
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: PatchedStaticWebhookSubscriptionRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/webhooks/{id}/static-events".format(
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
    StaticWebhookSubscription
    | WebhooksStaticEventsPartialUpdateResponse400
    | WebhooksStaticEventsPartialUpdateResponse401
    | WebhooksStaticEventsPartialUpdateResponse403
    | WebhooksStaticEventsPartialUpdateResponse404
    | None
):
    if response.status_code == 200:
        response_200 = StaticWebhookSubscription.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = WebhooksStaticEventsPartialUpdateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = WebhooksStaticEventsPartialUpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = WebhooksStaticEventsPartialUpdateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = WebhooksStaticEventsPartialUpdateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StaticWebhookSubscription
    | WebhooksStaticEventsPartialUpdateResponse400
    | WebhooksStaticEventsPartialUpdateResponse401
    | WebhooksStaticEventsPartialUpdateResponse403
    | WebhooksStaticEventsPartialUpdateResponse404
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedStaticWebhookSubscriptionRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticWebhookSubscription
    | WebhooksStaticEventsPartialUpdateResponse400
    | WebhooksStaticEventsPartialUpdateResponse401
    | WebhooksStaticEventsPartialUpdateResponse403
    | WebhooksStaticEventsPartialUpdateResponse404
]:
    """Replace static rental event subscriptions

     Replace the set of static rental event types delivered to the owned user webhook. An empty list
    disables static events.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PatchedStaticWebhookSubscriptionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticWebhookSubscription | WebhooksStaticEventsPartialUpdateResponse400 | WebhooksStaticEventsPartialUpdateResponse401 | WebhooksStaticEventsPartialUpdateResponse403 | WebhooksStaticEventsPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedStaticWebhookSubscriptionRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticWebhookSubscription
    | WebhooksStaticEventsPartialUpdateResponse400
    | WebhooksStaticEventsPartialUpdateResponse401
    | WebhooksStaticEventsPartialUpdateResponse403
    | WebhooksStaticEventsPartialUpdateResponse404
    | None
):
    """Replace static rental event subscriptions

     Replace the set of static rental event types delivered to the owned user webhook. An empty list
    disables static events.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PatchedStaticWebhookSubscriptionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticWebhookSubscription | WebhooksStaticEventsPartialUpdateResponse400 | WebhooksStaticEventsPartialUpdateResponse401 | WebhooksStaticEventsPartialUpdateResponse403 | WebhooksStaticEventsPartialUpdateResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedStaticWebhookSubscriptionRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticWebhookSubscription
    | WebhooksStaticEventsPartialUpdateResponse400
    | WebhooksStaticEventsPartialUpdateResponse401
    | WebhooksStaticEventsPartialUpdateResponse403
    | WebhooksStaticEventsPartialUpdateResponse404
]:
    """Replace static rental event subscriptions

     Replace the set of static rental event types delivered to the owned user webhook. An empty list
    disables static events.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PatchedStaticWebhookSubscriptionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticWebhookSubscription | WebhooksStaticEventsPartialUpdateResponse400 | WebhooksStaticEventsPartialUpdateResponse401 | WebhooksStaticEventsPartialUpdateResponse403 | WebhooksStaticEventsPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedStaticWebhookSubscriptionRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticWebhookSubscription
    | WebhooksStaticEventsPartialUpdateResponse400
    | WebhooksStaticEventsPartialUpdateResponse401
    | WebhooksStaticEventsPartialUpdateResponse403
    | WebhooksStaticEventsPartialUpdateResponse404
    | None
):
    """Replace static rental event subscriptions

     Replace the set of static rental event types delivered to the owned user webhook. An empty list
    disables static events.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PatchedStaticWebhookSubscriptionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticWebhookSubscription | WebhooksStaticEventsPartialUpdateResponse400 | WebhooksStaticEventsPartialUpdateResponse401 | WebhooksStaticEventsPartialUpdateResponse403 | WebhooksStaticEventsPartialUpdateResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
