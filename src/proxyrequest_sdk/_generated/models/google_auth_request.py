from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="GoogleAuthRequest")


@_attrs_define
class GoogleAuthRequest:
    """Enhanced Google OAuth authentication with comprehensive security validation and user management."""

    credential: str
    """ Google ID token credential """
    client_id: str | Unset = UNSET
    """ Google OAuth client ID """
    select_by: str | Unset = UNSET
    """ User selection method """
    affiliate_code: str | Unset = UNSET
    """ Optional affiliate code """
    referral_code: str | Unset = UNSET
    """ Optional referral code """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential = self.credential

        client_id = self.client_id

        select_by = self.select_by

        affiliate_code = self.affiliate_code

        referral_code = self.referral_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credential": credential,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if select_by is not UNSET:
            field_dict["select_by"] = select_by
        if affiliate_code is not UNSET:
            field_dict["affiliate_code"] = affiliate_code
        if referral_code is not UNSET:
            field_dict["referral_code"] = referral_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential = d.pop("credential")

        client_id = d.pop("client_id", UNSET)

        select_by = d.pop("select_by", UNSET)

        affiliate_code = d.pop("affiliate_code", UNSET)

        referral_code = d.pop("referral_code", UNSET)

        google_auth_request = cls(
            credential=credential,
            client_id=client_id,
            select_by=select_by,
            affiliate_code=affiliate_code,
            referral_code=referral_code,
        )

        google_auth_request.additional_properties = d
        return google_auth_request

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
