from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reason_enum import ReasonEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID


T = TypeVar("T", bound="ReplacementRequestRequest")


@_attrs_define
class ReplacementRequestRequest:
    endpoint_ids: list[UUID]
    reason: ReasonEnum
    """ * `not_working` - not_working * `slow_speed` - slow_speed * `blocked` - blocked * `other` - other """
    details: str | Unset = ""
    idempotency_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_ids = []
        for endpoint_ids_item_data in self.endpoint_ids:
            endpoint_ids_item = str(endpoint_ids_item_data)
            endpoint_ids.append(endpoint_ids_item)

        reason = self.reason.value

        details = self.details

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint_ids": endpoint_ids,
                "reason": reason,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint_ids = []
        _endpoint_ids = d.pop("endpoint_ids")
        for endpoint_ids_item_data in _endpoint_ids:
            endpoint_ids_item = UUID(endpoint_ids_item_data)

            endpoint_ids.append(endpoint_ids_item)

        reason = ReasonEnum(d.pop("reason"))

        details = d.pop("details", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        replacement_request_request = cls(
            endpoint_ids=endpoint_ids,
            reason=reason,
            details=details,
            idempotency_key=idempotency_key,
        )

        replacement_request_request.additional_properties = d
        return replacement_request_request

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
