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
    from ..models.location_country_summary import LocationCountrySummary
    from ..models.location_region_summary import LocationRegionSummary


T = TypeVar("T", bound="City")


@_attrs_define
class City:
    code: str
    """ Raw city code as it appears in the source data. los_angeles paris """
    name: str
    """ English display name of the city used across the admin and API responses. """
    country: LocationCountrySummary
    region: LocationRegionSummary
    isps: list[LocationCodeName]
    asns: list[LocationCodeName]
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_code_name import LocationCodeName
        from ..models.location_country_summary import LocationCountrySummary
        from ..models.location_region_summary import LocationRegionSummary

        code = self.code

        name = self.name

        country = self.country.to_dict()

        region = self.region.to_dict()

        isps = []
        for isps_item_data in self.isps:
            isps_item = isps_item_data.to_dict()
            isps.append(isps_item)

        asns = []
        for asns_item_data in self.asns:
            asns_item = asns_item_data.to_dict()
            asns.append(asns_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
                "country": country,
                "region": region,
                "isps": isps,
                "asns": asns,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_code_name import LocationCodeName
        from ..models.location_country_summary import LocationCountrySummary
        from ..models.location_region_summary import LocationRegionSummary

        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        country = LocationCountrySummary.from_dict(d.pop("country"))

        region = LocationRegionSummary.from_dict(d.pop("region"))

        isps = []
        _isps = d.pop("isps")
        for isps_item_data in _isps:
            isps_item = LocationCodeName.from_dict(isps_item_data)

            isps.append(isps_item)

        asns = []
        _asns = d.pop("asns")
        for asns_item_data in _asns:
            asns_item = LocationCodeName.from_dict(asns_item_data)

            asns.append(asns_item)

        id = d.pop("id", UNSET)

        city = cls(
            code=code,
            name=name,
            country=country,
            region=region,
            isps=isps,
            asns=asns,
            id=id,
        )

        city.additional_properties = d
        return city

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
