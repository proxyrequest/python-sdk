from enum import Enum


class StatusStatusEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    NOT_STARTED = "not_started"
    PENDING = "pending"
    REJECTED = "rejected"
    REQUIRES_INPUT = "requires_input"
    REVOKED = "revoked"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
