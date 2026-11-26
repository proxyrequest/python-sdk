from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.static_connection_state_enum import StaticConnectionStateEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.static_asn import StaticASN


T = TypeVar("T", bound="StaticConnection")


@_attrs_define
class StaticConnection:
    assignment_id: UUID
    address_id: UUID
    source_ip: str
    host: str
    http_port: int | None
    socks_port: int | None
    state: StaticConnectionStateEnum
    """ * `active` - active * `held` - held * `provisioning` - provisioning """
    asn: None | StaticASN
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.static_asn import StaticASN

        assignment_id = str(self.assignment_id)

        address_id = str(self.address_id)

        source_ip = self.source_ip

        host = self.host

        http_port: int | None
        http_port = self.http_port

        socks_port: int | None
        socks_port = self.socks_port

        state = self.state.value

        asn: dict[str, Any] | None
        if isinstance(self.asn, StaticASN):
            asn = self.asn.to_dict()
        else:
            asn = self.asn

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignment_id": assignment_id,
                "address_id": address_id,
                "source_ip": source_ip,
                "host": host,
                "http_port": http_port,
                "socks_port": socks_port,
                "state": state,
                "asn": asn,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.static_asn import StaticASN

        d = dict(src_dict)
        assignment_id = UUID(d.pop("assignment_id"))

        address_id = UUID(d.pop("address_id"))

        source_ip = d.pop("source_ip")

        host = d.pop("host")

        def _parse_http_port(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        http_port = _parse_http_port(d.pop("http_port"))

        def _parse_socks_port(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        socks_port = _parse_socks_port(d.pop("socks_port"))

        state = StaticConnectionStateEnum(d.pop("state"))

        def _parse_asn(data: object) -> None | StaticASN:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                asn_type_1 = StaticASN.from_dict(data)

                return asn_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StaticASN, data)

        asn = _parse_asn(d.pop("asn"))

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        static_connection = cls(
            assignment_id=assignment_id,
            address_id=address_id,
            source_ip=source_ip,
            host=host,
            http_port=http_port,
            socks_port=socks_port,
            state=state,
            asn=asn,
            username=username,
            password=password,
        )

        static_connection.additional_properties = d
        return static_connection

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
