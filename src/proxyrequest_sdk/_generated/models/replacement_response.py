from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reason_enum import ReasonEnum
from ..models.static_replacement_status_enum import StaticReplacementStatusEnum
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.replacement_item import ReplacementItem


T = TypeVar("T", bound="ReplacementResponse")


@_attrs_define
class ReplacementResponse:
    id: UUID
    order_id: UUID
    reason: ReasonEnum
    """ * `not_working` - not_working * `slow_speed` - slow_speed * `blocked` - blocked * `other` - other """
    details: str
    status: StaticReplacementStatusEnum
    """ * `pending` - pending * `rejected` - rejected * `needs_manual` - needs_manual * `processing` - processing *
    `ineligible` - ineligible * `partial` - partial * `completed` - completed """
    comment: str
    created: datetime.datetime
    items: list[ReplacementItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.replacement_item import ReplacementItem

        id = str(self.id)

        order_id = str(self.order_id)

        reason = self.reason.value

        details = self.details

        status = self.status.value

        comment = self.comment

        created = self.created.isoformat()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "order_id": order_id,
                "reason": reason,
                "details": details,
                "status": status,
                "comment": comment,
                "created": created,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replacement_item import ReplacementItem

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        order_id = UUID(d.pop("order_id"))

        reason = ReasonEnum(d.pop("reason"))

        details = d.pop("details")

        status = StaticReplacementStatusEnum(d.pop("status"))

        comment = d.pop("comment")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ReplacementItem.from_dict(items_item_data)

            items.append(items_item)

        replacement_response = cls(
            id=id,
            order_id=order_id,
            reason=reason,
            details=details,
            status=status,
            comment=comment,
            created=created,
            items=items,
        )

        replacement_response.additional_properties = d
        return replacement_response

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
