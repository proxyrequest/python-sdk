from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provider_enum import ProviderEnum


T = TypeVar("T", bound="SocialAccountState")


@_attrs_define
class SocialAccountState:
    provider: ProviderEnum
    """ * `discord` - discord * `google` - google * `meta` - meta * `twitter` - twitter """
    linked: bool
    can_unlink: bool
    unlink_block_reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        linked = self.linked

        can_unlink = self.can_unlink

        unlink_block_reason = self.unlink_block_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "linked": linked,
                "can_unlink": can_unlink,
                "unlink_block_reason": unlink_block_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = ProviderEnum(d.pop("provider"))

        linked = d.pop("linked")

        can_unlink = d.pop("can_unlink")

        unlink_block_reason = d.pop("unlink_block_reason")

        social_account_state = cls(
            provider=provider,
            linked=linked,
            can_unlink=can_unlink,
            unlink_block_reason=unlink_block_reason,
        )

        social_account_state.additional_properties = d
        return social_account_state

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
