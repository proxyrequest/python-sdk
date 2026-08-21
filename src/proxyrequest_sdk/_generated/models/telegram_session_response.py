from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.telegram_session_response_user import TelegramSessionResponseUser


T = TypeVar("T", bound="TelegramSessionResponse")


@_attrs_define
class TelegramSessionResponse:
    access: str
    expires_in: int
    locale: str
    timezone: str
    user: TelegramSessionResponseUser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.telegram_session_response_user import TelegramSessionResponseUser

        access = self.access

        expires_in = self.expires_in

        locale = self.locale

        timezone = self.timezone

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "expires_in": expires_in,
                "locale": locale,
                "timezone": timezone,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.telegram_session_response_user import TelegramSessionResponseUser

        d = dict(src_dict)
        access = d.pop("access")

        expires_in = d.pop("expires_in")

        locale = d.pop("locale")

        timezone = d.pop("timezone")

        user = TelegramSessionResponseUser.from_dict(d.pop("user"))

        telegram_session_response = cls(
            access=access,
            expires_in=expires_in,
            locale=locale,
            timezone=timezone,
            user=user,
        )

        telegram_session_response.additional_properties = d
        return telegram_session_response

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
