from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="PatchedEndpointUpdateRequest")


@_attrs_define
class PatchedEndpointUpdateRequest:
    label: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    allowed_ips: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        is_active = self.is_active

        allowed_ips: list[str] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = self.allowed_ips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        is_active = d.pop("is_active", UNSET)

        allowed_ips = cast(list[str], d.pop("allowed_ips", UNSET))

        patched_endpoint_update_request = cls(
            label=label,
            is_active=is_active,
            allowed_ips=allowed_ips,
        )

        patched_endpoint_update_request.additional_properties = d
        return patched_endpoint_update_request

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
