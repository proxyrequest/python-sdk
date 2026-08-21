from __future__ import annotations

import hashlib
import hmac
import json
import re
import time
from typing import Any

from .errors import InvalidSignatureError


class WebhookVerifier:
    """Verify ProxyRequest webhook signatures against the exact raw request body."""

    @staticmethod
    def verify(
        raw_body: bytes | str,
        signature: str,
        secret: str,
        timestamp_header: str | None = None,
        tolerance: int | None = 300,
        now: int | None = None,
    ) -> bool:
        if not signature or not secret or (tolerance is not None and tolerance < 0):
            return False
        parsed = _parse_signature(signature)
        if parsed is None:
            return False
        timestamp, received = parsed
        if timestamp_header is not None:
            header = timestamp_header.strip()
            if not header.isdigit() or int(header) != timestamp:
                return False
        if (
            tolerance is not None
            and abs((int(time.time()) if now is None else now) - timestamp) > tolerance
        ):
            return False
        body = raw_body.encode() if isinstance(raw_body, str) else raw_body
        expected = hmac.new(
            secret.encode(), str(timestamp).encode() + b"." + body, hashlib.sha256
        ).hexdigest()
        return any(hmac.compare_digest(expected, candidate.lower()) for candidate in received)

    @staticmethod
    def verify_or_raise(
        raw_body: bytes | str,
        signature: str,
        secret: str,
        timestamp_header: str | None = None,
        tolerance: int | None = 300,
        now: int | None = None,
    ) -> None:
        if not WebhookVerifier.verify(
            raw_body, signature, secret, timestamp_header, tolerance, now
        ):
            raise InvalidSignatureError("The ProxyRequest webhook signature is invalid or expired.")

    @staticmethod
    def decode_verified_json(
        raw_body: bytes | str,
        signature: str,
        secret: str,
        timestamp_header: str | None = None,
        tolerance: int | None = 300,
        now: int | None = None,
    ) -> dict[str, Any]:
        WebhookVerifier.verify_or_raise(
            raw_body, signature, secret, timestamp_header, tolerance, now
        )
        try:
            payload = json.loads(raw_body)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError("The verified webhook body is not valid JSON.") from error
        if not isinstance(payload, dict) or not all(isinstance(key, str) for key in payload):
            raise ValueError("The verified webhook payload must be a JSON object.")
        return payload


def _parse_signature(signature: str) -> tuple[int, list[str]] | None:
    timestamp: int | None = None
    signatures: list[str] = []
    for part in signature.split(","):
        pair = part.strip().split("=", 1)
        if len(pair) != 2:
            return None
        key, value = pair
        if key == "t":
            if timestamp is not None or not value.isdigit() or len(value) > 19:
                return None
            timestamp = int(value)
        elif key == "v1" and re.fullmatch(r"[a-fA-F0-9]{64}", value):
            signatures.append(value)
    return (timestamp, signatures) if timestamp is not None and signatures else None
