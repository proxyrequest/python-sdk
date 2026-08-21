from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="LogRecord")


@_attrs_define
class LogRecord:
    id: int
    server_ip: None | str
    user_ip: None | str
    protocol: str
    method: str
    user_id: str
    reseller_id: str
    username: str
    hostname: str
    status_code: int
    error_code: int
    error_message: str
    country: str
    region: str
    city: str
    asn: str
    level: str
    is_session: bool
    timestamp: datetime.datetime
    package_id: str | Unset = UNSET
    package_alias: str | Unset = UNSET
    ledger_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        server_ip: None | str
        server_ip = self.server_ip

        user_ip: None | str
        user_ip = self.user_ip

        protocol = self.protocol

        method = self.method

        user_id = self.user_id

        reseller_id = self.reseller_id

        username = self.username

        hostname = self.hostname

        status_code = self.status_code

        error_code = self.error_code

        error_message = self.error_message

        country = self.country

        region = self.region

        city = self.city

        asn = self.asn

        level = self.level

        is_session = self.is_session

        timestamp = self.timestamp.isoformat()

        package_id = self.package_id

        package_alias = self.package_alias

        ledger_id = self.ledger_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "server_ip": server_ip,
                "user_ip": user_ip,
                "protocol": protocol,
                "method": method,
                "user_id": user_id,
                "reseller_id": reseller_id,
                "username": username,
                "hostname": hostname,
                "status_code": status_code,
                "error_code": error_code,
                "error_message": error_message,
                "country": country,
                "region": region,
                "city": city,
                "asn": asn,
                "level": level,
                "is_session": is_session,
                "timestamp": timestamp,
            }
        )
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if package_alias is not UNSET:
            field_dict["package_alias"] = package_alias
        if ledger_id is not UNSET:
            field_dict["ledger_id"] = ledger_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_server_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        server_ip = _parse_server_ip(d.pop("server_ip"))

        def _parse_user_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_ip = _parse_user_ip(d.pop("user_ip"))

        protocol = d.pop("protocol")

        method = d.pop("method")

        user_id = d.pop("user_id")

        reseller_id = d.pop("reseller_id")

        username = d.pop("username")

        hostname = d.pop("hostname")

        status_code = d.pop("status_code")

        error_code = d.pop("error_code")

        error_message = d.pop("error_message")

        country = d.pop("country")

        region = d.pop("region")

        city = d.pop("city")

        asn = d.pop("asn")

        level = d.pop("level")

        is_session = d.pop("is_session")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        package_id = d.pop("package_id", UNSET)

        package_alias = d.pop("package_alias", UNSET)

        ledger_id = d.pop("ledger_id", UNSET)

        log_record = cls(
            id=id,
            server_ip=server_ip,
            user_ip=user_ip,
            protocol=protocol,
            method=method,
            user_id=user_id,
            reseller_id=reseller_id,
            username=username,
            hostname=hostname,
            status_code=status_code,
            error_code=error_code,
            error_message=error_message,
            country=country,
            region=region,
            city=city,
            asn=asn,
            level=level,
            is_session=is_session,
            timestamp=timestamp,
            package_id=package_id,
            package_alias=package_alias,
            ledger_id=ledger_id,
        )

        log_record.additional_properties = d
        return log_record

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
