from __future__ import annotations

import hashlib
import hmac

import pytest

from proxyrequest_sdk import InvalidSignatureError, WebhookVerifier


def signature(body: bytes, secret: str, timestamp: int) -> str:
    digest = hmac.new(
        secret.encode(),
        str(timestamp).encode() + b"." + body,
        hashlib.sha256,
    ).hexdigest()
    return f"t={timestamp},v1={'0' * 64},v1={digest}"


def test_valid_signature_and_verified_json() -> None:
    body = b'{"event":"invoice.paid","data":{"id":"42"}}'
    header = signature(body, "secret", 1_700_000_000)
    assert WebhookVerifier.verify(body, header, "secret", "1700000000", now=1_700_000_100)
    payload = WebhookVerifier.decode_verified_json(
        body,
        header,
        "secret",
        timestamp_header="1700000000",
        now=1_700_000_100,
    )
    assert payload["event"] == "invoice.paid"


def test_invalid_expired_and_malformed_signatures_are_rejected() -> None:
    body = b"{}"
    header = signature(body, "secret", 1_700_000_000)
    assert not WebhookVerifier.verify(body, header, "secret", now=1_700_001_000)
    assert not WebhookVerifier.verify(body, header, "secret", "1699999999", now=1_700_000_000)
    assert not WebhookVerifier.verify(body, "invalid", "secret", now=1_700_000_000)
    with pytest.raises(InvalidSignatureError):
        WebhookVerifier.verify_or_raise(body, header, "wrong", now=1_700_000_000)


def test_verified_payload_must_be_a_json_object() -> None:
    body = b"[]"
    header = signature(body, "secret", 1_700_000_000)
    with pytest.raises(ValueError, match="JSON object"):
        WebhookVerifier.decode_verified_json(body, header, "secret", now=1_700_000_000)
