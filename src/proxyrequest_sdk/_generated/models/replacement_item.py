from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.replacement_item_state_enum import ReplacementItemStateEnum
from typing import cast
from uuid import UUID


T = TypeVar("T", bound="ReplacementItem")


@_attrs_define
class ReplacementItem:
    id: UUID
    endpoint_id: UUID
    state: ReplacementItemStateEnum
    """ * `pending` - pending * `needs_manual` - needs_manual * `provisioning` - provisioning * `completed` -
    completed * `ineligible` - ineligible * `rejected` - rejected """
    source_ip: str
    replacement_ip: None | str
    error: str
    comment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        endpoint_id = str(self.endpoint_id)

        state = self.state.value

        source_ip = self.source_ip

        replacement_ip: None | str
        replacement_ip = self.replacement_ip

        error = self.error

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "endpoint_id": endpoint_id,
                "state": state,
                "source_ip": source_ip,
                "replacement_ip": replacement_ip,
                "error": error,
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        endpoint_id = UUID(d.pop("endpoint_id"))

        state = ReplacementItemStateEnum(d.pop("state"))

        source_ip = d.pop("source_ip")

        def _parse_replacement_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        replacement_ip = _parse_replacement_ip(d.pop("replacement_ip"))

        error = d.pop("error")

        comment = d.pop("comment")

        replacement_item = cls(
            id=id,
            endpoint_id=endpoint_id,
            state=state,
            source_ip=source_ip,
            replacement_ip=replacement_ip,
            error=error,
            comment=comment,
        )

        replacement_item.additional_properties = d
        return replacement_item

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
