from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.location_asn_geo_item import LocationASNGeoItem


T = TypeVar("T", bound="LocationASNRecord")


@_attrs_define
class LocationASNRecord:
    code: str
    name: str
    geo: list[LocationASNGeoItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_asn_geo_item import LocationASNGeoItem

        code = self.code

        name = self.name

        geo: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geo, Unset):
            geo = []
            for geo_item_data in self.geo:
                geo_item = geo_item_data.to_dict()
                geo.append(geo_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )
        if geo is not UNSET:
            field_dict["geo"] = geo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_asn_geo_item import LocationASNGeoItem

        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        _geo = d.pop("geo", UNSET)
        geo: list[LocationASNGeoItem] | Unset = UNSET
        if _geo is not UNSET:
            geo = []
            for geo_item_data in _geo:
                geo_item = LocationASNGeoItem.from_dict(geo_item_data)

                geo.append(geo_item)

        location_asn_record = cls(
            code=code,
            name=name,
            geo=geo,
        )

        location_asn_record.additional_properties = d
        return location_asn_record

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
