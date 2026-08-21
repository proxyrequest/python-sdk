from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="GeneratedProxy")


@_attrs_define
class GeneratedProxy:
    host: str
    port: int
    protocol: str
    username: str
    password: str
    connection_string: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        protocol = self.protocol

        username = self.username

        password = self.password

        connection_string = self.connection_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "port": port,
                "protocol": protocol,
                "username": username,
                "password": password,
                "connection_string": connection_string,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        port = d.pop("port")

        protocol = d.pop("protocol")

        username = d.pop("username")

        password = d.pop("password")

        connection_string = d.pop("connection_string")

        generated_proxy = cls(
            host=host,
            port=port,
            protocol=protocol,
            username=username,
            password=password,
            connection_string=connection_string,
        )

        generated_proxy.additional_properties = d
        return generated_proxy

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
