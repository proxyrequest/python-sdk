from enum import Enum


class ProviderEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    DISCORD = "discord"
    GOOGLE = "google"
    META = "meta"
    TWITTER = "twitter"

    def __str__(self) -> str:
        return str(self.value)
