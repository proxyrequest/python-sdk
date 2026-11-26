from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.channel_enum import ChannelEnum
from ..models.method_enum import MethodEnum
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.login_history_client_hints import LoginHistoryClientHints
    from ..models.login_history_location import LoginHistoryLocation


T = TypeVar("T", bound="LoginHistory")


@_attrs_define
class LoginHistory:
    id: int
    user: UUID
    authenticated_at: datetime.datetime
    method: MethodEnum
    """ * `password` - Password * `google` - Google * `registration` - Registration * `unknown` - Unknown """
    channel: ChannelEnum
    """ * `public_api` - Public API * `admin_panel` - Admin panel * `unknown` - Unknown """
    mfa_verified: bool
    ip_address: None | str
    ip_source: str
    user_agent: str
    browser: str
    operating_system: str
    device: str
    language: str
    client_hints: LoginHistoryClientHints
    location: LoginHistoryLocation
    request_host: str
    request_path: str
    request_method: str
    request_id: str
    cf_ray: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.login_history_client_hints import LoginHistoryClientHints
        from ..models.login_history_location import LoginHistoryLocation

        id = self.id

        user = str(self.user)

        authenticated_at = self.authenticated_at.isoformat()

        method = self.method.value

        channel = self.channel.value

        mfa_verified = self.mfa_verified

        ip_address: None | str
        ip_address = self.ip_address

        ip_source = self.ip_source

        user_agent = self.user_agent

        browser = self.browser

        operating_system = self.operating_system

        device = self.device

        language = self.language

        client_hints = self.client_hints.to_dict()

        location = self.location.to_dict()

        request_host = self.request_host

        request_path = self.request_path

        request_method = self.request_method

        request_id = self.request_id

        cf_ray = self.cf_ray

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
                "authenticated_at": authenticated_at,
                "method": method,
                "channel": channel,
                "mfa_verified": mfa_verified,
                "ip_address": ip_address,
                "ip_source": ip_source,
                "user_agent": user_agent,
                "browser": browser,
                "operating_system": operating_system,
                "device": device,
                "language": language,
                "client_hints": client_hints,
                "location": location,
                "request_host": request_host,
                "request_path": request_path,
                "request_method": request_method,
                "request_id": request_id,
                "cf_ray": cf_ray,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_history_client_hints import LoginHistoryClientHints
        from ..models.login_history_location import LoginHistoryLocation

        d = dict(src_dict)
        id = d.pop("id")

        user = UUID(d.pop("user"))

        authenticated_at = datetime.datetime.fromisoformat(d.pop("authenticated_at"))

        method = MethodEnum(d.pop("method"))

        channel = ChannelEnum(d.pop("channel"))

        mfa_verified = d.pop("mfa_verified")

        def _parse_ip_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address = _parse_ip_address(d.pop("ip_address"))

        ip_source = d.pop("ip_source")

        user_agent = d.pop("user_agent")

        browser = d.pop("browser")

        operating_system = d.pop("operating_system")

        device = d.pop("device")

        language = d.pop("language")

        client_hints = LoginHistoryClientHints.from_dict(d.pop("client_hints"))

        location = LoginHistoryLocation.from_dict(d.pop("location"))

        request_host = d.pop("request_host")

        request_path = d.pop("request_path")

        request_method = d.pop("request_method")

        request_id = d.pop("request_id")

        cf_ray = d.pop("cf_ray")

        login_history = cls(
            id=id,
            user=user,
            authenticated_at=authenticated_at,
            method=method,
            channel=channel,
            mfa_verified=mfa_verified,
            ip_address=ip_address,
            ip_source=ip_source,
            user_agent=user_agent,
            browser=browser,
            operating_system=operating_system,
            device=device,
            language=language,
            client_hints=client_hints,
            location=location,
            request_host=request_host,
            request_path=request_path,
            request_method=request_method,
            request_id=request_id,
            cf_ray=cf_ray,
        )

        login_history.additional_properties = d
        return login_history

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
