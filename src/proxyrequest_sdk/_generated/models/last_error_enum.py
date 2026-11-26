from enum import Enum


class LastErrorEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    INSUFFICIENT_BALANCE = "insufficient_balance"
    PAYMENT_UNAVAILABLE = "payment_unavailable"
    TERM_UNAVAILABLE = "term_unavailable"

    def __str__(self) -> str:
        return str(self.value)
