from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="SignUpRequest")


@_attrs_define
class SignUpRequest:
    """Comprehensive user registration with enhanced validation, security measures, and referral/affiliate code handling."""

    email: str
    """ Valid email address for account creation """
    password: str
    """ Strong password meeting security requirements """
    token: str
    """ Cloudflare Turnstile security token """
    affiliate_code: str | Unset = UNSET
    """ Optional affiliate referral code """
    referral_code: str | Unset = UNSET
    """ Optional user referral code """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        token = self.token

        affiliate_code = self.affiliate_code

        referral_code = self.referral_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
                "token": token,
            }
        )
        if affiliate_code is not UNSET:
            field_dict["affiliate_code"] = affiliate_code
        if referral_code is not UNSET:
            field_dict["referral_code"] = referral_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        password = d.pop("password")

        token = d.pop("token")

        affiliate_code = d.pop("affiliate_code", UNSET)

        referral_code = d.pop("referral_code", UNSET)

        sign_up_request = cls(
            email=email,
            password=password,
            token=token,
            affiliate_code=affiliate_code,
            referral_code=referral_code,
        )

        sign_up_request.additional_properties = d
        return sign_up_request

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
