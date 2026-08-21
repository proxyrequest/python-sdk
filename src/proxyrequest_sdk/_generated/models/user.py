from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.language_enum import LanguageEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.user_coupons_item import UserCouponsItem
    from ..models.user_currency import UserCurrency


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """Customer account with contact details, security settings, package data, referral information, and managed sub-users
    visible to the caller.

    """

    id: UUID
    username: str
    """ Value must contain only letters, numbers, and underscores. It must not start or end with an underscore. """
    email: str
    date_joined: datetime.datetime
    date_joined_ts: int
    """ Timestamp of when the user joined """
    allowed_ips: list[str]
    """ List of IP addresses allowed for this user """
    blocked_domains: list[str]
    """ List of domains blocked for this user """
    parent_id: str
    """ ID of the parent user (for sub-accounts) """
    sub_users: int
    """ Number of sub-users managed by this reseller """
    referrals: int
    """ Number of users referred by this user """
    referral_code: str
    referral_data_earned: int
    referral_data_pending: int
    referral_balance_pending: int
    referral_balance_earned: int
    currency: UserCurrency
    """ Currency information for the user's transactions """
    coupons: list[UserCouponsItem]
    """ Available coupons for this user """
    data: int | None
    """ Available data allowance for the user """
    data_spent: int | None
    """ Amount of data consumed by the user """
    data_updated: datetime.datetime | None
    """ Last update timestamp for user's data """
    proxy_password: None | str
    """ Proxy authentication password """
    proxy_password_reset: datetime.datetime | None
    """ Last proxy password reset timestamp """
    is_reseller: bool | Unset = UNSET
    """ Reseller can create sub-users and manage their data. """
    is_marketer: bool | Unset = UNSET
    """ Marketer can manage marketing campaigns and view analytics. """
    is_superuser: bool | Unset = UNSET
    """ Designates that this user has all permissions without explicitly assigning them. """
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    balance: int | Unset = UNSET
    language: LanguageEnum | Unset = UNSET
    """ * `en` - EN * `de` - DE * `fr` - FR * `it` - IT * `ru` - RU """
    country: str | Unset = UNSET
    state: str | Unset = UNSET
    city: str | Unset = UNSET
    address: str | Unset = UNSET
    zip_: str | Unset = UNSET
    company_name: str | Unset = UNSET
    company_address: str | Unset = UNSET
    company_city: str | Unset = UNSET
    company_postal_code: str | Unset = UNSET
    company_country: str | Unset = UNSET
    company_vat_number: str | Unset = UNSET
    connection_limit: int | Unset = UNSET
    """ The maximum number of concurrent connections allowed for this package. """
    referral_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_coupons_item import UserCouponsItem
        from ..models.user_currency import UserCurrency

        id = str(self.id)

        username = self.username

        email = self.email

        date_joined = self.date_joined.isoformat()

        date_joined_ts = self.date_joined_ts

        allowed_ips = self.allowed_ips

        blocked_domains = self.blocked_domains

        parent_id = self.parent_id

        sub_users = self.sub_users

        referrals = self.referrals

        referral_code = self.referral_code

        referral_data_earned = self.referral_data_earned

        referral_data_pending = self.referral_data_pending

        referral_balance_pending = self.referral_balance_pending

        referral_balance_earned = self.referral_balance_earned

        currency = self.currency.to_dict()

        coupons = []
        for coupons_item_data in self.coupons:
            coupons_item = coupons_item_data.to_dict()
            coupons.append(coupons_item)

        data: int | None
        data = self.data

        data_spent: int | None
        data_spent = self.data_spent

        data_updated: None | str
        if isinstance(self.data_updated, datetime.datetime):
            data_updated = self.data_updated.isoformat()
        else:
            data_updated = self.data_updated

        proxy_password: None | str
        proxy_password = self.proxy_password

        proxy_password_reset: None | str
        if isinstance(self.proxy_password_reset, datetime.datetime):
            proxy_password_reset = self.proxy_password_reset.isoformat()
        else:
            proxy_password_reset = self.proxy_password_reset

        is_reseller = self.is_reseller

        is_marketer = self.is_marketer

        is_superuser = self.is_superuser

        first_name = self.first_name

        last_name = self.last_name

        balance = self.balance

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        country = self.country

        state = self.state

        city = self.city

        address = self.address

        zip_ = self.zip_

        company_name = self.company_name

        company_address = self.company_address

        company_city = self.company_city

        company_postal_code = self.company_postal_code

        company_country = self.company_country

        company_vat_number = self.company_vat_number

        connection_limit = self.connection_limit

        referral_id = self.referral_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "email": email,
                "date_joined": date_joined,
                "date_joined_ts": date_joined_ts,
                "allowed_ips": allowed_ips,
                "blocked_domains": blocked_domains,
                "parent_id": parent_id,
                "sub_users": sub_users,
                "referrals": referrals,
                "referral_code": referral_code,
                "referral_data_earned": referral_data_earned,
                "referral_data_pending": referral_data_pending,
                "referral_balance_pending": referral_balance_pending,
                "referral_balance_earned": referral_balance_earned,
                "currency": currency,
                "coupons": coupons,
                "data": data,
                "data_spent": data_spent,
                "data_updated": data_updated,
                "proxy_password": proxy_password,
                "proxy_password_reset": proxy_password_reset,
            }
        )
        if is_reseller is not UNSET:
            field_dict["is_reseller"] = is_reseller
        if is_marketer is not UNSET:
            field_dict["is_marketer"] = is_marketer
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if balance is not UNSET:
            field_dict["balance"] = balance
        if language is not UNSET:
            field_dict["language"] = language
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if address is not UNSET:
            field_dict["address"] = address
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_address is not UNSET:
            field_dict["company_address"] = company_address
        if company_city is not UNSET:
            field_dict["company_city"] = company_city
        if company_postal_code is not UNSET:
            field_dict["company_postal_code"] = company_postal_code
        if company_country is not UNSET:
            field_dict["company_country"] = company_country
        if company_vat_number is not UNSET:
            field_dict["company_vat_number"] = company_vat_number
        if connection_limit is not UNSET:
            field_dict["connection_limit"] = connection_limit
        if referral_id is not UNSET:
            field_dict["referral_id"] = referral_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_coupons_item import UserCouponsItem
        from ..models.user_currency import UserCurrency

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        username = d.pop("username")

        email = d.pop("email")

        date_joined = datetime.datetime.fromisoformat(d.pop("date_joined"))

        date_joined_ts = d.pop("date_joined_ts")

        allowed_ips = cast(list[str], d.pop("allowed_ips"))

        blocked_domains = cast(list[str], d.pop("blocked_domains"))

        parent_id = d.pop("parent_id")

        sub_users = d.pop("sub_users")

        referrals = d.pop("referrals")

        referral_code = d.pop("referral_code")

        referral_data_earned = d.pop("referral_data_earned")

        referral_data_pending = d.pop("referral_data_pending")

        referral_balance_pending = d.pop("referral_balance_pending")

        referral_balance_earned = d.pop("referral_balance_earned")

        currency = UserCurrency.from_dict(d.pop("currency"))

        coupons = []
        _coupons = d.pop("coupons")
        for coupons_item_data in _coupons:
            coupons_item = UserCouponsItem.from_dict(coupons_item_data)

            coupons.append(coupons_item)

        def _parse_data(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        data = _parse_data(d.pop("data"))

        def _parse_data_spent(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        data_spent = _parse_data_spent(d.pop("data_spent"))

        def _parse_data_updated(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_updated_type_0 = datetime.datetime.fromisoformat(data)

                return data_updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        data_updated = _parse_data_updated(d.pop("data_updated"))

        def _parse_proxy_password(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        proxy_password = _parse_proxy_password(d.pop("proxy_password"))

        def _parse_proxy_password_reset(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_password_reset_type_0 = datetime.datetime.fromisoformat(data)

                return proxy_password_reset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        proxy_password_reset = _parse_proxy_password_reset(d.pop("proxy_password_reset"))

        is_reseller = d.pop("is_reseller", UNSET)

        is_marketer = d.pop("is_marketer", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        balance = d.pop("balance", UNSET)

        _language = d.pop("language", UNSET)
        language: LanguageEnum | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = LanguageEnum(_language)

        country = d.pop("country", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        address = d.pop("address", UNSET)

        zip_ = d.pop("zip", UNSET)

        company_name = d.pop("company_name", UNSET)

        company_address = d.pop("company_address", UNSET)

        company_city = d.pop("company_city", UNSET)

        company_postal_code = d.pop("company_postal_code", UNSET)

        company_country = d.pop("company_country", UNSET)

        company_vat_number = d.pop("company_vat_number", UNSET)

        connection_limit = d.pop("connection_limit", UNSET)

        referral_id = d.pop("referral_id", UNSET)

        user = cls(
            id=id,
            username=username,
            email=email,
            date_joined=date_joined,
            date_joined_ts=date_joined_ts,
            allowed_ips=allowed_ips,
            blocked_domains=blocked_domains,
            parent_id=parent_id,
            sub_users=sub_users,
            referrals=referrals,
            referral_code=referral_code,
            referral_data_earned=referral_data_earned,
            referral_data_pending=referral_data_pending,
            referral_balance_pending=referral_balance_pending,
            referral_balance_earned=referral_balance_earned,
            currency=currency,
            coupons=coupons,
            data=data,
            data_spent=data_spent,
            data_updated=data_updated,
            proxy_password=proxy_password,
            proxy_password_reset=proxy_password_reset,
            is_reseller=is_reseller,
            is_marketer=is_marketer,
            is_superuser=is_superuser,
            first_name=first_name,
            last_name=last_name,
            balance=balance,
            language=language,
            country=country,
            state=state,
            city=city,
            address=address,
            zip_=zip_,
            company_name=company_name,
            company_address=company_address,
            company_city=company_city,
            company_postal_code=company_postal_code,
            company_country=company_country,
            company_vat_number=company_vat_number,
            connection_limit=connection_limit,
            referral_id=referral_id,
        )

        user.additional_properties = d
        return user

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
