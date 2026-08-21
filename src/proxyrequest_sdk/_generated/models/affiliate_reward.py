from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reward_status_enum import RewardStatusEnum
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.package_short import PackageShort


T = TypeVar("T", bound="AffiliateReward")


@_attrs_define
class AffiliateReward:
    email: str
    package: PackageShort
    price_total: int
    commission_amount: int
    created: datetime.datetime
    id: str | Unset = UNSET
    status: RewardStatusEnum | Unset = UNSET
    """ * `pending` - Pending * `paid` - Paid * `review` - Review * `cancelled` - Cancelled """
    data: int | Unset = UNSET
    """ The amount of data in bytes. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.package_short import PackageShort

        email = self.email

        package = self.package.to_dict()

        price_total = self.price_total

        commission_amount = self.commission_amount

        created = self.created.isoformat()

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "package": package,
                "price_total": price_total,
                "commission_amount": commission_amount,
                "created": created,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_short import PackageShort

        d = dict(src_dict)
        email = d.pop("email")

        package = PackageShort.from_dict(d.pop("package"))

        price_total = d.pop("price_total")

        commission_amount = d.pop("commission_amount")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: RewardStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RewardStatusEnum(_status)

        data = d.pop("data", UNSET)

        affiliate_reward = cls(
            email=email,
            package=package,
            price_total=price_total,
            commission_amount=commission_amount,
            created=created,
            id=id,
            status=status,
            data=data,
        )

        affiliate_reward.additional_properties = d
        return affiliate_reward

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
