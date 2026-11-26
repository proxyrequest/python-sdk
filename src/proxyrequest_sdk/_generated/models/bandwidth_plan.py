from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID


T = TypeVar("T", bound="BandwidthPlan")


@_attrs_define
class BandwidthPlan:
    id: UUID
    speed_mbps: int
    duration_days: int
    price_minor: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        speed_mbps = self.speed_mbps

        duration_days = self.duration_days

        price_minor = self.price_minor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "speed_mbps": speed_mbps,
                "duration_days": duration_days,
                "price_minor": price_minor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        speed_mbps = d.pop("speed_mbps")

        duration_days = d.pop("duration_days")

        price_minor = d.pop("price_minor")

        bandwidth_plan = cls(
            id=id,
            speed_mbps=speed_mbps,
            duration_days=duration_days,
            price_minor=price_minor,
        )

        bandwidth_plan.additional_properties = d
        return bandwidth_plan

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
