from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.invoice import Invoice
    from ..models.invoice_short import InvoiceShort


T = TypeVar("T", bound="PaginatedInvoiceReadList")


@_attrs_define
class PaginatedInvoiceReadList:
    count: int
    results: list[Invoice | InvoiceShort]
    next_: None | str | Unset = UNSET
    previous: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice import Invoice
        from ..models.invoice_short import InvoiceShort

        count = self.count

        results = []
        for results_item_data in self.results:
            results_item: dict[str, Any]
            if isinstance(results_item_data, Invoice):
                results_item = results_item_data.to_dict()
            else:
                results_item = results_item_data.to_dict()

            results.append(results_item)

        next_: None | str | Unset
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        previous: None | str | Unset
        if isinstance(self.previous, Unset):
            previous = UNSET
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "results": results,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice import Invoice
        from ..models.invoice_short import InvoiceShort

        d = dict(src_dict)
        count = d.pop("count")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(data: object) -> Invoice | InvoiceShort:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_invoice_read_type_0 = Invoice.from_dict(data)

                    return componentsschemas_invoice_read_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_invoice_read_type_1 = InvoiceShort.from_dict(data)

                return componentsschemas_invoice_read_type_1

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        def _parse_next_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_ = _parse_next_(d.pop("next", UNSET))

        def _parse_previous(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous = _parse_previous(d.pop("previous", UNSET))

        paginated_invoice_read_list = cls(
            count=count,
            results=results,
            next_=next_,
            previous=previous,
        )

        paginated_invoice_read_list.additional_properties = d
        return paginated_invoice_read_list

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
