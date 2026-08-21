from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.proxy_generation_connection_request import ProxyGenerationConnectionRequest
    from ..models.proxy_generation_session_request import ProxyGenerationSessionRequest
    from ..models.proxy_generation_targeting_request import ProxyGenerationTargetingRequest


T = TypeVar("T", bound="GenerateProxyRequest")


@_attrs_define
class GenerateProxyRequest:
    """Validates proxy generation request data and builds generator config."""

    package_id: UUID
    """ ProxyRequest package UUID used to generate credentials. Headless integrations must resolve this from their
    local product mapping. """
    quantity: int
    """ Number of proxies to generate """
    user_id: UUID | Unset = UNSET
    """ ProxyRequest sub-user UUID that will use the generated credentials. Headless integrations must resolve this
    from their local customer mapping. """
    targeting: ProxyGenerationTargetingRequest | Unset = UNSET
    connection: ProxyGenerationConnectionRequest | Unset = UNSET
    session: ProxyGenerationSessionRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.proxy_generation_connection_request import ProxyGenerationConnectionRequest
        from ..models.proxy_generation_session_request import ProxyGenerationSessionRequest
        from ..models.proxy_generation_targeting_request import ProxyGenerationTargetingRequest

        package_id = str(self.package_id)

        quantity = self.quantity

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        targeting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.targeting, Unset):
            targeting = self.targeting.to_dict()

        connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connection, Unset):
            connection = self.connection.to_dict()

        session: dict[str, Any] | Unset = UNSET
        if not isinstance(self.session, Unset):
            session = self.session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package_id": package_id,
                "quantity": quantity,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if targeting is not UNSET:
            field_dict["targeting"] = targeting
        if connection is not UNSET:
            field_dict["connection"] = connection
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proxy_generation_connection_request import ProxyGenerationConnectionRequest
        from ..models.proxy_generation_session_request import ProxyGenerationSessionRequest
        from ..models.proxy_generation_targeting_request import ProxyGenerationTargetingRequest

        d = dict(src_dict)
        package_id = UUID(d.pop("package_id"))

        quantity = d.pop("quantity")

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        _targeting = d.pop("targeting", UNSET)
        targeting: ProxyGenerationTargetingRequest | Unset
        if isinstance(_targeting, Unset):
            targeting = UNSET
        else:
            targeting = ProxyGenerationTargetingRequest.from_dict(_targeting)

        _connection = d.pop("connection", UNSET)
        connection: ProxyGenerationConnectionRequest | Unset
        if isinstance(_connection, Unset):
            connection = UNSET
        else:
            connection = ProxyGenerationConnectionRequest.from_dict(_connection)

        _session = d.pop("session", UNSET)
        session: ProxyGenerationSessionRequest | Unset
        if isinstance(_session, Unset):
            session = UNSET
        else:
            session = ProxyGenerationSessionRequest.from_dict(_session)

        generate_proxy_request = cls(
            package_id=package_id,
            quantity=quantity,
            user_id=user_id,
            targeting=targeting,
            connection=connection,
            session=session,
        )

        generate_proxy_request.additional_properties = d
        return generate_proxy_request

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
