from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.duration_kind_enum import DurationKindEnum
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.rental_term_option_price_tiers_item import RentalTermOptionPriceTiersItem


T = TypeVar("T", bound="RentalTermOption")


@_attrs_define
class RentalTermOption:
    id: UUID
    package_id: UUID
    name: str
    term_name: str
    duration_kind: DurationKindEnum
    """ * `hours` - hours * `calendar_months` - calendar_months """
    duration_value: int
    network_class: str
    allocation_mode: str
    available: int
    price_tiers: list[RentalTermOptionPriceTiersItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rental_term_option_price_tiers_item import RentalTermOptionPriceTiersItem

        id = str(self.id)

        package_id = str(self.package_id)

        name = self.name

        term_name = self.term_name

        duration_kind = self.duration_kind.value

        duration_value = self.duration_value

        network_class = self.network_class

        allocation_mode = self.allocation_mode

        available = self.available

        price_tiers = []
        for price_tiers_item_data in self.price_tiers:
            price_tiers_item = price_tiers_item_data.to_dict()
            price_tiers.append(price_tiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "package_id": package_id,
                "name": name,
                "term_name": term_name,
                "duration_kind": duration_kind,
                "duration_value": duration_value,
                "network_class": network_class,
                "allocation_mode": allocation_mode,
                "available": available,
                "price_tiers": price_tiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rental_term_option_price_tiers_item import RentalTermOptionPriceTiersItem

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        package_id = UUID(d.pop("package_id"))

        name = d.pop("name")

        term_name = d.pop("term_name")

        duration_kind = DurationKindEnum(d.pop("duration_kind"))

        duration_value = d.pop("duration_value")

        network_class = d.pop("network_class")

        allocation_mode = d.pop("allocation_mode")

        available = d.pop("available")

        price_tiers = []
        _price_tiers = d.pop("price_tiers")
        for price_tiers_item_data in _price_tiers:
            price_tiers_item = RentalTermOptionPriceTiersItem.from_dict(price_tiers_item_data)

            price_tiers.append(price_tiers_item)

        rental_term_option = cls(
            id=id,
            package_id=package_id,
            name=name,
            term_name=term_name,
            duration_kind=duration_kind,
            duration_value=duration_value,
            network_class=network_class,
            allocation_mode=allocation_mode,
            available=available,
            price_tiers=price_tiers,
        )

        rental_term_option.additional_properties = d
        return rental_term_option

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
