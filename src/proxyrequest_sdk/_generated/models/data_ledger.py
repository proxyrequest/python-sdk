from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime


T = TypeVar("T", bound="DataLedger")


@_attrs_define
class DataLedger:
    """A purchased data bucket, not a complete transaction history. Finite purchases with an expiration have separate
    buckets. Compatible non-expiring top-ups and unlimited packages may reuse an existing bucket.

    """

    id: str
    data: int
    """ Total data allocated to this ledger entry in bytes. 1073741824 = 1 GiB 10737418240 = 10 GiB """
    data_remaining: int
    """ Bytes still available for consumption from this ledger entry. Decremented in FIFO order as the customer uses
    the proxy. When this reaches zero the entry is exhausted. """
    expires: datetime.datetime | None
    """ Date and time when this ledger entry expires and any remaining data is forfeited. Leave blank for entries
    that do not expire. """
    updated: datetime.datetime
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        data = self.data

        data_remaining = self.data_remaining

        expires: None | str
        if isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        updated = self.updated.isoformat()

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "data": data,
                "data_remaining": data_remaining,
                "expires": expires,
                "updated": updated,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        data = d.pop("data")

        data_remaining = d.pop("data_remaining")

        def _parse_expires(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = datetime.datetime.fromisoformat(data)

                return expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires = _parse_expires(d.pop("expires"))

        updated = datetime.datetime.fromisoformat(d.pop("updated"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        data_ledger = cls(
            id=id,
            data=data,
            data_remaining=data_remaining,
            expires=expires,
            updated=updated,
            created=created,
        )

        data_ledger.additional_properties = d
        return data_ledger

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
