from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime


T = TypeVar("T", bound="BandwidthPurchase")


@_attrs_define
class BandwidthPurchase:
    speed_mbps: int
    duration_days: int
    service_value_minor: int
    credit_minor: int
    operation: str
    credited_to_wallet_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speed_mbps = self.speed_mbps

        duration_days = self.duration_days

        service_value_minor = self.service_value_minor

        credit_minor = self.credit_minor

        operation = self.operation

        credited_to_wallet_at: None | str
        if isinstance(self.credited_to_wallet_at, datetime.datetime):
            credited_to_wallet_at = self.credited_to_wallet_at.isoformat()
        else:
            credited_to_wallet_at = self.credited_to_wallet_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speed_mbps": speed_mbps,
                "duration_days": duration_days,
                "service_value_minor": service_value_minor,
                "credit_minor": credit_minor,
                "operation": operation,
                "credited_to_wallet_at": credited_to_wallet_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        speed_mbps = d.pop("speed_mbps")

        duration_days = d.pop("duration_days")

        service_value_minor = d.pop("service_value_minor")

        credit_minor = d.pop("credit_minor")

        operation = d.pop("operation")

        def _parse_credited_to_wallet_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credited_to_wallet_at_type_0 = datetime.datetime.fromisoformat(data)

                return credited_to_wallet_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        credited_to_wallet_at = _parse_credited_to_wallet_at(d.pop("credited_to_wallet_at"))

        bandwidth_purchase = cls(
            speed_mbps=speed_mbps,
            duration_days=duration_days,
            service_value_minor=service_value_minor,
            credit_minor=credit_minor,
            operation=operation,
            credited_to_wallet_at=credited_to_wallet_at,
        )

        bandwidth_purchase.additional_properties = d
        return bandwidth_purchase

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
