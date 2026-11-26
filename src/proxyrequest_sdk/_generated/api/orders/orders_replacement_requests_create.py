from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_replacement_requests_create_response_400 import (
    OrdersReplacementRequestsCreateResponse400,
)
from ...models.orders_replacement_requests_create_response_401 import (
    OrdersReplacementRequestsCreateResponse401,
)
from ...models.orders_replacement_requests_create_response_403 import (
    OrdersReplacementRequestsCreateResponse403,
)
from ...models.orders_replacement_requests_create_response_404 import (
    OrdersReplacementRequestsCreateResponse404,
)
from ...models.replacement_request_request import ReplacementRequestRequest
from ...models.replacement_response import ReplacementResponse
from ...models.static_mutation_error import StaticMutationError
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: ReplacementRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/orders/{id}/replacement-requests".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OrdersReplacementRequestsCreateResponse400
    | OrdersReplacementRequestsCreateResponse401
    | OrdersReplacementRequestsCreateResponse403
    | OrdersReplacementRequestsCreateResponse404
    | ReplacementResponse
    | StaticMutationError
    | None
):
    if response.status_code == 201:
        response_201 = ReplacementResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = OrdersReplacementRequestsCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersReplacementRequestsCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersReplacementRequestsCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersReplacementRequestsCreateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = StaticMutationError.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrdersReplacementRequestsCreateResponse400
    | OrdersReplacementRequestsCreateResponse401
    | OrdersReplacementRequestsCreateResponse403
    | OrdersReplacementRequestsCreateResponse404
    | ReplacementResponse
    | StaticMutationError
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ReplacementRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersReplacementRequestsCreateResponse400
    | OrdersReplacementRequestsCreateResponse401
    | OrdersReplacementRequestsCreateResponse403
    | OrdersReplacementRequestsCreateResponse404
    | ReplacementResponse
    | StaticMutationError
]:
    """Request an IP replacement

     Submit distinct active endpoints from one owned order and a reason for administrator approval. A
    custom reason is limited to 255 characters. Pending requests do not reserve inventory or change the
    paid rental period.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (ReplacementRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersReplacementRequestsCreateResponse400 | OrdersReplacementRequestsCreateResponse401 | OrdersReplacementRequestsCreateResponse403 | OrdersReplacementRequestsCreateResponse404 | ReplacementResponse | StaticMutationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ReplacementRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersReplacementRequestsCreateResponse400
    | OrdersReplacementRequestsCreateResponse401
    | OrdersReplacementRequestsCreateResponse403
    | OrdersReplacementRequestsCreateResponse404
    | ReplacementResponse
    | StaticMutationError
    | None
):
    """Request an IP replacement

     Submit distinct active endpoints from one owned order and a reason for administrator approval. A
    custom reason is limited to 255 characters. Pending requests do not reserve inventory or change the
    paid rental period.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (ReplacementRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersReplacementRequestsCreateResponse400 | OrdersReplacementRequestsCreateResponse401 | OrdersReplacementRequestsCreateResponse403 | OrdersReplacementRequestsCreateResponse404 | ReplacementResponse | StaticMutationError
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ReplacementRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersReplacementRequestsCreateResponse400
    | OrdersReplacementRequestsCreateResponse401
    | OrdersReplacementRequestsCreateResponse403
    | OrdersReplacementRequestsCreateResponse404
    | ReplacementResponse
    | StaticMutationError
]:
    """Request an IP replacement

     Submit distinct active endpoints from one owned order and a reason for administrator approval. A
    custom reason is limited to 255 characters. Pending requests do not reserve inventory or change the
    paid rental period.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (ReplacementRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersReplacementRequestsCreateResponse400 | OrdersReplacementRequestsCreateResponse401 | OrdersReplacementRequestsCreateResponse403 | OrdersReplacementRequestsCreateResponse404 | ReplacementResponse | StaticMutationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ReplacementRequestRequest,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersReplacementRequestsCreateResponse400
    | OrdersReplacementRequestsCreateResponse401
    | OrdersReplacementRequestsCreateResponse403
    | OrdersReplacementRequestsCreateResponse404
    | ReplacementResponse
    | StaticMutationError
    | None
):
    """Request an IP replacement

     Submit distinct active endpoints from one owned order and a reason for administrator approval. A
    custom reason is limited to 255 characters. Pending requests do not reserve inventory or change the
    paid rental period.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (ReplacementRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersReplacementRequestsCreateResponse400 | OrdersReplacementRequestsCreateResponse401 | OrdersReplacementRequestsCreateResponse403 | OrdersReplacementRequestsCreateResponse404 | ReplacementResponse | StaticMutationError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed
