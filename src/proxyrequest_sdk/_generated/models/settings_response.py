from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.settings_crypto import SettingsCrypto
    from ..models.settings_gateway import SettingsGateway
    from ..models.settings_referral import SettingsReferral


T = TypeVar("T", bound="SettingsResponse")


@_attrs_define
class SettingsResponse:
    gateways: list[SettingsGateway]
    spent_total: float
    orders_total: int
    orders_active: int
    data_available: int
    data_spent: int
    referrals: SettingsReferral
    crypto: SettingsCrypto
    payment_methods: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.settings_crypto import SettingsCrypto
        from ..models.settings_gateway import SettingsGateway
        from ..models.settings_referral import SettingsReferral

        gateways = []
        for gateways_item_data in self.gateways:
            gateways_item = gateways_item_data.to_dict()
            gateways.append(gateways_item)

        spent_total = self.spent_total

        orders_total = self.orders_total

        orders_active = self.orders_active

        data_available = self.data_available

        data_spent = self.data_spent

        referrals = self.referrals.to_dict()

        crypto = self.crypto.to_dict()

        payment_methods = self.payment_methods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gateways": gateways,
                "spent_total": spent_total,
                "orders_total": orders_total,
                "orders_active": orders_active,
                "data_available": data_available,
                "data_spent": data_spent,
                "referrals": referrals,
                "crypto": crypto,
                "payment_methods": payment_methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.settings_crypto import SettingsCrypto
        from ..models.settings_gateway import SettingsGateway
        from ..models.settings_referral import SettingsReferral

        d = dict(src_dict)
        gateways = []
        _gateways = d.pop("gateways")
        for gateways_item_data in _gateways:
            gateways_item = SettingsGateway.from_dict(gateways_item_data)

            gateways.append(gateways_item)

        spent_total = d.pop("spent_total")

        orders_total = d.pop("orders_total")

        orders_active = d.pop("orders_active")

        data_available = d.pop("data_available")

        data_spent = d.pop("data_spent")

        referrals = SettingsReferral.from_dict(d.pop("referrals"))

        crypto = SettingsCrypto.from_dict(d.pop("crypto"))

        payment_methods = cast(list[str], d.pop("payment_methods"))

        settings_response = cls(
            gateways=gateways,
            spent_total=spent_total,
            orders_total=orders_total,
            orders_active=orders_active,
            data_available=data_available,
            data_spent=data_spent,
            referrals=referrals,
            crypto=crypto,
            payment_methods=payment_methods,
        )

        settings_response.additional_properties = d
        return settings_response

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
