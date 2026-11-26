from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.allocation_mode_enum import AllocationModeEnum
from ..models.duration_kind_enum import DurationKindEnum
from ..models.network_class_enum import NetworkClassEnum
from typing import cast
from uuid import UUID


T = TypeVar("T", bound="CatalogOffer")


@_attrs_define
class CatalogOffer:
    id: UUID
    package_id: UUID
    name: str
    term_id: UUID
    term_name: str
    country_code: str
    duration_kind: DurationKindEnum
    """ * `hours` - hours * `calendar_months` - calendar_months """
    duration_value: int
    allocation_mode: AllocationModeEnum
    """ * `dedicated` - dedicated * `shared` - shared """
    network_class: NetworkClassEnum
    """ * `isp` - isp * `dc` - dc """
    quantity: int
    price_cents: int
    renewal_price_cents: int
    max_bandwidth_mbps: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        package_id = str(self.package_id)

        name = self.name

        term_id = str(self.term_id)

        term_name = self.term_name

        country_code = self.country_code

        duration_kind = self.duration_kind.value

        duration_value = self.duration_value

        allocation_mode = self.allocation_mode.value

        network_class = self.network_class.value

        quantity = self.quantity

        price_cents = self.price_cents

        renewal_price_cents = self.renewal_price_cents

        max_bandwidth_mbps: int | None
        max_bandwidth_mbps = self.max_bandwidth_mbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "package_id": package_id,
                "name": name,
                "term_id": term_id,
                "term_name": term_name,
                "country_code": country_code,
                "duration_kind": duration_kind,
                "duration_value": duration_value,
                "allocation_mode": allocation_mode,
                "network_class": network_class,
                "quantity": quantity,
                "price_cents": price_cents,
                "renewal_price_cents": renewal_price_cents,
                "max_bandwidth_mbps": max_bandwidth_mbps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        package_id = UUID(d.pop("package_id"))

        name = d.pop("name")

        term_id = UUID(d.pop("term_id"))

        term_name = d.pop("term_name")

        country_code = d.pop("country_code")

        duration_kind = DurationKindEnum(d.pop("duration_kind"))

        duration_value = d.pop("duration_value")

        allocation_mode = AllocationModeEnum(d.pop("allocation_mode"))

        network_class = NetworkClassEnum(d.pop("network_class"))

        quantity = d.pop("quantity")

        price_cents = d.pop("price_cents")

        renewal_price_cents = d.pop("renewal_price_cents")

        def _parse_max_bandwidth_mbps(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_bandwidth_mbps = _parse_max_bandwidth_mbps(d.pop("max_bandwidth_mbps"))

        catalog_offer = cls(
            id=id,
            package_id=package_id,
            name=name,
            term_id=term_id,
            term_name=term_name,
            country_code=country_code,
            duration_kind=duration_kind,
            duration_value=duration_value,
            allocation_mode=allocation_mode,
            network_class=network_class,
            quantity=quantity,
            price_cents=price_cents,
            renewal_price_cents=renewal_price_cents,
            max_bandwidth_mbps=max_bandwidth_mbps,
        )

        catalog_offer.additional_properties = d
        return catalog_offer

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
