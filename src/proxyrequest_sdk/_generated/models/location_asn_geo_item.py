from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.location_code_name import LocationCodeName


T = TypeVar("T", bound="LocationASNGeoItem")


@_attrs_define
class LocationASNGeoItem:
    country: LocationCodeName
    region: LocationCodeName | Unset = UNSET
    city: LocationCodeName | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_code_name import LocationCodeName

        country = self.country.to_dict()

        region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        city: dict[str, Any] | Unset = UNSET
        if not isinstance(self.city, Unset):
            city = self.city.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_code_name import LocationCodeName

        d = dict(src_dict)
        country = LocationCodeName.from_dict(d.pop("country"))

        _region = d.pop("region", UNSET)
        region: LocationCodeName | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = LocationCodeName.from_dict(_region)

        _city = d.pop("city", UNSET)
        city: LocationCodeName | Unset
        if isinstance(_city, Unset):
            city = UNSET
        else:
            city = LocationCodeName.from_dict(_city)

        location_asn_geo_item = cls(
            country=country,
            region=region,
            city=city,
        )

        location_asn_geo_item.additional_properties = d
        return location_asn_geo_item

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
