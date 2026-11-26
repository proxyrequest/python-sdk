from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.last_error_enum import LastErrorEnum
from typing import cast
from uuid import UUID
import datetime


T = TypeVar("T", bound="AutoRenewalStatus")


@_attrs_define
class AutoRenewalStatus:
    enabled: bool
    term_id: None | UUID
    last_attempt_at: datetime.datetime | None
    last_error: LastErrorEnum | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        term_id: None | str
        if isinstance(self.term_id, UUID):
            term_id = str(self.term_id)
        else:
            term_id = self.term_id

        last_attempt_at: None | str
        if isinstance(self.last_attempt_at, datetime.datetime):
            last_attempt_at = self.last_attempt_at.isoformat()
        else:
            last_attempt_at = self.last_attempt_at

        last_error: None | str
        if isinstance(self.last_error, LastErrorEnum):
            last_error = self.last_error.value
        else:
            last_error = self.last_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "term_id": term_id,
                "last_attempt_at": last_attempt_at,
                "last_error": last_error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_term_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                term_id_type_0 = UUID(data)

                return term_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        term_id = _parse_term_id(d.pop("term_id"))

        def _parse_last_attempt_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_attempt_at = _parse_last_attempt_at(d.pop("last_attempt_at"))

        def _parse_last_error(data: object) -> LastErrorEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_error_type_0 = LastErrorEnum(data)

                return last_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LastErrorEnum | None, data)

        last_error = _parse_last_error(d.pop("last_error"))

        auto_renewal_status = cls(
            enabled=enabled,
            term_id=term_id,
            last_attempt_at=last_attempt_at,
            last_error=last_error,
        )

        auto_renewal_status.additional_properties = d
        return auto_renewal_status

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
