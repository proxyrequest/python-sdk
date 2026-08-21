from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime


T = TypeVar("T", bound="TransactionRecord")


@_attrs_define
class TransactionRecord:
    sender_uuid: None | str
    recipient_uuid: None | str
    type_: int
    amount: int
    package_uuid: None | str
    details: None | str
    date: datetime.datetime | None
    timestamp: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_uuid: None | str
        sender_uuid = self.sender_uuid

        recipient_uuid: None | str
        recipient_uuid = self.recipient_uuid

        type_ = self.type_

        amount = self.amount

        package_uuid: None | str
        package_uuid = self.package_uuid

        details: None | str
        details = self.details

        date: None | str
        if isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        timestamp: None | str
        if isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sender_uuid": sender_uuid,
                "recipient_uuid": recipient_uuid,
                "type": type_,
                "amount": amount,
                "package_uuid": package_uuid,
                "details": details,
                "date": date,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_sender_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sender_uuid = _parse_sender_uuid(d.pop("sender_uuid"))

        def _parse_recipient_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        recipient_uuid = _parse_recipient_uuid(d.pop("recipient_uuid"))

        type_ = d.pop("type")

        amount = d.pop("amount")

        def _parse_package_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        package_uuid = _parse_package_uuid(d.pop("package_uuid"))

        def _parse_details(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        details = _parse_details(d.pop("details"))

        def _parse_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.datetime.fromisoformat(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date = _parse_date(d.pop("date"))

        def _parse_timestamp(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        timestamp = _parse_timestamp(d.pop("timestamp"))

        transaction_record = cls(
            sender_uuid=sender_uuid,
            recipient_uuid=recipient_uuid,
            type_=type_,
            amount=amount,
            package_uuid=package_uuid,
            details=details,
            date=date,
            timestamp=timestamp,
        )

        transaction_record.additional_properties = d
        return transaction_record

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
