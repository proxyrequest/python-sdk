from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID
import datetime


T = TypeVar("T", bound="ProviderBalanceCheckpoint")


@_attrs_define
class ProviderBalanceCheckpoint:
    id: UUID
    available_bytes: str
    """ Observed balance in bytes, as a decimal string. """
    observed_at: datetime.datetime
    created: datetime.datetime
    created_by: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        available_bytes = self.available_bytes

        observed_at = self.observed_at.isoformat()

        created = self.created.isoformat()

        created_by: None | str
        created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "available_bytes": available_bytes,
                "observed_at": observed_at,
                "created": created,
                "created_by": created_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        available_bytes = d.pop("available_bytes")

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_created_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by = _parse_created_by(d.pop("created_by"))

        provider_balance_checkpoint = cls(
            id=id,
            available_bytes=available_bytes,
            observed_at=observed_at,
            created=created,
            created_by=created_by,
        )

        provider_balance_checkpoint.additional_properties = d
        return provider_balance_checkpoint

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
