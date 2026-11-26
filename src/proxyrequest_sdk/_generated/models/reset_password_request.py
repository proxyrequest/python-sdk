from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID


T = TypeVar("T", bound="ResetPasswordRequest")


@_attrs_define
class ResetPasswordRequest:
    """Password reset confirmation with enhanced security validation."""

    order_id: UUID | Unset = UNSET
    uidb64: str | Unset = UNSET
    """ Base64 encoded user ID """
    token: str | Unset = UNSET
    """ Password reset token """
    new_password1: str | Unset = UNSET
    """ New password """
    new_password2: str | Unset = UNSET
    """ Confirm new password """
    turnstile_token: str | Unset = UNSET
    """ Cloudflare Turnstile security token """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id: str | Unset = UNSET
        if not isinstance(self.order_id, Unset):
            order_id = str(self.order_id)

        uidb64 = self.uidb64

        token = self.token

        new_password1 = self.new_password1

        new_password2 = self.new_password2

        turnstile_token = self.turnstile_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if uidb64 is not UNSET:
            field_dict["uidb64"] = uidb64
        if token is not UNSET:
            field_dict["token"] = token
        if new_password1 is not UNSET:
            field_dict["new_password1"] = new_password1
        if new_password2 is not UNSET:
            field_dict["new_password2"] = new_password2
        if turnstile_token is not UNSET:
            field_dict["turnstile_token"] = turnstile_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _order_id = d.pop("order_id", UNSET)
        order_id: UUID | Unset
        if isinstance(_order_id, Unset):
            order_id = UNSET
        else:
            order_id = UUID(_order_id)

        uidb64 = d.pop("uidb64", UNSET)

        token = d.pop("token", UNSET)

        new_password1 = d.pop("new_password1", UNSET)

        new_password2 = d.pop("new_password2", UNSET)

        turnstile_token = d.pop("turnstile_token", UNSET)

        reset_password_request = cls(
            order_id=order_id,
            uidb64=uidb64,
            token=token,
            new_password1=new_password1,
            new_password2=new_password2,
            turnstile_token=turnstile_token,
        )

        reset_password_request.additional_properties = d
        return reset_password_request

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
