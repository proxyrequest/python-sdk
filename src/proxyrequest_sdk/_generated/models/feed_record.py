from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime


T = TypeVar("T", bound="FeedRecord")


@_attrs_define
class FeedRecord:
    id: int
    established_connections: int
    reseller_id: str
    user_id: str
    package_id: str
    ledger_id: str
    username: str
    user_ip: str
    server_ip: str
    data: int
    hostname: str
    protocol: str
    method: str
    pool: str
    is_session: bool
    country: str
    region: str
    city: str
    asn: str
    timestamp: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        established_connections = self.established_connections

        reseller_id = self.reseller_id

        user_id = self.user_id

        package_id = self.package_id

        ledger_id = self.ledger_id

        username = self.username

        user_ip = self.user_ip

        server_ip = self.server_ip

        data = self.data

        hostname = self.hostname

        protocol = self.protocol

        method = self.method

        pool = self.pool

        is_session = self.is_session

        country = self.country

        region = self.region

        city = self.city

        asn = self.asn

        timestamp: None | str
        if isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "established_connections": established_connections,
                "reseller_id": reseller_id,
                "user_id": user_id,
                "package_id": package_id,
                "ledger_id": ledger_id,
                "username": username,
                "user_ip": user_ip,
                "server_ip": server_ip,
                "data": data,
                "hostname": hostname,
                "protocol": protocol,
                "method": method,
                "pool": pool,
                "is_session": is_session,
                "country": country,
                "region": region,
                "city": city,
                "asn": asn,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        established_connections = d.pop("established_connections")

        reseller_id = d.pop("reseller_id")

        user_id = d.pop("user_id")

        package_id = d.pop("package_id")

        ledger_id = d.pop("ledger_id")

        username = d.pop("username")

        user_ip = d.pop("user_ip")

        server_ip = d.pop("server_ip")

        data = d.pop("data")

        hostname = d.pop("hostname")

        protocol = d.pop("protocol")

        method = d.pop("method")

        pool = d.pop("pool")

        is_session = d.pop("is_session")

        country = d.pop("country")

        region = d.pop("region")

        city = d.pop("city")

        asn = d.pop("asn")

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

        feed_record = cls(
            id=id,
            established_connections=established_connections,
            reseller_id=reseller_id,
            user_id=user_id,
            package_id=package_id,
            ledger_id=ledger_id,
            username=username,
            user_ip=user_ip,
            server_ip=server_ip,
            data=data,
            hostname=hostname,
            protocol=protocol,
            method=method,
            pool=pool,
            is_session=is_session,
            country=country,
            region=region,
            city=city,
            asn=asn,
            timestamp=timestamp,
        )

        feed_record.additional_properties = d
        return feed_record

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
