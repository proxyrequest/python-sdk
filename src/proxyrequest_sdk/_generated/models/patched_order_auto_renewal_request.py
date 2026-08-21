from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchedOrderAutoRenewalRequest")


@_attrs_define
class PatchedOrderAutoRenewalRequest:
    auto_renewal_percentage: int | Unset = UNSET
    auto_renewal_data: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_renewal_percentage = self.auto_renewal_percentage

        auto_renewal_data = self.auto_renewal_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_renewal_percentage is not UNSET:
            field_dict["auto_renewal_percentage"] = auto_renewal_percentage
        if auto_renewal_data is not UNSET:
            field_dict["auto_renewal_data"] = auto_renewal_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_renewal_percentage = d.pop("auto_renewal_percentage", UNSET)

        auto_renewal_data = d.pop("auto_renewal_data", UNSET)

        patched_order_auto_renewal_request = cls(
            auto_renewal_percentage=auto_renewal_percentage,
            auto_renewal_data=auto_renewal_data,
        )

        patched_order_auto_renewal_request.additional_properties = d
        return patched_order_auto_renewal_request

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
