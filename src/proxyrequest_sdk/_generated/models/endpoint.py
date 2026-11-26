from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.endpoint_capabilities import EndpointCapabilities
    from ..models.period import Period
    from ..models.static_connection import StaticConnection


T = TypeVar("T", bound="Endpoint")


@_attrs_define
class Endpoint:
    order_id: str
    allowed_ips: list[str]
    periods: list[Period]
    connections: list[StaticConnection]
    max_bandwidth_mbps: int | None
    capabilities: EndpointCapabilities
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.endpoint_capabilities import EndpointCapabilities
        from ..models.period import Period
        from ..models.static_connection import StaticConnection

        order_id = self.order_id

        allowed_ips = self.allowed_ips

        periods = []
        for periods_item_data in self.periods:
            periods_item = periods_item_data.to_dict()
            periods.append(periods_item)

        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()
            connections.append(connections_item)

        max_bandwidth_mbps: int | None
        max_bandwidth_mbps = self.max_bandwidth_mbps

        capabilities = self.capabilities.to_dict()

        id = self.id

        label = self.label

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "allowed_ips": allowed_ips,
                "periods": periods,
                "connections": connections,
                "max_bandwidth_mbps": max_bandwidth_mbps,
                "capabilities": capabilities,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_capabilities import EndpointCapabilities
        from ..models.period import Period
        from ..models.static_connection import StaticConnection

        d = dict(src_dict)
        order_id = d.pop("order_id")

        allowed_ips = cast(list[str], d.pop("allowed_ips"))

        periods = []
        _periods = d.pop("periods")
        for periods_item_data in _periods:
            periods_item = Period.from_dict(periods_item_data)

            periods.append(periods_item)

        connections = []
        _connections = d.pop("connections")
        for connections_item_data in _connections:
            connections_item = StaticConnection.from_dict(connections_item_data)

            connections.append(connections_item)

        def _parse_max_bandwidth_mbps(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_bandwidth_mbps = _parse_max_bandwidth_mbps(d.pop("max_bandwidth_mbps"))

        capabilities = EndpointCapabilities.from_dict(d.pop("capabilities"))

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        is_active = d.pop("is_active", UNSET)

        endpoint = cls(
            order_id=order_id,
            allowed_ips=allowed_ips,
            periods=periods,
            connections=connections,
            max_bandwidth_mbps=max_bandwidth_mbps,
            capabilities=capabilities,
            id=id,
            label=label,
            is_active=is_active,
        )

        endpoint.additional_properties = d
        return endpoint

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
