from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.level_enum import LevelEnum
from ..models.reward_status_enum import RewardStatusEnum
from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="Reward")


@_attrs_define
class Reward:
    email: str
    created: datetime.datetime
    id: str | Unset = UNSET
    balance: int | Unset = UNSET
    data: int | Unset = UNSET
    """ The amount of data in bytes. """
    status: RewardStatusEnum | Unset = UNSET
    """ * `pending` - Pending * `paid` - Paid * `review` - Review * `cancelled` - Cancelled """
    description: str | Unset = UNSET
    """ Description of the reward, used to include payout details. """
    level: LevelEnum | Unset = UNSET
    """ * `standard` - Standard * `silver` - Silver * `gold` - Gold * `diamond` - Diamond """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        created = self.created.isoformat()

        id = self.id

        balance = self.balance

        data = self.data

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "created": created,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if balance is not UNSET:
            field_dict["balance"] = balance
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = d.pop("id", UNSET)

        balance = d.pop("balance", UNSET)

        data = d.pop("data", UNSET)

        _status = d.pop("status", UNSET)
        status: RewardStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RewardStatusEnum(_status)

        description = d.pop("description", UNSET)

        _level = d.pop("level", UNSET)
        level: LevelEnum | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = LevelEnum(_level)

        reward = cls(
            email=email,
            created=created,
            id=id,
            balance=balance,
            data=data,
            status=status,
            description=description,
            level=level,
        )

        reward.additional_properties = d
        return reward

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
