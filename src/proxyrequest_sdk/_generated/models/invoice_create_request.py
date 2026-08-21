from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_create_request_gateway_enum import InvoiceCreateRequestGatewayEnum
from ..types import UNSET, Unset
from uuid import UUID


T = TypeVar("T", bound="InvoiceCreateRequest")


@_attrs_define
class InvoiceCreateRequest:
    gateway: InvoiceCreateRequestGatewayEnum
    """ * `crypto` - crypto * `wallet` - wallet * `manual` - manual * `stripe` - stripe """
    package_id: UUID | Unset = UNSET
    """ Package to purchase. Required for package purchases. """
    user_id: UUID | Unset = UNSET
    """ Managed sub-user that should receive the purchase. """
    crypto_currency: str | Unset = UNSET
    coupon_code: str | Unset = UNSET
    country_code: str | Unset = UNSET
    data: int | Unset = UNSET
    """ Residential proxy data to purchase, in bytes. """
    quantity: int | Unset = UNSET
    """ Number of static proxies to purchase. """
    amount: int | Unset = UNSET
    """ Account balance amount to purchase, in the smallest currency unit. """
    connection_limit: int | Unset = UNSET
    expires: int | Unset = UNSET
    """ Optional expiration as a Unix timestamp in seconds. """
    company_name: str | Unset = UNSET
    company_registration_number: str | Unset = UNSET
    company_vat_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway.value

        package_id: str | Unset = UNSET
        if not isinstance(self.package_id, Unset):
            package_id = str(self.package_id)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        crypto_currency = self.crypto_currency

        coupon_code = self.coupon_code

        country_code = self.country_code

        data = self.data

        quantity = self.quantity

        amount = self.amount

        connection_limit = self.connection_limit

        expires = self.expires

        company_name = self.company_name

        company_registration_number = self.company_registration_number

        company_vat_number = self.company_vat_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gateway": gateway,
            }
        )
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if crypto_currency is not UNSET:
            field_dict["crypto_currency"] = crypto_currency
        if coupon_code is not UNSET:
            field_dict["coupon_code"] = coupon_code
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if data is not UNSET:
            field_dict["data"] = data
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if amount is not UNSET:
            field_dict["amount"] = amount
        if connection_limit is not UNSET:
            field_dict["connection_limit"] = connection_limit
        if expires is not UNSET:
            field_dict["expires"] = expires
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_registration_number is not UNSET:
            field_dict["company_registration_number"] = company_registration_number
        if company_vat_number is not UNSET:
            field_dict["company_vat_number"] = company_vat_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gateway = InvoiceCreateRequestGatewayEnum(d.pop("gateway"))

        _package_id = d.pop("package_id", UNSET)
        package_id: UUID | Unset
        if isinstance(_package_id, Unset):
            package_id = UNSET
        else:
            package_id = UUID(_package_id)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        crypto_currency = d.pop("crypto_currency", UNSET)

        coupon_code = d.pop("coupon_code", UNSET)

        country_code = d.pop("country_code", UNSET)

        data = d.pop("data", UNSET)

        quantity = d.pop("quantity", UNSET)

        amount = d.pop("amount", UNSET)

        connection_limit = d.pop("connection_limit", UNSET)

        expires = d.pop("expires", UNSET)

        company_name = d.pop("company_name", UNSET)

        company_registration_number = d.pop("company_registration_number", UNSET)

        company_vat_number = d.pop("company_vat_number", UNSET)

        invoice_create_request = cls(
            gateway=gateway,
            package_id=package_id,
            user_id=user_id,
            crypto_currency=crypto_currency,
            coupon_code=coupon_code,
            country_code=country_code,
            data=data,
            quantity=quantity,
            amount=amount,
            connection_limit=connection_limit,
            expires=expires,
            company_name=company_name,
            company_registration_number=company_registration_number,
            company_vat_number=company_vat_number,
        )

        invoice_create_request.additional_properties = d
        return invoice_create_request

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
