from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.location_option import LocationOption
    from ..models.rental_term_option import RentalTermOption


T = TypeVar("T", bound="AvailabilityResponse")


@_attrs_define
class AvailabilityResponse:
    currency: str
    available: int
    terms: list[RentalTermOption]
    countries: list[LocationOption]
    regions: list[LocationOption]
    cities: list[LocationOption]
    operators: list[LocationOption]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_option import LocationOption
        from ..models.rental_term_option import RentalTermOption

        currency = self.currency

        available = self.available

        terms = []
        for terms_item_data in self.terms:
            terms_item = terms_item_data.to_dict()
            terms.append(terms_item)

        countries = []
        for countries_item_data in self.countries:
            countries_item = countries_item_data.to_dict()
            countries.append(countries_item)

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        cities = []
        for cities_item_data in self.cities:
            cities_item = cities_item_data.to_dict()
            cities.append(cities_item)

        operators = []
        for operators_item_data in self.operators:
            operators_item = operators_item_data.to_dict()
            operators.append(operators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "available": available,
                "terms": terms,
                "countries": countries,
                "regions": regions,
                "cities": cities,
                "operators": operators,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_option import LocationOption
        from ..models.rental_term_option import RentalTermOption

        d = dict(src_dict)
        currency = d.pop("currency")

        available = d.pop("available")

        terms = []
        _terms = d.pop("terms")
        for terms_item_data in _terms:
            terms_item = RentalTermOption.from_dict(terms_item_data)

            terms.append(terms_item)

        countries = []
        _countries = d.pop("countries")
        for countries_item_data in _countries:
            countries_item = LocationOption.from_dict(countries_item_data)

            countries.append(countries_item)

        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = LocationOption.from_dict(regions_item_data)

            regions.append(regions_item)

        cities = []
        _cities = d.pop("cities")
        for cities_item_data in _cities:
            cities_item = LocationOption.from_dict(cities_item_data)

            cities.append(cities_item)

        operators = []
        _operators = d.pop("operators")
        for operators_item_data in _operators:
            operators_item = LocationOption.from_dict(operators_item_data)

            operators.append(operators_item)

        availability_response = cls(
            currency=currency,
            available=available,
            terms=terms,
            countries=countries,
            regions=regions,
            cities=cities,
            operators=operators,
        )

        availability_response.additional_properties = d
        return availability_response

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
