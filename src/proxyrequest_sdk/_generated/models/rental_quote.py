from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.duration_kind_enum import DurationKindEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.cart_line import CartLine
    from ..models.location_selection import LocationSelection


T = TypeVar("T", bound="RentalQuote")


@_attrs_define
class RentalQuote:
    version: int
    term_id: UUID
    duration_kind: DurationKindEnum
    """ * `hours` - hours * `calendar_months` - calendar_months """
    duration_value: int
    quantity: int
    price_cents: int
    currency: str
    country_code: str
    allocation_mode: str
    network_class: str
    hold_hours: int
    commission_rate: str
    commission_type: str
    location: LocationSelection | Unset = UNSET
    tier_id: UUID | Unset = UNSET
    min_quantity: int | Unset = UNSET
    unit_price_cents: int | Unset = UNSET
    items: list[CartLine] | Unset = UNSET
    offer_id: UUID | Unset = UNSET
    endpoint_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cart_line import CartLine
        from ..models.location_selection import LocationSelection

        version = self.version

        term_id = str(self.term_id)

        duration_kind = self.duration_kind.value

        duration_value = self.duration_value

        quantity = self.quantity

        price_cents = self.price_cents

        currency = self.currency

        country_code = self.country_code

        allocation_mode = self.allocation_mode

        network_class = self.network_class

        hold_hours = self.hold_hours

        commission_rate = self.commission_rate

        commission_type = self.commission_type

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        tier_id: str | Unset = UNSET
        if not isinstance(self.tier_id, Unset):
            tier_id = str(self.tier_id)

        min_quantity = self.min_quantity

        unit_price_cents = self.unit_price_cents

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        offer_id: str | Unset = UNSET
        if not isinstance(self.offer_id, Unset):
            offer_id = str(self.offer_id)

        endpoint_ids: list[str] | Unset = UNSET
        if not isinstance(self.endpoint_ids, Unset):
            endpoint_ids = []
            for endpoint_ids_item_data in self.endpoint_ids:
                endpoint_ids_item = str(endpoint_ids_item_data)
                endpoint_ids.append(endpoint_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "term_id": term_id,
                "duration_kind": duration_kind,
                "duration_value": duration_value,
                "quantity": quantity,
                "price_cents": price_cents,
                "currency": currency,
                "country_code": country_code,
                "allocation_mode": allocation_mode,
                "network_class": network_class,
                "hold_hours": hold_hours,
                "commission_rate": commission_rate,
                "commission_type": commission_type,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if tier_id is not UNSET:
            field_dict["tier_id"] = tier_id
        if min_quantity is not UNSET:
            field_dict["min_quantity"] = min_quantity
        if unit_price_cents is not UNSET:
            field_dict["unit_price_cents"] = unit_price_cents
        if items is not UNSET:
            field_dict["items"] = items
        if offer_id is not UNSET:
            field_dict["offer_id"] = offer_id
        if endpoint_ids is not UNSET:
            field_dict["endpoint_ids"] = endpoint_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cart_line import CartLine
        from ..models.location_selection import LocationSelection

        d = dict(src_dict)
        version = d.pop("version")

        term_id = UUID(d.pop("term_id"))

        duration_kind = DurationKindEnum(d.pop("duration_kind"))

        duration_value = d.pop("duration_value")

        quantity = d.pop("quantity")

        price_cents = d.pop("price_cents")

        currency = d.pop("currency")

        country_code = d.pop("country_code")

        allocation_mode = d.pop("allocation_mode")

        network_class = d.pop("network_class")

        hold_hours = d.pop("hold_hours")

        commission_rate = d.pop("commission_rate")

        commission_type = d.pop("commission_type")

        _location = d.pop("location", UNSET)
        location: LocationSelection | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationSelection.from_dict(_location)

        _tier_id = d.pop("tier_id", UNSET)
        tier_id: UUID | Unset
        if isinstance(_tier_id, Unset):
            tier_id = UNSET
        else:
            tier_id = UUID(_tier_id)

        min_quantity = d.pop("min_quantity", UNSET)

        unit_price_cents = d.pop("unit_price_cents", UNSET)

        _items = d.pop("items", UNSET)
        items: list[CartLine] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CartLine.from_dict(items_item_data)

                items.append(items_item)

        _offer_id = d.pop("offer_id", UNSET)
        offer_id: UUID | Unset
        if isinstance(_offer_id, Unset):
            offer_id = UNSET
        else:
            offer_id = UUID(_offer_id)

        _endpoint_ids = d.pop("endpoint_ids", UNSET)
        endpoint_ids: list[UUID] | Unset = UNSET
        if _endpoint_ids is not UNSET:
            endpoint_ids = []
            for endpoint_ids_item_data in _endpoint_ids:
                endpoint_ids_item = UUID(endpoint_ids_item_data)

                endpoint_ids.append(endpoint_ids_item)

        rental_quote = cls(
            version=version,
            term_id=term_id,
            duration_kind=duration_kind,
            duration_value=duration_value,
            quantity=quantity,
            price_cents=price_cents,
            currency=currency,
            country_code=country_code,
            allocation_mode=allocation_mode,
            network_class=network_class,
            hold_hours=hold_hours,
            commission_rate=commission_rate,
            commission_type=commission_type,
            location=location,
            tier_id=tier_id,
            min_quantity=min_quantity,
            unit_price_cents=unit_price_cents,
            items=items,
            offer_id=offer_id,
            endpoint_ids=endpoint_ids,
        )

        rental_quote.additional_properties = d
        return rental_quote

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
