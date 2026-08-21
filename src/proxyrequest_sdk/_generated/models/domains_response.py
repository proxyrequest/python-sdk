from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.domain_record import DomainRecord


T = TypeVar("T", bound="DomainsResponse")


@_attrs_define
class DomainsResponse:
    next_: None | str
    previous: None | str
    timezone: str
    start: datetime.datetime
    end: datetime.datetime
    results: list[DomainRecord]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_record import DomainRecord

        next_: None | str
        next_ = self.next_

        previous: None | str
        previous = self.previous

        timezone = self.timezone

        start = self.start.isoformat()

        end = self.end.isoformat()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next": next_,
                "previous": previous,
                "timezone": timezone,
                "start": start,
                "end": end,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_record import DomainRecord

        d = dict(src_dict)

        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        def _parse_previous(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous = _parse_previous(d.pop("previous"))

        timezone = d.pop("timezone")

        start = datetime.datetime.fromisoformat(d.pop("start"))

        end = datetime.datetime.fromisoformat(d.pop("end"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = DomainRecord.from_dict(results_item_data)

            results.append(results_item)

        domains_response = cls(
            next_=next_,
            previous=previous,
            timezone=timezone,
            start=start,
            end=end,
            results=results,
        )

        domains_response.additional_properties = d
        return domains_response

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
