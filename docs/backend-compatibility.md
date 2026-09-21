# Backend compatibility and MFA

`openapi/openapi.yaml` is the unfiltered public contract; `openapi/source.json`
records its source commit and SHA-256. Generation excludes only the disabled
`sessions_list` and `sessions_destroy` operations, leaving 79 operations in 17
groups. `client.sessions` and its standalone models are removed. Sticky proxy
generation options remain available.

## Login

Password and Google login both return `TokenPairResponse` (200) or `OTPChallenge`
(202). Complete a challenge before constructing an authenticated client:

```python
from getpass import getpass

from proxyrequest_sdk import Client
from proxyrequest_sdk.models import LoginRequest, OTPChallenge, VerifyOTPRequest

with Client.anonymous() as anonymous:
    result = anonymous.authorization.login(
        body=LoginRequest(email="customer@example.com", password=getpass("Password: "))
    )
    if isinstance(result, OTPChallenge):
        result = anonymous.authorization.verify_otp(
            body=VerifyOTPRequest(challenge=result.challenge, code=getpass("OTP: "))
        )
    access_token = result.token

with Client.with_bearer_token(access_token) as client:
    print(client.profile.get().username)
```

`login_with_google(body=GoogleAuthRequest(credential=credential))` uses the same
union. `AsyncClient` exposes identical resource/model names; await the operations.
Secure refresh-token storage and reauthentication remain the caller's responsibility.

## MFA management

```python
from proxyrequest_sdk.models import (
    TwoFactorConfirmRequest,
    TwoFactorDisableRequest,
    TwoFactorSetupRequestRequest,
)

setup = client.profile.setup_two_factor(
    body=TwoFactorSetupRequestRequest(password=password)
)
# Present setup.otpauth_url securely and ask for an enrollment code.
client.profile.confirm_two_factor(body=TwoFactorConfirmRequest(code=enrollment_code))
# Sign in again before subsequent authenticated operations.
client.profile.disable_two_factor(
    body=TwoFactorDisableRequest(password=password, code=current_code)
)
```

Use a fresh Google `credential` instead of `password` for a Google-authenticated
account. Replacing an enabled authenticator also needs its existing `code` in the
setup body. The doubled `RequestRequest` suffix is the canonical generated model
name. MFA confirmation/disable and password changes can invalidate existing JWTs;
reauthenticate explicitly rather than retrying security mutations automatically.

## Response and error handling

- `User.orders` and legacy allocation fields may be `UNSET` depending on backend
  configuration. Distinguish missing (`UNSET`) from explicit `None`.
- Invoice get/list returns `Invoice | InvoiceShort`; use `isinstance` before
  accessing full-only properties. Creation returns `Invoice`, with nullable
  `package`, `country`, and `coupon`.
- New payment fields are typed. Unknown gateway values remain usable via the
  extensible enum, and unknown response fields remain in additional properties.
- HTTP errors are classified before generated model parsing. Malformed success
  responses raise `ApiError` with status, raw body, headers, and original cause;
  they are not silently retried as a fresh create.
- `*_with_response` methods retain response metadata on successful calls.

The compatibility suite covers sync/async clients with real serializer fixtures,
OTP challenges, nullable and variable responses, and decoding/HTTP failures. No
production mutations are used. See [audit and resolution status](SDK-AUDIT.md).

## Analytics decoding diagnostics

`analytics.list_feed()` returns `FeedResponse` with `count`, `next`, `previous`,
`timezone`, `start`, `end`, and `results`. `analytics.list_domains()` returns
`DomainsResponse` without a total `count`. Feed records support empty identifier
strings and a null `timestamp`. Both endpoints use `limit`/`offset`; an integration
that exposes `page`/`page_size` should translate them to
`limit=page_size, offset=(page-1)*page_size`.

`Unable to decode the ProxyRequest HTTP 200 response.` means that the SDK received
HTTP 200 but could not parse the JSON or construct the response model. The message
alone does not identify the cause. Capture the original exception and request ID:

```python
from importlib.metadata import version

from proxyrequest_sdk import ApiError

try:
    page = client.analytics.list_feed(limit=20, offset=0)
except ApiError as error:
    print("SDK:", version("proxyrequest-sdk"))
    print("HTTP:", error.status_code, "request:", error.request_id)
    print("Decoder:", repr(error.__cause__))
    raise
```

For example, a missing required field produces `KeyError('field_name')`;
non-JSON response content produces `JSONDecodeError`. `error.raw_body` contains
the original bytes for local inspection. Redact customer data before sharing it.
The same diagnostics apply to `AsyncClient` and `*_with_response` calls.

The analytics regression fixtures were rendered by the backend with synthetic
ClickHouse rows; see [fixture provenance](../tests/fixtures/analytics-responses.md).
They cover empty pages, nullable timestamps, timezone offsets, pagination without
a total count, and the reported `Europe/Kiev` date window. Passing these tests does
not establish the shape of a particular deployed server's response.
