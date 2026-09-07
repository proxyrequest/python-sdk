from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="PaymentGateway")


@_attrs_define
class PaymentGateway:
    code: str
    name: str
    kind: str
    supported_currencies: list[str]
    supported_crypto_currencies: list[str]
    requires_crypto_currency: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        kind = self.kind

        supported_currencies = self.supported_currencies

        supported_crypto_currencies = self.supported_crypto_currencies

        requires_crypto_currency = self.requires_crypto_currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
                "kind": kind,
                "supported_currencies": supported_currencies,
                "supported_crypto_currencies": supported_crypto_currencies,
                "requires_crypto_currency": requires_crypto_currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        kind = d.pop("kind")

        supported_currencies = cast(list[str], d.pop("supported_currencies"))

        supported_crypto_currencies = cast(list[str], d.pop("supported_crypto_currencies"))

        requires_crypto_currency = d.pop("requires_crypto_currency")

        payment_gateway = cls(
            code=code,
            name=name,
            kind=kind,
            supported_currencies=supported_currencies,
            supported_crypto_currencies=supported_crypto_currencies,
            requires_crypto_currency=requires_crypto_currency,
        )

        payment_gateway.additional_properties = d
        return payment_gateway

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
