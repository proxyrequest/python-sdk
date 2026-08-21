from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CouponPriceResponse")


@_attrs_define
class CouponPriceResponse:
    price_original: int
    """ Original price in the service's smallest currency unit. """
    price_discounted: int
    """ Price after applying the coupon, in the smallest currency unit. """
    discount_percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price_original = self.price_original

        price_discounted = self.price_discounted

        discount_percentage = self.discount_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price_original": price_original,
                "price_discounted": price_discounted,
                "discount_percentage": discount_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price_original = d.pop("price_original")

        price_discounted = d.pop("price_discounted")

        discount_percentage = d.pop("discount_percentage")

        coupon_price_response = cls(
            price_original=price_original,
            price_discounted=price_discounted,
            discount_percentage=discount_percentage,
        )

        coupon_price_response.additional_properties = d
        return coupon_price_response

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
