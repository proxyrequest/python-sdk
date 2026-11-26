from enum import Enum


class StaticRentalStatusEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    EXPIRED = "expired"
    FULFILLED = "fulfilled"
    PAID_UNFULFILLED = "paid_unfulfilled"
    PARTIALLY_FULFILLED = "partially_fulfilled"
    PARTIALLY_REFUNDED = "partially_refunded"
    PROVISIONING = "provisioning"
    REFUNDED = "refunded"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
