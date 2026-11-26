from enum import Enum


class KycProviderEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    IDENFY = "idenfy"
    JUMIO = "jumio"
    STRIPE = "stripe"
    SUMSUB = "sumsub"
    TRULIOO = "trulioo"
    VERIFF = "veriff"

    def __str__(self) -> str:
        return str(self.value)
