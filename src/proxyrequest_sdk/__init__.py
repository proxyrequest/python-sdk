"""Official Python SDK for ProxyRequest."""

from importlib.metadata import PackageNotFoundError, version

from ._generated.types import UNSET, Unset
from .client import DEFAULT_BASE_URL, AsyncClient, Client
from .errors import (
    ApiError,
    ErrorKind,
    InvalidSignatureError,
    PaginationError,
    ProxyRequestError,
)
from .files import FileDownload
from .webhooks import WebhookVerifier

try:
    __version__ = version("proxyrequest-sdk")
except PackageNotFoundError:  # pragma: no cover - source tree without an installed package
    __version__ = "0.0.0"

__all__ = [
    "DEFAULT_BASE_URL",
    "UNSET",
    "ApiError",
    "AsyncClient",
    "Client",
    "ErrorKind",
    "FileDownload",
    "InvalidSignatureError",
    "PaginationError",
    "ProxyRequestError",
    "Unset",
    "WebhookVerifier",
    "__version__",
]
