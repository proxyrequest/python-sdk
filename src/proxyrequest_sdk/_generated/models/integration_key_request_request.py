from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.scopes_enum import ScopesEnum
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="IntegrationKeyRequestRequest")


@_attrs_define
class IntegrationKeyRequestRequest:
    title: str
    scopes: list[ScopesEnum]
    allowed_ips: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        allowed_ips: list[str] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = self.allowed_ips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "scopes": scopes,
            }
        )
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = ScopesEnum(scopes_item_data)

            scopes.append(scopes_item)

        allowed_ips = cast(list[str], d.pop("allowed_ips", UNSET))

        integration_key_request_request = cls(
            title=title,
            scopes=scopes,
            allowed_ips=allowed_ips,
        )

        integration_key_request_request.additional_properties = d
        return integration_key_request_request

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
