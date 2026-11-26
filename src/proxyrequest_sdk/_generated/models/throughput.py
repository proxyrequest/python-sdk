from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.throughput_stats_type_0 import ThroughputStatsType0


T = TypeVar("T", bound="Throughput")


@_attrs_define
class Throughput:
    available: bool
    bytes_per_second: int | None
    mbps: float | None
    stats: None | ThroughputStatsType0
    partial: bool | Unset = UNSET
    observed_at_unix_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.throughput_stats_type_0 import ThroughputStatsType0

        available = self.available

        bytes_per_second: int | None
        bytes_per_second = self.bytes_per_second

        mbps: float | None
        mbps = self.mbps

        stats: dict[str, Any] | None
        if isinstance(self.stats, ThroughputStatsType0):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        partial = self.partial

        observed_at_unix_ms = self.observed_at_unix_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available": available,
                "bytes_per_second": bytes_per_second,
                "mbps": mbps,
                "stats": stats,
            }
        )
        if partial is not UNSET:
            field_dict["partial"] = partial
        if observed_at_unix_ms is not UNSET:
            field_dict["observed_at_unix_ms"] = observed_at_unix_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.throughput_stats_type_0 import ThroughputStatsType0

        d = dict(src_dict)
        available = d.pop("available")

        def _parse_bytes_per_second(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        bytes_per_second = _parse_bytes_per_second(d.pop("bytes_per_second"))

        def _parse_mbps(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mbps = _parse_mbps(d.pop("mbps"))

        def _parse_stats(data: object) -> None | ThroughputStatsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = ThroughputStatsType0.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ThroughputStatsType0, data)

        stats = _parse_stats(d.pop("stats"))

        partial = d.pop("partial", UNSET)

        observed_at_unix_ms = d.pop("observed_at_unix_ms", UNSET)

        throughput = cls(
            available=available,
            bytes_per_second=bytes_per_second,
            mbps=mbps,
            stats=stats,
            partial=partial,
            observed_at_unix_ms=observed_at_unix_ms,
        )

        throughput.additional_properties = d
        return throughput

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
