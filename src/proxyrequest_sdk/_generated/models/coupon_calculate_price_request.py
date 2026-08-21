from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID


T = TypeVar("T", bound="CouponCalculatePriceRequest")


@_attrs_define
class CouponCalculatePriceRequest:
    coupon_code: str
    data: int
    package_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coupon_code = self.coupon_code

        data = self.data

        package_id: str | Unset = UNSET
        if not isinstance(self.package_id, Unset):
            package_id = str(self.package_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coupon_code": coupon_code,
                "data": data,
            }
        )
        if package_id is not UNSET:
            field_dict["package_id"] = package_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        coupon_code = d.pop("coupon_code")

        data = d.pop("data")

        _package_id = d.pop("package_id", UNSET)
        package_id: UUID | Unset
        if isinstance(_package_id, Unset):
            package_id = UNSET
        else:
            package_id = UUID(_package_id)

        coupon_calculate_price_request = cls(
            coupon_code=coupon_code,
            data=data,
            package_id=package_id,
        )

        coupon_calculate_price_request.additional_properties = d
        return coupon_calculate_price_request

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
