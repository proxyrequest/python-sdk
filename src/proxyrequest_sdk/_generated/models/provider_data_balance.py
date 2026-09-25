from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.freshness_enum import FreshnessEnum
from ..models.severity_enum import SeverityEnum
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.provider_balance_checkpoint import ProviderBalanceCheckpoint


T = TypeVar("T", bound="ProviderDataBalance")


@_attrs_define
class ProviderDataBalance:
    checkpoint_id: UUID
    provider_id: str
    provider_name: str
    observed_at: datetime.datetime
    """ Time the available balance was observed. """
    available_bytes: str
    """ Observed balance in bytes, as a decimal string. """
    used_bytes: None | str
    """ Calculated usage since the observation, in bytes. """
    remaining_bytes: None | str
    """ Remaining bytes at calculated_at, as a decimal string. """
    remaining_percent: float | None
    severity: None | SeverityEnum
    freshness: FreshnessEnum
    """ * `fresh` - fresh * `stale` - stale * `unavailable` - unavailable """
    error: str
    calculated_at: datetime.datetime | None
    """ Time of the last successful calculation. """
    history: list[ProviderBalanceCheckpoint]
    """ Latest entries by creation time, limited by PROVIDER_DATA_BALANCE_HISTORY_LIMIT (default 10). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_balance_checkpoint import ProviderBalanceCheckpoint

        checkpoint_id = str(self.checkpoint_id)

        provider_id = self.provider_id

        provider_name = self.provider_name

        observed_at = self.observed_at.isoformat()

        available_bytes = self.available_bytes

        used_bytes: None | str
        used_bytes = self.used_bytes

        remaining_bytes: None | str
        remaining_bytes = self.remaining_bytes

        remaining_percent: float | None
        remaining_percent = self.remaining_percent

        severity: None | str
        if isinstance(self.severity, SeverityEnum):
            severity = self.severity.value
        else:
            severity = self.severity

        freshness = self.freshness.value

        error = self.error

        calculated_at: None | str
        if isinstance(self.calculated_at, datetime.datetime):
            calculated_at = self.calculated_at.isoformat()
        else:
            calculated_at = self.calculated_at

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkpoint_id": checkpoint_id,
                "provider_id": provider_id,
                "provider_name": provider_name,
                "observed_at": observed_at,
                "available_bytes": available_bytes,
                "used_bytes": used_bytes,
                "remaining_bytes": remaining_bytes,
                "remaining_percent": remaining_percent,
                "severity": severity,
                "freshness": freshness,
                "error": error,
                "calculated_at": calculated_at,
                "history": history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_balance_checkpoint import ProviderBalanceCheckpoint

        d = dict(src_dict)
        checkpoint_id = UUID(d.pop("checkpoint_id"))

        provider_id = d.pop("provider_id")

        provider_name = d.pop("provider_name")

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        available_bytes = d.pop("available_bytes")

        def _parse_used_bytes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        used_bytes = _parse_used_bytes(d.pop("used_bytes"))

        def _parse_remaining_bytes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        remaining_bytes = _parse_remaining_bytes(d.pop("remaining_bytes"))

        def _parse_remaining_percent(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        remaining_percent = _parse_remaining_percent(d.pop("remaining_percent"))

        def _parse_severity(data: object) -> None | SeverityEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                severity_type_0 = SeverityEnum(data)

                return severity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SeverityEnum, data)

        severity = _parse_severity(d.pop("severity"))

        freshness = FreshnessEnum(d.pop("freshness"))

        error = d.pop("error")

        def _parse_calculated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                calculated_at_type_0 = datetime.datetime.fromisoformat(data)

                return calculated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        calculated_at = _parse_calculated_at(d.pop("calculated_at"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = ProviderBalanceCheckpoint.from_dict(history_item_data)

            history.append(history_item)

        provider_data_balance = cls(
            checkpoint_id=checkpoint_id,
            provider_id=provider_id,
            provider_name=provider_name,
            observed_at=observed_at,
            available_bytes=available_bytes,
            used_bytes=used_bytes,
            remaining_bytes=remaining_bytes,
            remaining_percent=remaining_percent,
            severity=severity,
            freshness=freshness,
            error=error,
            calculated_at=calculated_at,
            history=history,
        )

        provider_data_balance.additional_properties = d
        return provider_data_balance

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
