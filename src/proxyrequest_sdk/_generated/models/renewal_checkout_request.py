from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.crypto_currency_enum import CryptoCurrencyEnum
from ..models.invoice_create_request_gateway_enum import InvoiceCreateRequestGatewayEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="RenewalCheckoutRequest")


@_attrs_define
class RenewalCheckoutRequest:
    """Invoice transport validation with an explicitly composed application command."""

    gateway: InvoiceCreateRequestGatewayEnum
    """ * `revolut` - revolut * `paypal` - paypal * `coinbase` - coinbase * `cryptomus` - cryptomus * `stripe` -
    stripe * `coingate` - coingate * `wallet` - wallet * `manual` - manual * `whitepay` - whitepay * `wayforpay` -
    wayforpay * `usegateway` - usegateway * `binance` - binance * `anymoney` - anymoney * `coinpayments` -
    coinpayments * `checkoutcom` - checkoutcom * `nowpayments` - nowpayments * `btcpay` - btcpay * `braintree` -
    braintree * `monobank` - monobank * `liqpay` - liqpay * `iyzico` - iyzico * `paytr` - paytr * `payu` - payu *
    `tpay` - tpay * `przelewy24` - przelewy24 * `gopay` - gopay * `comgate` - comgate * `monei` - monei * `redsys` -
    redsys * `payplug` - payplug * `mollie` - mollie * `unzer` - unzer * `payone` - payone * `nexi_xpay` - nexi_xpay
    * `halyk_epay` - halyk_epay * `kaspi_pay` - kaspi_pay * `vipps_mobilepay` - vipps_mobilepay * `paytrail` -
    paytrail * `crypto` - crypto * `credit_card` - credit_card """
    country_code: str | Unset = UNSET
    company_vat_number: str | Unset = UNSET
    company_name: str | Unset = UNSET
    company_registration_number: str | Unset = UNSET
    crypto_currency: CryptoCurrencyEnum | Unset = UNSET
    """ * `btc` - btc * `eth` - eth * `usdt` - usdt """
    payment_currency: str | Unset = UNSET
    coupon_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway.value

        country_code = self.country_code

        company_vat_number = self.company_vat_number

        company_name = self.company_name

        company_registration_number = self.company_registration_number

        crypto_currency: str | Unset = UNSET
        if not isinstance(self.crypto_currency, Unset):
            crypto_currency = self.crypto_currency.value

        payment_currency = self.payment_currency

        coupon_code = self.coupon_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gateway": gateway,
            }
        )
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if company_vat_number is not UNSET:
            field_dict["company_vat_number"] = company_vat_number
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_registration_number is not UNSET:
            field_dict["company_registration_number"] = company_registration_number
        if crypto_currency is not UNSET:
            field_dict["crypto_currency"] = crypto_currency
        if payment_currency is not UNSET:
            field_dict["payment_currency"] = payment_currency
        if coupon_code is not UNSET:
            field_dict["coupon_code"] = coupon_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gateway = InvoiceCreateRequestGatewayEnum(d.pop("gateway"))

        country_code = d.pop("country_code", UNSET)

        company_vat_number = d.pop("company_vat_number", UNSET)

        company_name = d.pop("company_name", UNSET)

        company_registration_number = d.pop("company_registration_number", UNSET)

        _crypto_currency = d.pop("crypto_currency", UNSET)
        crypto_currency: CryptoCurrencyEnum | Unset
        if isinstance(_crypto_currency, Unset):
            crypto_currency = UNSET
        else:
            crypto_currency = CryptoCurrencyEnum(_crypto_currency)

        payment_currency = d.pop("payment_currency", UNSET)

        coupon_code = d.pop("coupon_code", UNSET)

        renewal_checkout_request = cls(
            gateway=gateway,
            country_code=country_code,
            company_vat_number=company_vat_number,
            company_name=company_name,
            company_registration_number=company_registration_number,
            crypto_currency=crypto_currency,
            payment_currency=payment_currency,
            coupon_code=coupon_code,
        )

        renewal_checkout_request.additional_properties = d
        return renewal_checkout_request

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
