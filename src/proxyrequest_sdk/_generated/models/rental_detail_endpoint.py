from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.password_rotation_status_enum import PasswordRotationStatusEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.period import Period
    from ..models.rental_detail_endpoint_capabilities import RentalDetailEndpointCapabilities
    from ..models.static_connection import StaticConnection


T = TypeVar("T", bound="RentalDetailEndpoint")


@_attrs_define
class RentalDetailEndpoint:
    order_id: str
    allowed_ips: list[str]
    periods: list[Period]
    connections: list[StaticConnection]
    max_bandwidth_mbps: int | None
    capabilities: RentalDetailEndpointCapabilities
    group_id: None | UUID
    group_size: int
    renewable: bool
    ready: bool
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    password_rotation_status: None | PasswordRotationStatusEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.period import Period
        from ..models.rental_detail_endpoint_capabilities import RentalDetailEndpointCapabilities
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

        group_id: None | str
        if isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        group_size = self.group_size

        renewable = self.renewable

        ready = self.ready

        id = self.id

        label = self.label

        is_active = self.is_active

        password_rotation_status: None | str | Unset
        if isinstance(self.password_rotation_status, Unset):
            password_rotation_status = UNSET
        elif isinstance(self.password_rotation_status, PasswordRotationStatusEnum):
            password_rotation_status = self.password_rotation_status.value
        else:
            password_rotation_status = self.password_rotation_status

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
                "group_id": group_id,
                "group_size": group_size,
                "renewable": renewable,
                "ready": ready,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if password_rotation_status is not UNSET:
            field_dict["password_rotation_status"] = password_rotation_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.period import Period
        from ..models.rental_detail_endpoint_capabilities import RentalDetailEndpointCapabilities
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

        capabilities = RentalDetailEndpointCapabilities.from_dict(d.pop("capabilities"))

        def _parse_group_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)

                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        group_id = _parse_group_id(d.pop("group_id"))

        group_size = d.pop("group_size")

        renewable = d.pop("renewable")

        ready = d.pop("ready")

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_password_rotation_status(
            data: object,
        ) -> None | PasswordRotationStatusEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                password_rotation_status_type_0 = PasswordRotationStatusEnum(data)

                return password_rotation_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PasswordRotationStatusEnum | Unset, data)

        password_rotation_status = _parse_password_rotation_status(
            d.pop("password_rotation_status", UNSET)
        )

        rental_detail_endpoint = cls(
            order_id=order_id,
            allowed_ips=allowed_ips,
            periods=periods,
            connections=connections,
            max_bandwidth_mbps=max_bandwidth_mbps,
            capabilities=capabilities,
            group_id=group_id,
            group_size=group_size,
            renewable=renewable,
            ready=ready,
            id=id,
            label=label,
            is_active=is_active,
            password_rotation_status=password_rotation_status,
        )

        rental_detail_endpoint.additional_properties = d
        return rental_detail_endpoint

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
