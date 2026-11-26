from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="EnabledResponse")


@_attrs_define
class EnabledResponse:
    enabled: bool
    has_password: bool | Unset = UNSET
    can_reset: bool | Unset = UNSET
    self_: bool | Unset = UNSET
    requires_reauth: bool | Unset = UNSET
    secret: str | Unset = UNSET
    otpauth_url: str | Unset = UNSET
    qr_svg: str | Unset = UNSET
    recovery_codes: list[str] | Unset = UNSET
    recovery_codes_remaining: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        has_password = self.has_password

        can_reset = self.can_reset

        self_ = self.self_

        requires_reauth = self.requires_reauth

        secret = self.secret

        otpauth_url = self.otpauth_url

        qr_svg = self.qr_svg

        recovery_codes: list[str] | Unset = UNSET
        if not isinstance(self.recovery_codes, Unset):
            recovery_codes = self.recovery_codes

        recovery_codes_remaining = self.recovery_codes_remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if has_password is not UNSET:
            field_dict["has_password"] = has_password
        if can_reset is not UNSET:
            field_dict["can_reset"] = can_reset
        if self_ is not UNSET:
            field_dict["self"] = self_
        if requires_reauth is not UNSET:
            field_dict["requires_reauth"] = requires_reauth
        if secret is not UNSET:
            field_dict["secret"] = secret
        if otpauth_url is not UNSET:
            field_dict["otpauth_url"] = otpauth_url
        if qr_svg is not UNSET:
            field_dict["qr_svg"] = qr_svg
        if recovery_codes is not UNSET:
            field_dict["recovery_codes"] = recovery_codes
        if recovery_codes_remaining is not UNSET:
            field_dict["recovery_codes_remaining"] = recovery_codes_remaining

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        has_password = d.pop("has_password", UNSET)

        can_reset = d.pop("can_reset", UNSET)

        self_ = d.pop("self", UNSET)

        requires_reauth = d.pop("requires_reauth", UNSET)

        secret = d.pop("secret", UNSET)

        otpauth_url = d.pop("otpauth_url", UNSET)

        qr_svg = d.pop("qr_svg", UNSET)

        recovery_codes = cast(list[str], d.pop("recovery_codes", UNSET))

        recovery_codes_remaining = d.pop("recovery_codes_remaining", UNSET)

        enabled_response = cls(
            enabled=enabled,
            has_password=has_password,
            can_reset=can_reset,
            self_=self_,
            requires_reauth=requires_reauth,
            secret=secret,
            otpauth_url=otpauth_url,
            qr_svg=qr_svg,
            recovery_codes=recovery_codes,
            recovery_codes_remaining=recovery_codes_remaining,
        )

        enabled_response.additional_properties = d
        return enabled_response

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
