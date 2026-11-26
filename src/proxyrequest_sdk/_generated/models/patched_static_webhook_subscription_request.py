from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.static_events_enum import StaticEventsEnum
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="PatchedStaticWebhookSubscriptionRequest")


@_attrs_define
class PatchedStaticWebhookSubscriptionRequest:
    static_events: list[StaticEventsEnum] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        static_events: list[str] | Unset = UNSET
        if not isinstance(self.static_events, Unset):
            static_events = []
            for static_events_item_data in self.static_events:
                static_events_item = static_events_item_data.value
                static_events.append(static_events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if static_events is not UNSET:
            field_dict["static_events"] = static_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _static_events = d.pop("static_events", UNSET)
        static_events: list[StaticEventsEnum] | Unset = UNSET
        if _static_events is not UNSET:
            static_events = []
            for static_events_item_data in _static_events:
                static_events_item = StaticEventsEnum(static_events_item_data)

                static_events.append(static_events_item)

        patched_static_webhook_subscription_request = cls(
            static_events=static_events,
        )

        patched_static_webhook_subscription_request.additional_properties = d
        return patched_static_webhook_subscription_request

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
