from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID


T = TypeVar("T", bound="LocationSelection")


@_attrs_define
class LocationSelection:
    country_code: str
    operator: str | Unset = UNSET
    region_id: None | Unset | UUID = UNSET
    city_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        operator = self.operator

        region_id: None | str | Unset
        if isinstance(self.region_id, Unset):
            region_id = UNSET
        elif isinstance(self.region_id, UUID):
            region_id = str(self.region_id)
        else:
            region_id = self.region_id

        city_id: None | str | Unset
        if isinstance(self.city_id, Unset):
            city_id = UNSET
        elif isinstance(self.city_id, UUID):
            city_id = str(self.city_id)
        else:
            city_id = self.city_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country_code": country_code,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator
        if region_id is not UNSET:
            field_dict["region_id"] = region_id
        if city_id is not UNSET:
            field_dict["city_id"] = city_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("country_code")

        operator = d.pop("operator", UNSET)

        def _parse_region_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                region_id_type_0 = UUID(data)

                return region_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        region_id = _parse_region_id(d.pop("region_id", UNSET))

        def _parse_city_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                city_id_type_0 = UUID(data)

                return city_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        city_id = _parse_city_id(d.pop("city_id", UNSET))

        location_selection = cls(
            country_code=country_code,
            operator=operator,
            region_id=region_id,
            city_id=city_id,
        )

        location_selection.additional_properties = d
        return location_selection

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
