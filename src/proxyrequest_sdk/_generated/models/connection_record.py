from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID


T = TypeVar("T", bound="ConnectionRecord")


@_attrs_define
class ConnectionRecord:
    user_id: UUID
    package_id: UUID
    connections: int
    server_ip: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = str(self.user_id)

        package_id = str(self.package_id)

        connections = self.connections

        server_ip = self.server_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "package_id": package_id,
                "connections": connections,
                "server_ip": server_ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = UUID(d.pop("user_id"))

        package_id = UUID(d.pop("package_id"))

        connections = d.pop("connections")

        server_ip = d.pop("server_ip")

        connection_record = cls(
            user_id=user_id,
            package_id=package_id,
            connections=connections,
            server_ip=server_ip,
        )

        connection_record.additional_properties = d
        return connection_record

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
