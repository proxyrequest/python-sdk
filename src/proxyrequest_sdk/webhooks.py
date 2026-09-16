from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import json
import re
from typing import Any

from .errors import InvalidSignatureError


class WebhookVerifier:
    """Verify X-Signature against the exact raw request body."""

    @staticmethod
    def verify(raw_body: bytes | str, signature: str, secret: str) -> bool:
        if not signature or not secret or not re.fullmatch(r"[A-Za-z0-9+/]{43}=", signature):
            return False
        try:
            received = base64.b64decode(signature, validate=True)
        except (ValueError, binascii.Error):
            return False
        if len(received) != 32 or base64.b64encode(received).decode() != signature:
            return False
        body = raw_body.encode() if isinstance(raw_body, str) else raw_body
        expected = hmac.new(secret.encode(), body, hashlib.sha256).digest()
        return hmac.compare_digest(expected, received)

    @staticmethod
    def verify_or_raise(raw_body: bytes | str, signature: str, secret: str) -> None:
        if not WebhookVerifier.verify(raw_body, signature, secret):
            raise InvalidSignatureError("The ProxyRequest webhook signature is invalid.")

    @staticmethod
    def decode_verified_json(raw_body: bytes | str, signature: str, secret: str) -> dict[str, Any]:
        WebhookVerifier.verify_or_raise(raw_body, signature, secret)
        try:
            payload = json.loads(raw_body)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError("The verified webhook body is not valid JSON.") from error
        if not isinstance(payload, dict) or not all(isinstance(key, str) for key in payload):
            raise ValueError("The verified webhook payload must be a JSON object.")
        return payload
