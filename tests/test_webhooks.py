from __future__ import annotations

import base64
import hashlib
import hmac
import json
from pathlib import Path

import pytest

from proxyrequest_sdk import InvalidSignatureError, WebhookVerifier


@pytest.mark.parametrize(
    "vector", json.loads((Path(__file__).parent / "fixtures/webhook-signatures.json").read_text())
)
def test_accountant_base64_vectors(vector: dict[str, str | bool]) -> None:
    body, secret, header = str(vector["body"]), str(vector["secret"]), str(vector["signature"])
    assert (
        base64.b64encode(hmac.new(secret.encode(), body.encode(), hashlib.sha256).digest()).decode()
        == header
    )
    for raw in (body, body.encode()):
        assert WebhookVerifier.verify(raw, header, secret)
        WebhookVerifier.verify_or_raise(raw, header, secret)
    assert not WebhookVerifier.verify(body + " ", header, secret)
    assert not WebhookVerifier.verify(body, header, "wrong")
    if vector["jsonObject"]:
        assert WebhookVerifier.decode_verified_json(body, header, secret) == json.loads(body)
    else:
        with pytest.raises(ValueError):
            WebhookVerifier.decode_verified_json(body, header, secret)


def test_malformed_base64_is_rejected_before_json_decoding() -> None:
    header = "5wDDfJLTJLjXr4cfnNOxikeVi5Cy4qZleyqDMRlZ048="
    for malformed in (
        "",
        " ",
        header[:-1],
        header + "\n",
        header.replace("8=", "9="),
        "A" * 44,
        "A" * 64,
    ):
        assert not WebhookVerifier.verify('{"hello":"world"}', malformed, "super-secret")
        with pytest.raises(InvalidSignatureError):
            WebhookVerifier.decode_verified_json("not json", malformed, "super-secret")
    assert not WebhookVerifier.verify('{"hello":"world"}', header, "")
