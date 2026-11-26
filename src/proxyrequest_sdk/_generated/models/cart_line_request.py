from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.location_selection_request import LocationSelectionRequest


T = TypeVar("T", bound="CartLineRequest")


@_attrs_define
class CartLineRequest:
    quantity: int
    location: LocationSelectionRequest
    operator: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_selection_request import LocationSelectionRequest

        quantity = self.quantity

        location = self.location.to_dict()

        operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "location": location,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_selection_request import LocationSelectionRequest

        d = dict(src_dict)
        quantity = d.pop("quantity")

        location = LocationSelectionRequest.from_dict(d.pop("location"))

        operator = d.pop("operator", UNSET)

        cart_line_request = cls(
            quantity=quantity,
            location=location,
            operator=operator,
        )

        cart_line_request.additional_properties = d
        return cart_line_request

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
