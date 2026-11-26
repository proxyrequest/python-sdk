from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.scopes_enum import ScopesEnum
from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="IntegrationKeyCreated")


@_attrs_define
class IntegrationKeyCreated:
    title: str
    """ Descriptive label that identifies the purpose or owner of this API key. Mobile App Dashboard Integration CI
    Pipeline """
    scopes: list[ScopesEnum]
    allowed_ips: list[str]
    created: datetime.datetime
    key: str
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        allowed_ips = self.allowed_ips

        created = self.created.isoformat()

        key = self.key

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "scopes": scopes,
                "allowed_ips": allowed_ips,
                "created": created,
                "key": key,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

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

        allowed_ips = cast(list[str], d.pop("allowed_ips"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        key = d.pop("key")

        id = d.pop("id", UNSET)

        integration_key_created = cls(
            title=title,
            scopes=scopes,
            allowed_ips=allowed_ips,
            created=created,
            key=key,
            id=id,
        )

        integration_key_created.additional_properties = d
        return integration_key_created

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
