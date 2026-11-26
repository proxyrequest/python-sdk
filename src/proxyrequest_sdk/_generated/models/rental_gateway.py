from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rental_gateway_protocol_enum import RentalGatewayProtocolEnum


T = TypeVar("T", bound="RentalGateway")


@_attrs_define
class RentalGateway:
    host: str
    protocol: RentalGatewayProtocolEnum
    """ * `http` - http * `socks5` - socks5 """
    port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        protocol = self.protocol.value

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "protocol": protocol,
                "port": port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        protocol = RentalGatewayProtocolEnum(d.pop("protocol"))

        port = d.pop("port")

        rental_gateway = cls(
            host=host,
            protocol=protocol,
            port=port,
        )

        rental_gateway.additional_properties = d
        return rental_gateway

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
