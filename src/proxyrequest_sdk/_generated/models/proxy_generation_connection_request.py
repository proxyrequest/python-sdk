from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.protocol_enum import ProtocolEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="ProxyGenerationConnectionRequest")


@_attrs_define
class ProxyGenerationConnectionRequest:
    protocol: ProtocolEnum | Unset = ProtocolEnum.HTTP
    """ * `http` - http * `socks5` - socks5 * `auto` - auto """
    host: str | Unset = UNSET
    """ Gateway host. Leave empty to use the default gateway. """
    port: int | Unset = UNSET
    """ Gateway port. Leave empty to use the port for the selected protocol. """
    format_: str | Unset = "{protocol}://{username}:{password}@{host}:{port}"
    """ Connection string format. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        host = self.host

        port = self.port

        format_ = self.format_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _protocol = d.pop("protocol", UNSET)
        protocol: ProtocolEnum | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = ProtocolEnum(_protocol)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        format_ = d.pop("format", UNSET)

        proxy_generation_connection_request = cls(
            protocol=protocol,
            host=host,
            port=port,
            format_=format_,
        )

        proxy_generation_connection_request.additional_properties = d
        return proxy_generation_connection_request

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
