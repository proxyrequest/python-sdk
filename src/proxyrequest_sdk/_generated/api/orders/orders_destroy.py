from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_destroy_response_400 import OrdersDestroyResponse400
from ...models.orders_destroy_response_401 import OrdersDestroyResponse401
from ...models.orders_destroy_response_403 import OrdersDestroyResponse403
from ...models.orders_destroy_response_404 import OrdersDestroyResponse404
from ...models.orders_destroy_response_409 import OrdersDestroyResponse409
from ...models.orders_destroy_response_412 import OrdersDestroyResponse412
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/orders/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | OrdersDestroyResponse400
    | OrdersDestroyResponse401
    | OrdersDestroyResponse403
    | OrdersDestroyResponse404
    | OrdersDestroyResponse409
    | OrdersDestroyResponse412
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = OrdersDestroyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersDestroyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersDestroyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersDestroyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = OrdersDestroyResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 412:
        response_412 = OrdersDestroyResponse412.from_dict(response.json())

        return response_412

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | OrdersDestroyResponse400
    | OrdersDestroyResponse401
    | OrdersDestroyResponse403
    | OrdersDestroyResponse404
    | OrdersDestroyResponse409
    | OrdersDestroyResponse412
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
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Any
    | OrdersDestroyResponse400
    | OrdersDestroyResponse401
    | OrdersDestroyResponse403
    | OrdersDestroyResponse404
    | OrdersDestroyResponse409
    | OrdersDestroyResponse412
]:
    """Delete a sub-user order

     Removes an active order owned by a managed sub-user. Remaining data is returned to the reseller's
    matching order when possible.

    Args:
        id (str):
        idempotency_key (str | Unset):
        if_match (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OrdersDestroyResponse400 | OrdersDestroyResponse401 | OrdersDestroyResponse403 | OrdersDestroyResponse404 | OrdersDestroyResponse409 | OrdersDestroyResponse412]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
        if_match=if_match,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Any
    | OrdersDestroyResponse400
    | OrdersDestroyResponse401
    | OrdersDestroyResponse403
    | OrdersDestroyResponse404
    | OrdersDestroyResponse409
    | OrdersDestroyResponse412
    | None
):
    """Delete a sub-user order

     Removes an active order owned by a managed sub-user. Remaining data is returned to the reseller's
    matching order when possible.

    Args:
        id (str):
        idempotency_key (str | Unset):
        if_match (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OrdersDestroyResponse400 | OrdersDestroyResponse401 | OrdersDestroyResponse403 | OrdersDestroyResponse404 | OrdersDestroyResponse409 | OrdersDestroyResponse412
    """

    return sync_detailed(
        id=id,
        client=client,
        idempotency_key=idempotency_key,
        if_match=if_match,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Any
    | OrdersDestroyResponse400
    | OrdersDestroyResponse401
    | OrdersDestroyResponse403
    | OrdersDestroyResponse404
    | OrdersDestroyResponse409
    | OrdersDestroyResponse412
]:
    """Delete a sub-user order

     Removes an active order owned by a managed sub-user. Remaining data is returned to the reseller's
    matching order when possible.

    Args:
        id (str):
        idempotency_key (str | Unset):
        if_match (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OrdersDestroyResponse400 | OrdersDestroyResponse401 | OrdersDestroyResponse403 | OrdersDestroyResponse404 | OrdersDestroyResponse409 | OrdersDestroyResponse412]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
        if_match=if_match,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Any
    | OrdersDestroyResponse400
    | OrdersDestroyResponse401
    | OrdersDestroyResponse403
    | OrdersDestroyResponse404
    | OrdersDestroyResponse409
    | OrdersDestroyResponse412
    | None
):
    """Delete a sub-user order

     Removes an active order owned by a managed sub-user. Remaining data is returned to the reseller's
    matching order when possible.

    Args:
        id (str):
        idempotency_key (str | Unset):
        if_match (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OrdersDestroyResponse400 | OrdersDestroyResponse401 | OrdersDestroyResponse403 | OrdersDestroyResponse404 | OrdersDestroyResponse409 | OrdersDestroyResponse412
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            idempotency_key=idempotency_key,
            if_match=if_match,
            accept_language=accept_language,
        )
    ).parsed
