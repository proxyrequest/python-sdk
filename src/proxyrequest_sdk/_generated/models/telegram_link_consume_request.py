from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="TelegramLinkConsumeRequest")


@_attrs_define
class TelegramLinkConsumeRequest:
    token: str
    telegram_user_id: int
    chat_id: int
    username: str | Unset = UNSET
    language_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        telegram_user_id = self.telegram_user_id

        chat_id = self.chat_id

        username = self.username

        language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "telegram_user_id": telegram_user_id,
                "chat_id": chat_id,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if language_code is not UNSET:
            field_dict["language_code"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        telegram_user_id = d.pop("telegram_user_id")

        chat_id = d.pop("chat_id")

        username = d.pop("username", UNSET)

        language_code = d.pop("language_code", UNSET)

        telegram_link_consume_request = cls(
            token=token,
            telegram_user_id=telegram_user_id,
            chat_id=chat_id,
            username=username,
            language_code=language_code,
        )

        telegram_link_consume_request.additional_properties = d
        return telegram_link_consume_request

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
