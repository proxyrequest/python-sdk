from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.duration_kind_enum import DurationKindEnum
from uuid import UUID


T = TypeVar("T", bound="RentalDetailTerm")


@_attrs_define
class RentalDetailTerm:
    id: UUID
    name: str
    duration_kind: DurationKindEnum
    """ * `hours` - hours * `calendar_months` - calendar_months """
    duration_value: int
    renewal_price_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        duration_kind = self.duration_kind.value

        duration_value = self.duration_value

        renewal_price_cents = self.renewal_price_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "duration_kind": duration_kind,
                "duration_value": duration_value,
                "renewal_price_cents": renewal_price_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        duration_kind = DurationKindEnum(d.pop("duration_kind"))

        duration_value = d.pop("duration_value")

        renewal_price_cents = d.pop("renewal_price_cents")

        rental_detail_term = cls(
            id=id,
            name=name,
            duration_kind=duration_kind,
            duration_value=duration_value,
            renewal_price_cents=renewal_price_cents,
        )

        rental_detail_term.additional_properties = d
        return rental_detail_term

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
