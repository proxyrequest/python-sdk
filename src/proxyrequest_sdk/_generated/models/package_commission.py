from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID


T = TypeVar("T", bound="PackageCommission")


@_attrs_define
class PackageCommission:
    id: UUID
    name: str
    pricing: Any
    commission_rate: float
    total_earnings: float
    total_orders: int
    pending: float
    billing_model: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        pricing = self.pricing

        commission_rate = self.commission_rate

        total_earnings = self.total_earnings

        total_orders = self.total_orders

        pending = self.pending

        billing_model = self.billing_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "pricing": pricing,
                "commission_rate": commission_rate,
                "total_earnings": total_earnings,
                "total_orders": total_orders,
                "pending": pending,
                "billing_model": billing_model,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        pricing = d.pop("pricing")

        commission_rate = d.pop("commission_rate")

        total_earnings = d.pop("total_earnings")

        total_orders = d.pop("total_orders")

        pending = d.pop("pending")

        billing_model = d.pop("billing_model")

        package_commission = cls(
            id=id,
            name=name,
            pricing=pricing,
            commission_rate=commission_rate,
            total_earnings=total_earnings,
            total_orders=total_orders,
            pending=pending,
            billing_model=billing_model,
        )

        package_commission.additional_properties = d
        return package_commission

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
