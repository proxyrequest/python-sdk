from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="TwoFactorSetupResponse")


@_attrs_define
class TwoFactorSetupResponse:
    secret: str
    otpauth_url: str
    qr_png_base64: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        otpauth_url = self.otpauth_url

        qr_png_base64 = self.qr_png_base64

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
                "otpauth_url": otpauth_url,
            }
        )
        if qr_png_base64 is not UNSET:
            field_dict["qr_png_base64"] = qr_png_base64

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret = d.pop("secret")

        otpauth_url = d.pop("otpauth_url")

        qr_png_base64 = d.pop("qr_png_base64", UNSET)

        two_factor_setup_response = cls(
            secret=secret,
            otpauth_url=otpauth_url,
            qr_png_base64=qr_png_base64,
        )

        two_factor_setup_response.additional_properties = d
        return two_factor_setup_response

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
