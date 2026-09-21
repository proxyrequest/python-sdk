from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CouponStats")


@_attrs_define
class CouponStats:
    total_redeems: int
    unique_users: int
    total_revenue: int
    total_discount_given: int
    total_data_given: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_redeems = self.total_redeems

        unique_users = self.unique_users

        total_revenue = self.total_revenue

        total_discount_given = self.total_discount_given

        total_data_given = self.total_data_given

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_redeems": total_redeems,
                "unique_users": unique_users,
                "total_revenue": total_revenue,
                "total_discount_given": total_discount_given,
                "total_data_given": total_data_given,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_redeems = d.pop("total_redeems")

        unique_users = d.pop("unique_users")

        total_revenue = d.pop("total_revenue")

        total_discount_given = d.pop("total_discount_given")

        total_data_given = d.pop("total_data_given")

        coupon_stats = cls(
            total_redeems=total_redeems,
            unique_users=unique_users,
            total_revenue=total_revenue,
            total_discount_given=total_discount_given,
            total_data_given=total_data_given,
        )

        coupon_stats.additional_properties = d
        return coupon_stats

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
