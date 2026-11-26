from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.purchase_response import PurchaseResponse


T = TypeVar("T", bound="StaticPurchasePage")


@_attrs_define
class StaticPurchasePage:
    count: int
    next_: None | str
    previous: None | str
    results: list[PurchaseResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.purchase_response import PurchaseResponse

        count = self.count

        next_: None | str
        next_ = self.next_

        previous: None | str
        previous = self.previous

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "next": next_,
                "previous": previous,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.purchase_response import PurchaseResponse

        d = dict(src_dict)
        count = d.pop("count")

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

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = PurchaseResponse.from_dict(results_item_data)

            results.append(results_item)

        static_purchase_page = cls(
            count=count,
            next_=next_,
            previous=previous,
            results=results,
        )

        static_purchase_page.additional_properties = d
        return static_purchase_page

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
