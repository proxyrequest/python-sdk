from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.environment_enum import EnvironmentEnum
from ..models.kyc_provider_enum import KycProviderEnum
from ..models.status_status_enum import StatusStatusEnum
from typing import cast
import datetime


T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    kyc_passed: bool
    status: StatusStatusEnum
    """ * `not_started` - not_started * `pending` - pending * `requires_input` - requires_input * `verified` -
    verified * `rejected` - rejected * `revoked` - revoked """
    source: str
    verified_at: datetime.datetime | None
    revoked_at: datetime.datetime | None
    retry_allowed: bool
    available_providers: list[KycProviderEnum]
    environment: EnvironmentEnum
    """ * `production` - production * `staging` - staging """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kyc_passed = self.kyc_passed

        status = self.status.value

        source = self.source

        verified_at: None | str
        if isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        revoked_at: None | str
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        retry_allowed = self.retry_allowed

        available_providers = []
        for available_providers_item_data in self.available_providers:
            available_providers_item = available_providers_item_data.value
            available_providers.append(available_providers_item)

        environment = self.environment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kyc_passed": kyc_passed,
                "status": status,
                "source": source,
                "verified_at": verified_at,
                "revoked_at": revoked_at,
                "retry_allowed": retry_allowed,
                "available_providers": available_providers,
                "environment": environment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kyc_passed = d.pop("kyc_passed")

        status = StatusStatusEnum(d.pop("status"))

        source = d.pop("source")

        def _parse_verified_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        verified_at = _parse_verified_at(d.pop("verified_at"))

        def _parse_revoked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        retry_allowed = d.pop("retry_allowed")

        available_providers = []
        _available_providers = d.pop("available_providers")
        for available_providers_item_data in _available_providers:
            available_providers_item = KycProviderEnum(available_providers_item_data)

            available_providers.append(available_providers_item)

        environment = EnvironmentEnum(d.pop("environment"))

        status = cls(
            kyc_passed=kyc_passed,
            status=status,
            source=source,
            verified_at=verified_at,
            revoked_at=revoked_at,
            retry_allowed=retry_allowed,
            available_providers=available_providers,
            environment=environment,
        )

        status.additional_properties = d
        return status

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
