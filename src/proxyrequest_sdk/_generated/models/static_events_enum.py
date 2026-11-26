from enum import Enum


class StaticEventsEnum(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    STATIC_ENDPOINT_EXPIRED = "static.endpoint.expired"
    STATIC_ENDPOINT_REPLACED = "static.endpoint.replaced"
    STATIC_RENTAL_AUTO_RENEWAL_FAILED = "static.rental.auto_renewal_failed"
    STATIC_RENTAL_FULFILLMENT_FINISHED = "static.rental.fulfillment_finished"
    STATIC_RENTAL_REFUNDED = "static.rental.refunded"

    def __str__(self) -> str:
        return str(self.value)
