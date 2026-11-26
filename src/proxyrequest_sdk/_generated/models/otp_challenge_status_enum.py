from enum import Enum


class OTPChallengeStatusEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    OTP_REQUIRED = "otp_required"

    def __str__(self) -> str:
        return str(self.value)
