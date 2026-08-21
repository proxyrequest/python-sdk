from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.session_list_response import SessionListResponse
from ...models.sessions_list_response_400 import SessionsListResponse400
from ...models.sessions_list_response_401 import SessionsListResponse401
from ...models.sessions_list_response_403 import SessionsListResponse403
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
        "url": "/sessions",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SessionsListResponse400
    | SessionsListResponse401
    | SessionsListResponse403
    | list[SessionListResponse]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SessionListResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = SessionsListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SessionsListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SessionsListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SessionsListResponse400
    | SessionsListResponse401
    | SessionsListResponse403
    | list[SessionListResponse]
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
    SessionsListResponse400
    | SessionsListResponse401
    | SessionsListResponse403
    | list[SessionListResponse]
]:
    """List active proxy sessions

     Returns sticky proxy session identifiers owned by the authenticated username. At most the configured
    safety limit is returned.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SessionsListResponse400 | SessionsListResponse401 | SessionsListResponse403 | list[SessionListResponse]]
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
    SessionsListResponse400
    | SessionsListResponse401
    | SessionsListResponse403
    | list[SessionListResponse]
    | None
):
    """List active proxy sessions

     Returns sticky proxy session identifiers owned by the authenticated username. At most the configured
    safety limit is returned.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SessionsListResponse400 | SessionsListResponse401 | SessionsListResponse403 | list[SessionListResponse]
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
    SessionsListResponse400
    | SessionsListResponse401
    | SessionsListResponse403
    | list[SessionListResponse]
]:
    """List active proxy sessions

     Returns sticky proxy session identifiers owned by the authenticated username. At most the configured
    safety limit is returned.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SessionsListResponse400 | SessionsListResponse401 | SessionsListResponse403 | list[SessionListResponse]]
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
    SessionsListResponse400
    | SessionsListResponse401
    | SessionsListResponse403
    | list[SessionListResponse]
    | None
):
    """List active proxy sessions

     Returns sticky proxy session identifiers owned by the authenticated username. At most the configured
    safety limit is returned.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SessionsListResponse400 | SessionsListResponse401 | SessionsListResponse403 | list[SessionListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
        )
    ).parsed
