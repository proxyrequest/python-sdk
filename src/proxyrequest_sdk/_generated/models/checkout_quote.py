from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.purchase_group import PurchaseGroup


T = TypeVar("T", bound="CheckoutQuote")


@_attrs_define
class CheckoutQuote:
    total: int
    currency: str
    groups: list[PurchaseGroup]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.purchase_group import PurchaseGroup

        total = self.total

        currency = self.currency

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "currency": currency,
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.purchase_group import PurchaseGroup

        d = dict(src_dict)
        total = d.pop("total")

        currency = d.pop("currency")

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = PurchaseGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        checkout_quote = cls(
            total=total,
            currency=currency,
            groups=groups,
        )

        checkout_quote.additional_properties = d
        return checkout_quote

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
