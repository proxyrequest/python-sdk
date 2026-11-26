from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.cart_line_request import CartLineRequest
    from ..models.location_selection_request import LocationSelectionRequest


T = TypeVar("T", bound="IntentRequest")


@_attrs_define
class IntentRequest:
    offer_id: UUID | Unset = UNSET
    term_id: UUID | Unset = UNSET
    quantity: int | Unset = UNSET
    location: LocationSelectionRequest | Unset = UNSET
    items: list[CartLineRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cart_line_request import CartLineRequest
        from ..models.location_selection_request import LocationSelectionRequest

        offer_id: str | Unset = UNSET
        if not isinstance(self.offer_id, Unset):
            offer_id = str(self.offer_id)

        term_id: str | Unset = UNSET
        if not isinstance(self.term_id, Unset):
            term_id = str(self.term_id)

        quantity = self.quantity

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offer_id is not UNSET:
            field_dict["offer_id"] = offer_id
        if term_id is not UNSET:
            field_dict["term_id"] = term_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if location is not UNSET:
            field_dict["location"] = location
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cart_line_request import CartLineRequest
        from ..models.location_selection_request import LocationSelectionRequest

        d = dict(src_dict)
        _offer_id = d.pop("offer_id", UNSET)
        offer_id: UUID | Unset
        if isinstance(_offer_id, Unset):
            offer_id = UNSET
        else:
            offer_id = UUID(_offer_id)

        _term_id = d.pop("term_id", UNSET)
        term_id: UUID | Unset
        if isinstance(_term_id, Unset):
            term_id = UNSET
        else:
            term_id = UUID(_term_id)

        quantity = d.pop("quantity", UNSET)

        _location = d.pop("location", UNSET)
        location: LocationSelectionRequest | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationSelectionRequest.from_dict(_location)

        _items = d.pop("items", UNSET)
        items: list[CartLineRequest] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CartLineRequest.from_dict(items_item_data)

                items.append(items_item)

        intent_request = cls(
            offer_id=offer_id,
            term_id=term_id,
            quantity=quantity,
            location=location,
            items=items,
        )

        intent_request.additional_properties = d
        return intent_request

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
