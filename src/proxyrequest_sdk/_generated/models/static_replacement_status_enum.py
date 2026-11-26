from enum import Enum


class StaticReplacementStatusEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    COMPLETED = "completed"
    INELIGIBLE = "ineligible"
    NEEDS_MANUAL = "needs_manual"
    PARTIAL = "partial"
    PENDING = "pending"
    PROCESSING = "processing"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
