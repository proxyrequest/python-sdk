from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.postal_place import PostalPlace


T = TypeVar("T", bound="Postal")


@_attrs_define
class Postal:
    code: str
    country: PostalPlace
    regions: list[PostalPlace]
    cities: list[PostalPlace]
    count: int
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.postal_place import PostalPlace

        code = self.code

        country = self.country.to_dict()

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        cities = []
        for cities_item_data in self.cities:
            cities_item = cities_item_data.to_dict()
            cities.append(cities_item)

        count = self.count

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "country": country,
                "regions": regions,
                "cities": cities,
                "count": count,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.postal_place import PostalPlace

        d = dict(src_dict)
        code = d.pop("code")

        country = PostalPlace.from_dict(d.pop("country"))

        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = PostalPlace.from_dict(regions_item_data)

            regions.append(regions_item)

        cities = []
        _cities = d.pop("cities")
        for cities_item_data in _cities:
            cities_item = PostalPlace.from_dict(cities_item_data)

            cities.append(cities_item)

        count = d.pop("count")

        id = d.pop("id", UNSET)

        postal = cls(
            code=code,
            country=country,
            regions=regions,
            cities=cities,
            count=count,
            id=id,
        )

        postal.additional_properties = d
        return postal

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
