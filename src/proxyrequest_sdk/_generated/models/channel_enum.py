from enum import Enum


class ChannelEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    ADMIN_PANEL = "admin_panel"
    PUBLIC_API = "public_api"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
