from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mode_enum import ModeEnum
from typing import cast
from uuid import UUID


T = TypeVar("T", bound="RentalDetailGroup")


@_attrs_define
class RentalDetailGroup:
    id: UUID
    quantity: int
    mode: ModeEnum
    """ * `grouped` - grouped * `individual` - individual """
    endpoint_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        quantity = self.quantity

        mode = self.mode.value

        endpoint_ids = []
        for endpoint_ids_item_data in self.endpoint_ids:
            endpoint_ids_item = str(endpoint_ids_item_data)
            endpoint_ids.append(endpoint_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quantity": quantity,
                "mode": mode,
                "endpoint_ids": endpoint_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        quantity = d.pop("quantity")

        mode = ModeEnum(d.pop("mode"))

        endpoint_ids = []
        _endpoint_ids = d.pop("endpoint_ids")
        for endpoint_ids_item_data in _endpoint_ids:
            endpoint_ids_item = UUID(endpoint_ids_item_data)

            endpoint_ids.append(endpoint_ids_item)

        rental_detail_group = cls(
            id=id,
            quantity=quantity,
            mode=mode,
            endpoint_ids=endpoint_ids,
        )

        rental_detail_group.additional_properties = d
        return rental_detail_group

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
