from enum import Enum


class PricingEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    BANDWIDTH = "bandwidth"
    FIXED = "fixed"
    RANGE = "range"

    def __str__(self) -> str:
        return str(self.value)
