from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="SettingsReferral")


@_attrs_define
class SettingsReferral:
    reward_balance_percentage: float
    reward_data_percentage: float
    reward_min_balance: float
    reward_min_data: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reward_balance_percentage = self.reward_balance_percentage

        reward_data_percentage = self.reward_data_percentage

        reward_min_balance = self.reward_min_balance

        reward_min_data = self.reward_min_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reward_balance_percentage": reward_balance_percentage,
                "reward_data_percentage": reward_data_percentage,
                "reward_min_balance": reward_min_balance,
                "reward_min_data": reward_min_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reward_balance_percentage = d.pop("reward_balance_percentage")

        reward_data_percentage = d.pop("reward_data_percentage")

        reward_min_balance = d.pop("reward_min_balance")

        reward_min_data = d.pop("reward_min_data")

        settings_referral = cls(
            reward_balance_percentage=reward_balance_percentage,
            reward_data_percentage=reward_data_percentage,
            reward_min_balance=reward_min_balance,
            reward_min_data=reward_min_data,
        )

        settings_referral.additional_properties = d
        return settings_referral

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
