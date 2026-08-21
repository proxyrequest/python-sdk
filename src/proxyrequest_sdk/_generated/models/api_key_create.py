from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="APIKeyCreate")


@_attrs_define
class APIKeyCreate:
    title: str
    key: str
    created: datetime.datetime
    id: str | Unset = UNSET
    allowed_ips: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        key = self.key

        created = self.created.isoformat()

        id = self.id

        allowed_ips: list[str] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = self.allowed_ips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "key": key,
                "created": created,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        key = d.pop("key")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = d.pop("id", UNSET)

        allowed_ips = cast(list[str], d.pop("allowed_ips", UNSET))

        api_key_create = cls(
            title=title,
            key=key,
            created=created,
            id=id,
            allowed_ips=allowed_ips,
        )

        api_key_create.additional_properties = d
        return api_key_create

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
