from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="APIKeyList")


@_attrs_define
class APIKeyList:
    title: str
    """ Descriptive label that identifies the purpose or owner of this API key. Mobile App Dashboard Integration CI
    Pipeline """
    prefix: str
    allowed_ips: list[str]
    created: datetime.datetime
    updated: datetime.datetime
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    """ The API key value used for authentication. Leave blank to have it generated automatically on save. Store
    this value securely. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        prefix = self.prefix

        allowed_ips = self.allowed_ips

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id = self.id

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "prefix": prefix,
                "allowed_ips": allowed_ips,
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        prefix = d.pop("prefix")

        allowed_ips = cast(list[str], d.pop("allowed_ips"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        updated = datetime.datetime.fromisoformat(d.pop("updated"))

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        api_key_list = cls(
            title=title,
            prefix=prefix,
            allowed_ips=allowed_ips,
            created=created,
            updated=updated,
            id=id,
            key=key,
        )

        api_key_list.additional_properties = d
        return api_key_list

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
