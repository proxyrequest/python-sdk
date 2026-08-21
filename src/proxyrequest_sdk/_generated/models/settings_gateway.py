from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID


T = TypeVar("T", bound="SettingsGateway")


@_attrs_define
class SettingsGateway:
    id: UUID
    name: str
    region: str
    hostname: str
    hostnames: list[str]
    port_http: int
    port_socks5: int
    port_auto: int
    port_haproxy: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        region = self.region

        hostname = self.hostname

        hostnames = self.hostnames

        port_http = self.port_http

        port_socks5 = self.port_socks5

        port_auto = self.port_auto

        port_haproxy = self.port_haproxy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "region": region,
                "hostname": hostname,
                "hostnames": hostnames,
                "port_http": port_http,
                "port_socks5": port_socks5,
                "port_auto": port_auto,
                "port_haproxy": port_haproxy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        region = d.pop("region")

        hostname = d.pop("hostname")

        hostnames = cast(list[str], d.pop("hostnames"))

        port_http = d.pop("port_http")

        port_socks5 = d.pop("port_socks5")

        port_auto = d.pop("port_auto")

        port_haproxy = d.pop("port_haproxy")

        settings_gateway = cls(
            id=id,
            name=name,
            region=region,
            hostname=hostname,
            hostnames=hostnames,
            port_http=port_http,
            port_socks5=port_socks5,
            port_auto=port_auto,
            port_haproxy=port_haproxy,
        )

        settings_gateway.additional_properties = d
        return settings_gateway

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
