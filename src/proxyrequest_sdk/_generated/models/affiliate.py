from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime


T = TypeVar("T", bound="Affiliate")


@_attrs_define
class Affiliate:
    email: str
    id: UUID | Unset = UNSET
    signup_ip: None | str | Unset = UNSET
    """ IP address from which the user signed up. This field is optional and can be used for tracking purposes. """
    signup_country: str | Unset = UNSET
    """ Country from which the user signed up. This field is optional and can be used for tracking purposes. """
    date_joined: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        signup_ip: None | str | Unset
        if isinstance(self.signup_ip, Unset):
            signup_ip = UNSET
        else:
            signup_ip = self.signup_ip

        signup_country = self.signup_country

        date_joined: str | Unset = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if signup_ip is not UNSET:
            field_dict["signup_ip"] = signup_ip
        if signup_country is not UNSET:
            field_dict["signup_country"] = signup_country
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_signup_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signup_ip = _parse_signup_ip(d.pop("signup_ip", UNSET))

        signup_country = d.pop("signup_country", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: datetime.datetime | Unset
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = datetime.datetime.fromisoformat(_date_joined)

        affiliate = cls(
            email=email,
            id=id,
            signup_ip=signup_ip,
            signup_country=signup_country,
            date_joined=date_joined,
        )

        affiliate.additional_properties = d
        return affiliate

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
