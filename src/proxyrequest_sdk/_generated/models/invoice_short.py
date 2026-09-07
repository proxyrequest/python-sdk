from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.checkout_status_enum import CheckoutStatusEnum
from ..models.invoice_gateway_enum import InvoiceGatewayEnum
from ..models.invoice_status_enum import InvoiceStatusEnum
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.coupon import Coupon


T = TypeVar("T", bound="InvoiceShort")


@_attrs_define
class InvoiceShort:
    coupon: Coupon | None
    country: Country | None
    updated: datetime.datetime
    created: datetime.datetime
    id: str | Unset = UNSET
    is_one_time: bool | Unset = UNSET
    """ Indicates whether this invoice is for a one-time purchase. Default is False, meaning it is a recurring
    invoice. """
    is_payout: bool | Unset = UNSET
    """ Indicates whether this invoice is a payout to the marketer. Default is False. """
    internal_id: str | Unset = UNSET
    """ A unique identifier for the invoice, generated automatically. """
    status: InvoiceStatusEnum | Unset = UNSET
    """ * `pending` - Pending * `paid` - Paid * `unpaid` - Unpaid * `error` - Error """
    description: str | Unset = UNSET
    """ A description of the invoice. This field is optional and can be left blank. """
    connection_limit: int | Unset = UNSET
    """ The maximum number of concurrent connections allowed for this package. """
    data: int | Unset = UNSET
    """ The amount of data in bytes. """
    balance: int | Unset = UNSET
    """ The balance to top up for the user. Must be zero or positive. """
    price_total: int | Unset = UNSET
    """ The total price of the invoice, including any discounts. Must be at least 1 cent. """
    gateway: InvoiceGatewayEnum | Unset = UNSET
    """ * `coinbase` - Coinbase * `cryptomus` - Cryptomus * `stripe` - Stripe * `coingate` - Coingate * `wallet` -
    Wallet * `manual` - Manual * `whitepay` - Whitepay * `wayforpay` - WayForPay * `usegateway` - UseGateway *
    `binance` - Binance Pay * `anymoney` - Any.Money * `coinpayments` - CoinPayments * `checkoutcom` - Checkout.com
    * `nowpayments` - NOWPayments * `btcpay` - BTCPay Server * `braintree` - Braintree * `monobank` - monobank *
    `liqpay` - LiqPay * `iyzico` - iyzico * `paytr` - PayTR * `payu` - PayU * `tpay` - Tpay * `przelewy24` -
    Przelewy24 * `gopay` - GoPay * `comgate` - Comgate * `monei` - MONEI * `redsys` - Redsys * `payplug` - PayPlug *
    `mollie` - Mollie * `unzer` - Unzer * `payone` - PAYONE * `nexi_xpay` - Nexi XPay * `halyk_epay` - Halyk ePay *
    `kaspi_pay` - Kaspi Pay * `vipps_mobilepay` - Vipps MobilePay * `paytrail` - Paytrail """
    currency: str | Unset = UNSET
    """ ISO 4217 currency captured when the invoice is created. """
    provider_checkout_id: str | Unset = UNSET
    """ Provider-side hosted checkout identifier used for reconciliation. """
    provider_payment_id: str | Unset = UNSET
    """ Provider-side payment or transaction identifier used for reconciliation. """
    checkout_status: CheckoutStatusEnum | Unset = UNSET
    """ * `not_required` - Not required * `initializing` - Initializing * `ready` - Ready * `failed` - Failed """
    vat: float | Unset = UNSET
    """ The VAT percentage applied to the invoice. Must be between 0 and 100. """
    company_name: str | Unset = UNSET
    company_address: str | Unset = UNSET
    company_city: str | Unset = UNSET
    company_postal_code: str | Unset = UNSET
    company_registration_number: str | Unset = UNSET
    company_vat_number: str | Unset = UNSET
    paid: datetime.datetime | None | Unset = UNSET
    """ The date and time when the invoice was paid. """
    expires: datetime.datetime | None | Unset = UNSET
    """ The date and time when the invoice expires. If not set, the invoice does not expire. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.country import Country
        from ..models.coupon import Coupon

        coupon: dict[str, Any] | None
        if isinstance(self.coupon, Coupon):
            coupon = self.coupon.to_dict()
        else:
            coupon = self.coupon

        country: dict[str, Any] | None
        if isinstance(self.country, Country):
            country = self.country.to_dict()
        else:
            country = self.country

        updated = self.updated.isoformat()

        created = self.created.isoformat()

        id = self.id

        is_one_time = self.is_one_time

        is_payout = self.is_payout

        internal_id = self.internal_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        connection_limit = self.connection_limit

        data = self.data

        balance = self.balance

        price_total = self.price_total

        gateway: str | Unset = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.value

        currency = self.currency

        provider_checkout_id = self.provider_checkout_id

        provider_payment_id = self.provider_payment_id

        checkout_status: str | Unset = UNSET
        if not isinstance(self.checkout_status, Unset):
            checkout_status = self.checkout_status.value

        vat = self.vat

        company_name = self.company_name

        company_address = self.company_address

        company_city = self.company_city

        company_postal_code = self.company_postal_code

        company_registration_number = self.company_registration_number

        company_vat_number = self.company_vat_number

        paid: None | str | Unset
        if isinstance(self.paid, Unset):
            paid = UNSET
        elif isinstance(self.paid, datetime.datetime):
            paid = self.paid.isoformat()
        else:
            paid = self.paid

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coupon": coupon,
                "country": country,
                "updated": updated,
                "created": created,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_one_time is not UNSET:
            field_dict["is_one_time"] = is_one_time
        if is_payout is not UNSET:
            field_dict["is_payout"] = is_payout
        if internal_id is not UNSET:
            field_dict["internal_id"] = internal_id
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if connection_limit is not UNSET:
            field_dict["connection_limit"] = connection_limit
        if data is not UNSET:
            field_dict["data"] = data
        if balance is not UNSET:
            field_dict["balance"] = balance
        if price_total is not UNSET:
            field_dict["price_total"] = price_total
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if currency is not UNSET:
            field_dict["currency"] = currency
        if provider_checkout_id is not UNSET:
            field_dict["provider_checkout_id"] = provider_checkout_id
        if provider_payment_id is not UNSET:
            field_dict["provider_payment_id"] = provider_payment_id
        if checkout_status is not UNSET:
            field_dict["checkout_status"] = checkout_status
        if vat is not UNSET:
            field_dict["vat"] = vat
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_address is not UNSET:
            field_dict["company_address"] = company_address
        if company_city is not UNSET:
            field_dict["company_city"] = company_city
        if company_postal_code is not UNSET:
            field_dict["company_postal_code"] = company_postal_code
        if company_registration_number is not UNSET:
            field_dict["company_registration_number"] = company_registration_number
        if company_vat_number is not UNSET:
            field_dict["company_vat_number"] = company_vat_number
        if paid is not UNSET:
            field_dict["paid"] = paid
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.country import Country
        from ..models.coupon import Coupon

        d = dict(src_dict)

        def _parse_coupon(data: object) -> Coupon | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coupon_type_1 = Coupon.from_dict(data)

                return coupon_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Coupon | None, data)

        coupon = _parse_coupon(d.pop("coupon"))

        def _parse_country(data: object) -> Country | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_type_1 = Country.from_dict(data)

                return country_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Country | None, data)

        country = _parse_country(d.pop("country"))

        updated = datetime.datetime.fromisoformat(d.pop("updated"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = d.pop("id", UNSET)

        is_one_time = d.pop("is_one_time", UNSET)

        is_payout = d.pop("is_payout", UNSET)

        internal_id = d.pop("internal_id", UNSET)

        _status = d.pop("status", UNSET)
        status: InvoiceStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvoiceStatusEnum(_status)

        description = d.pop("description", UNSET)

        connection_limit = d.pop("connection_limit", UNSET)

        data = d.pop("data", UNSET)

        balance = d.pop("balance", UNSET)

        price_total = d.pop("price_total", UNSET)

        _gateway = d.pop("gateway", UNSET)
        gateway: InvoiceGatewayEnum | Unset
        if isinstance(_gateway, Unset):
            gateway = UNSET
        else:
            gateway = InvoiceGatewayEnum(_gateway)

        currency = d.pop("currency", UNSET)

        provider_checkout_id = d.pop("provider_checkout_id", UNSET)

        provider_payment_id = d.pop("provider_payment_id", UNSET)

        _checkout_status = d.pop("checkout_status", UNSET)
        checkout_status: CheckoutStatusEnum | Unset
        if isinstance(_checkout_status, Unset):
            checkout_status = UNSET
        else:
            checkout_status = CheckoutStatusEnum(_checkout_status)

        vat = d.pop("vat", UNSET)

        company_name = d.pop("company_name", UNSET)

        company_address = d.pop("company_address", UNSET)

        company_city = d.pop("company_city", UNSET)

        company_postal_code = d.pop("company_postal_code", UNSET)

        company_registration_number = d.pop("company_registration_number", UNSET)

        company_vat_number = d.pop("company_vat_number", UNSET)

        def _parse_paid(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_type_0 = datetime.datetime.fromisoformat(data)

                return paid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paid = _parse_paid(d.pop("paid", UNSET))

        def _parse_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = datetime.datetime.fromisoformat(data)

                return expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))

        invoice_short = cls(
            coupon=coupon,
            country=country,
            updated=updated,
            created=created,
            id=id,
            is_one_time=is_one_time,
            is_payout=is_payout,
            internal_id=internal_id,
            status=status,
            description=description,
            connection_limit=connection_limit,
            data=data,
            balance=balance,
            price_total=price_total,
            gateway=gateway,
            currency=currency,
            provider_checkout_id=provider_checkout_id,
            provider_payment_id=provider_payment_id,
            checkout_status=checkout_status,
            vat=vat,
            company_name=company_name,
            company_address=company_address,
            company_city=company_city,
            company_postal_code=company_postal_code,
            company_registration_number=company_registration_number,
            company_vat_number=company_vat_number,
            paid=paid,
            expires=expires,
        )

        invoice_short.additional_properties = d
        return invoice_short

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
