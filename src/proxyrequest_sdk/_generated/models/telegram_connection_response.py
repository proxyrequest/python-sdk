from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="TelegramConnectionResponse")


@_attrs_define
class TelegramConnectionResponse:
    available: bool
    status: str
    bot_username: str
    locale: str
    timezone: str
    telegram_username: str | Unset = UNSET
    linked_at: datetime.datetime | None | Unset = UNSET
    pending_expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        status = self.status

        bot_username = self.bot_username

        locale = self.locale

        timezone = self.timezone

        telegram_username = self.telegram_username

        linked_at: None | str | Unset
        if isinstance(self.linked_at, Unset):
            linked_at = UNSET
        elif isinstance(self.linked_at, datetime.datetime):
            linked_at = self.linked_at.isoformat()
        else:
            linked_at = self.linked_at

        pending_expires_at: None | str | Unset
        if isinstance(self.pending_expires_at, Unset):
            pending_expires_at = UNSET
        elif isinstance(self.pending_expires_at, datetime.datetime):
            pending_expires_at = self.pending_expires_at.isoformat()
        else:
            pending_expires_at = self.pending_expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available": available,
                "status": status,
                "bot_username": bot_username,
                "locale": locale,
                "timezone": timezone,
            }
        )
        if telegram_username is not UNSET:
            field_dict["telegram_username"] = telegram_username
        if linked_at is not UNSET:
            field_dict["linked_at"] = linked_at
        if pending_expires_at is not UNSET:
            field_dict["pending_expires_at"] = pending_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available")

        status = d.pop("status")

        bot_username = d.pop("bot_username")

        locale = d.pop("locale")

        timezone = d.pop("timezone")

        telegram_username = d.pop("telegram_username", UNSET)

        def _parse_linked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                linked_at_type_0 = datetime.datetime.fromisoformat(data)

                return linked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        linked_at = _parse_linked_at(d.pop("linked_at", UNSET))

        def _parse_pending_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pending_expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return pending_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pending_expires_at = _parse_pending_expires_at(d.pop("pending_expires_at", UNSET))

        telegram_connection_response = cls(
            available=available,
            status=status,
            bot_username=bot_username,
            locale=locale,
            timezone=timezone,
            telegram_username=telegram_username,
            linked_at=linked_at,
            pending_expires_at=pending_expires_at,
        )

        telegram_connection_response.additional_properties = d
        return telegram_connection_response

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
