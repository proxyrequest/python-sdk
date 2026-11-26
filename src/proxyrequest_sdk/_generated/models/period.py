from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="Period")


@_attrs_define
class Period:
    starts_at: datetime.datetime
    ends_at: datetime.datetime
    duration_kind: str
    duration_value: int
    price_cents: int
    invoice_id: str
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        duration_kind = self.duration_kind

        duration_value = self.duration_value

        price_cents = self.price_cents

        invoice_id = self.invoice_id

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "starts_at": starts_at,
                "ends_at": ends_at,
                "duration_kind": duration_kind,
                "duration_value": duration_value,
                "price_cents": price_cents,
                "invoice_id": invoice_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starts_at = datetime.datetime.fromisoformat(d.pop("starts_at"))

        ends_at = datetime.datetime.fromisoformat(d.pop("ends_at"))

        duration_kind = d.pop("duration_kind")

        duration_value = d.pop("duration_value")

        price_cents = d.pop("price_cents")

        invoice_id = d.pop("invoice_id")

        id = d.pop("id", UNSET)

        period = cls(
            starts_at=starts_at,
            ends_at=ends_at,
            duration_kind=duration_kind,
            duration_value=duration_value,
            price_cents=price_cents,
            invoice_id=invoice_id,
            id=id,
        )

        period.additional_properties = d
        return period

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
