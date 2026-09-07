from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.checkout_status_enum import CheckoutStatusEnum
from ..models.invoice_gateway_enum import InvoiceGatewayEnum
from ..models.invoice_status_enum import InvoiceStatusEnum
from ..models.invoice_type_enum import InvoiceTypeEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.coupon_short import CouponShort
    from ..models.package_short import PackageShort


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    package: None | PackageShort
    country: Country | None
    user_id: UUID
    coupon: CouponShort | None
    payment_amount: int
    payment_currency: str
    fx_market_rate: str
    fx_effective_rate: str
    fx_markup_percent: str
    fx_quoted_at: datetime.datetime | None
    updated: datetime.datetime
    created: datetime.datetime
    id: str | Unset = UNSET
    type_: InvoiceTypeEnum | Unset = UNSET
    """ * `static` - Static * `residential` - Residential * `balance` - Balance """
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
    quantity: int | Unset = UNSET
    """ The number of proxies to assign. """
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
    payment_url: str | Unset = UNSET
    """ The URL for making the payment. Optional field with a maximum length of 500 characters. """
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.country import Country
        from ..models.coupon_short import CouponShort
        from ..models.package_short import PackageShort

        package: dict[str, Any] | None
        if isinstance(self.package, PackageShort):
            package = self.package.to_dict()
        else:
            package = self.package

        country: dict[str, Any] | None
        if isinstance(self.country, Country):
            country = self.country.to_dict()
        else:
            country = self.country

        user_id = str(self.user_id)

        coupon: dict[str, Any] | None
        if isinstance(self.coupon, CouponShort):
            coupon = self.coupon.to_dict()
        else:
            coupon = self.coupon

        payment_amount = self.payment_amount

        payment_currency = self.payment_currency

        fx_market_rate = self.fx_market_rate

        fx_effective_rate = self.fx_effective_rate

        fx_markup_percent = self.fx_markup_percent

        fx_quoted_at: None | str
        if isinstance(self.fx_quoted_at, datetime.datetime):
            fx_quoted_at = self.fx_quoted_at.isoformat()
        else:
            fx_quoted_at = self.fx_quoted_at

        updated = self.updated.isoformat()

        created = self.created.isoformat()

        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        is_one_time = self.is_one_time

        is_payout = self.is_payout

        internal_id = self.internal_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        connection_limit = self.connection_limit

        quantity = self.quantity

        data = self.data

        balance = self.balance

        price_total = self.price_total

        gateway: str | Unset = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.value

        payment_url = self.payment_url

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package": package,
                "country": country,
                "user_id": user_id,
                "coupon": coupon,
                "payment_amount": payment_amount,
                "payment_currency": payment_currency,
                "fx_market_rate": fx_market_rate,
                "fx_effective_rate": fx_effective_rate,
                "fx_markup_percent": fx_markup_percent,
                "fx_quoted_at": fx_quoted_at,
                "updated": updated,
                "created": created,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if data is not UNSET:
            field_dict["data"] = data
        if balance is not UNSET:
            field_dict["balance"] = balance
        if price_total is not UNSET:
            field_dict["price_total"] = price_total
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if payment_url is not UNSET:
            field_dict["payment_url"] = payment_url
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.country import Country
        from ..models.coupon_short import CouponShort
        from ..models.package_short import PackageShort

        d = dict(src_dict)

        def _parse_package(data: object) -> None | PackageShort:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                package_type_1 = PackageShort.from_dict(data)

                return package_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PackageShort, data)

        package = _parse_package(d.pop("package"))

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

        user_id = UUID(d.pop("user_id"))

        def _parse_coupon(data: object) -> CouponShort | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coupon_type_1 = CouponShort.from_dict(data)

                return coupon_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CouponShort | None, data)

        coupon = _parse_coupon(d.pop("coupon"))

        payment_amount = d.pop("payment_amount")

        payment_currency = d.pop("payment_currency")

        fx_market_rate = d.pop("fx_market_rate")

        fx_effective_rate = d.pop("fx_effective_rate")

        fx_markup_percent = d.pop("fx_markup_percent")

        def _parse_fx_quoted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fx_quoted_at_type_0 = datetime.datetime.fromisoformat(data)

                return fx_quoted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        fx_quoted_at = _parse_fx_quoted_at(d.pop("fx_quoted_at"))

        updated = datetime.datetime.fromisoformat(d.pop("updated"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: InvoiceTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InvoiceTypeEnum(_type_)

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

        quantity = d.pop("quantity", UNSET)

        data = d.pop("data", UNSET)

        balance = d.pop("balance", UNSET)

        price_total = d.pop("price_total", UNSET)

        _gateway = d.pop("gateway", UNSET)
        gateway: InvoiceGatewayEnum | Unset
        if isinstance(_gateway, Unset):
            gateway = UNSET
        else:
            gateway = InvoiceGatewayEnum(_gateway)

        payment_url = d.pop("payment_url", UNSET)

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

        invoice = cls(
            package=package,
            country=country,
            user_id=user_id,
            coupon=coupon,
            payment_amount=payment_amount,
            payment_currency=payment_currency,
            fx_market_rate=fx_market_rate,
            fx_effective_rate=fx_effective_rate,
            fx_markup_percent=fx_markup_percent,
            fx_quoted_at=fx_quoted_at,
            updated=updated,
            created=created,
            id=id,
            type_=type_,
            is_one_time=is_one_time,
            is_payout=is_payout,
            internal_id=internal_id,
            status=status,
            description=description,
            connection_limit=connection_limit,
            quantity=quantity,
            data=data,
            balance=balance,
            price_total=price_total,
            gateway=gateway,
            payment_url=payment_url,
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
        )

        invoice.additional_properties = d
        return invoice

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
