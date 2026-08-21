from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.coupon_type_enum import CouponTypeEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.coupon_short_packages_item import CouponShortPackagesItem


T = TypeVar("T", bound="CouponShort")


@_attrs_define
class CouponShort:
    is_expired: bool
    is_redeemed: bool
    packages: list[CouponShortPackagesItem]
    created: datetime.datetime
    value: int
    """ Arbitrary coupon value """
    code: str
    """ Leaving this field empty will generate a random code. """
    type_: CouponTypeEnum
    """ * `free_data` - Free Data * `monetary` - Money * `percentage` - Percentage """
    user: None | UUID
    """ The user who created this coupon. """
    id: str | Unset = UNSET
    is_multi_use: bool | Unset = UNSET
    """ If true, coupon can be used multiple times. """
    is_available_to_one_time: bool | Unset = UNSET
    """ If true, coupon can not be used for one-time package tiers. """
    limit: int | Unset = UNSET
    """ Number of times coupon can be used """
    valid_until: datetime.datetime | None | Unset = UNSET
    """ Leave empty for coupons that never expire """
    marketer: None | Unset | UUID = UNSET
    """ The marketer who owns this coupon. Required if is_marketer is true. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.coupon_short_packages_item import CouponShortPackagesItem

        is_expired = self.is_expired

        is_redeemed = self.is_redeemed

        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()
            packages.append(packages_item)

        created = self.created.isoformat()

        value = self.value

        code = self.code

        type_ = self.type_.value

        user: None | str
        if isinstance(self.user, UUID):
            user = str(self.user)
        else:
            user = self.user

        id = self.id

        is_multi_use = self.is_multi_use

        is_available_to_one_time = self.is_available_to_one_time

        limit = self.limit

        valid_until: None | str | Unset
        if isinstance(self.valid_until, Unset):
            valid_until = UNSET
        elif isinstance(self.valid_until, datetime.datetime):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        marketer: None | str | Unset
        if isinstance(self.marketer, Unset):
            marketer = UNSET
        elif isinstance(self.marketer, UUID):
            marketer = str(self.marketer)
        else:
            marketer = self.marketer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_expired": is_expired,
                "is_redeemed": is_redeemed,
                "packages": packages,
                "created": created,
                "value": value,
                "code": code,
                "type": type_,
                "user": user,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_multi_use is not UNSET:
            field_dict["is_multi_use"] = is_multi_use
        if is_available_to_one_time is not UNSET:
            field_dict["is_available_to_one_time"] = is_available_to_one_time
        if limit is not UNSET:
            field_dict["limit"] = limit
        if valid_until is not UNSET:
            field_dict["valid_until"] = valid_until
        if marketer is not UNSET:
            field_dict["marketer"] = marketer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coupon_short_packages_item import CouponShortPackagesItem

        d = dict(src_dict)
        is_expired = d.pop("is_expired")

        is_redeemed = d.pop("is_redeemed")

        packages = []
        _packages = d.pop("packages")
        for packages_item_data in _packages:
            packages_item = CouponShortPackagesItem.from_dict(packages_item_data)

            packages.append(packages_item)

        created = datetime.datetime.fromisoformat(d.pop("created"))

        value = d.pop("value")

        code = d.pop("code")

        type_ = CouponTypeEnum(d.pop("type"))

        def _parse_user(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_type_0 = UUID(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        user = _parse_user(d.pop("user"))

        id = d.pop("id", UNSET)

        is_multi_use = d.pop("is_multi_use", UNSET)

        is_available_to_one_time = d.pop("is_available_to_one_time", UNSET)

        limit = d.pop("limit", UNSET)

        def _parse_valid_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_until_type_0 = datetime.datetime.fromisoformat(data)

                return valid_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_until = _parse_valid_until(d.pop("valid_until", UNSET))

        def _parse_marketer(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marketer_type_0 = UUID(data)

                return marketer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        marketer = _parse_marketer(d.pop("marketer", UNSET))

        coupon_short = cls(
            is_expired=is_expired,
            is_redeemed=is_redeemed,
            packages=packages,
            created=created,
            value=value,
            code=code,
            type_=type_,
            user=user,
            id=id,
            is_multi_use=is_multi_use,
            is_available_to_one_time=is_available_to_one_time,
            limit=limit,
            valid_until=valid_until,
            marketer=marketer,
        )

        coupon_short.additional_properties = d
        return coupon_short

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
