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


T = TypeVar("T", bound="CouponUpdateRequest")


@_attrs_define
class CouponUpdateRequest:
    value: int
    """ Arbitrary coupon value """
    type_: CouponTypeEnum
    """ * `free_data` - Free Data * `monetary` - Money * `percentage` - Percentage """
    code: str | Unset = UNSET
    """ Coupon code cannot be changed if already set """
    is_multi_use: bool | Unset = UNSET
    """ If true, coupon can be used multiple times. """
    is_available_to_one_time: bool | Unset = UNSET
    """ If true, coupon can not be used for one-time package tiers. """
    marketer: None | Unset | UUID = UNSET
    """ The marketer who owns this coupon. Required if is_marketer is true. """
    limit: int | Unset = UNSET
    """ Number of times coupon can be used """
    valid_until: datetime.datetime | None | Unset = UNSET
    """ Leave empty for coupons that never expire """
    packages: list[str] | Unset = UNSET
    """ Select packages for which this coupon is available. If no packages are selected, the coupon is available to
    all packages. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_ = self.type_.value

        code = self.code

        is_multi_use = self.is_multi_use

        is_available_to_one_time = self.is_available_to_one_time

        marketer: None | str | Unset
        if isinstance(self.marketer, Unset):
            marketer = UNSET
        elif isinstance(self.marketer, UUID):
            marketer = str(self.marketer)
        else:
            marketer = self.marketer

        limit = self.limit

        valid_until: None | str | Unset
        if isinstance(self.valid_until, Unset):
            valid_until = UNSET
        elif isinstance(self.valid_until, datetime.datetime):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        packages: list[str] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = self.packages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "type": type_,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if is_multi_use is not UNSET:
            field_dict["is_multi_use"] = is_multi_use
        if is_available_to_one_time is not UNSET:
            field_dict["is_available_to_one_time"] = is_available_to_one_time
        if marketer is not UNSET:
            field_dict["marketer"] = marketer
        if limit is not UNSET:
            field_dict["limit"] = limit
        if valid_until is not UNSET:
            field_dict["valid_until"] = valid_until
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        type_ = CouponTypeEnum(d.pop("type"))

        code = d.pop("code", UNSET)

        is_multi_use = d.pop("is_multi_use", UNSET)

        is_available_to_one_time = d.pop("is_available_to_one_time", UNSET)

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

        packages = cast(list[str], d.pop("packages", UNSET))

        coupon_update_request = cls(
            value=value,
            type_=type_,
            code=code,
            is_multi_use=is_multi_use,
            is_available_to_one_time=is_available_to_one_time,
            marketer=marketer,
            limit=limit,
            valid_until=valid_until,
            packages=packages,
        )

        coupon_update_request.additional_properties = d
        return coupon_update_request

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
