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
  responses raise `ApiError` with status, raw body, headers, original cause, and
  the actual idempotency key; they are not silently retried as a fresh create.
- `*_with_response` methods retain response metadata on successful calls.

The compatibility suite covers sync/async clients with real serializer fixtures,
OTP challenges, nullable and variable responses, and decoding/HTTP failures. No
production mutations are used. See [audit and resolution status](SDK-AUDIT.md).
