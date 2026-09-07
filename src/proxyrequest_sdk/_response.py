from __future__ import annotations

from collections.abc import Callable
from typing import Any

import httpx

from .errors import ApiError


def parse_response(parser: Callable[..., Any], *, client: Any, response: httpx.Response) -> Any:
    """Classify HTTP failures before model parsing, retaining the original response."""
    if not 200 <= response.status_code < 300:
        raise ApiError.from_response(response.status_code, response.content, response.headers)
    try:
        parsed = parser(client=client, response=response)
        if parsed is None and response.content and response.status_code not in {204, 205}:
            raise ValueError("No model exists for this successful response.")
        return parsed
    except Exception as error:
        raise ApiError.decoding(
            response.status_code, response.content, response.headers, error
        ) from error
