from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.patched_user_update_request_meta import PatchedUserUpdateRequestMeta


T = TypeVar("T", bound="PatchedUserUpdateRequest")


@_attrs_define
class PatchedUserUpdateRequest:
    """Optional fields accepted when updating part of an existing customer account."""

    email: str | Unset = UNSET
    """ User's email address. Must be unique across the system. """
    first_name: str | Unset = UNSET
    """ User's first name. """
    last_name: str | Unset = UNSET
    """ User's last name. """
    country: str | Unset = UNSET
    """ User's country of residence. """
    state: str | Unset = UNSET
    """ User's state or province. """
    city: str | Unset = UNSET
    """ User's city. """
    address: str | Unset = UNSET
    """ User's street address. """
    zip_: str | Unset = UNSET
    """ User's postal/ZIP code. """
    company_name: str | Unset = UNSET
    """ Name of the user's company. """
    company_country: str | Unset = UNSET
    """ Country where the company is located. """
    company_city: str | Unset = UNSET
    """ City where the company is located. """
    company_address: str | Unset = UNSET
    """ Company's street address. """
    company_postal_code: str | Unset = UNSET
    """ Company's postal code. """
    company_vat_number: str | Unset = UNSET
    """ Company's VAT number. """
    is_reseller: bool | Unset = UNSET
    """ Whether the user has reseller privileges. Only superusers can modify. """
    blocked_domains: list[str] | Unset = UNSET
    """ List of domains to block for this user. """
    allowed_ips: list[str] | Unset = UNSET
    """ List of source IP addresses allowed for this user. The maximum list size is configured per deployment. """
    connection_limit: int | Unset = UNSET
    """ Maximum number of concurrent connections allowed for the user. """
    new_password: str | Unset = UNSET
    """ New password for the user. Must be 8-128 characters long. """
    meta: PatchedUserUpdateRequestMeta | Unset = UNSET
    """ Additional metadata for the user. Maximum 50 fields. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patched_user_update_request_meta import PatchedUserUpdateRequestMeta

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        country = self.country

        state = self.state

        city = self.city

        address = self.address

        zip_ = self.zip_

        company_name = self.company_name

        company_country = self.company_country

        company_city = self.company_city

        company_address = self.company_address

        company_postal_code = self.company_postal_code

        company_vat_number = self.company_vat_number

        is_reseller = self.is_reseller

        blocked_domains: list[str] | Unset = UNSET
        if not isinstance(self.blocked_domains, Unset):
            blocked_domains = self.blocked_domains

        allowed_ips: list[str] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = self.allowed_ips

        connection_limit = self.connection_limit

        new_password = self.new_password

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
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
        if company_country is not UNSET:
            field_dict["company_country"] = company_country
        if company_city is not UNSET:
            field_dict["company_city"] = company_city
        if company_address is not UNSET:
            field_dict["company_address"] = company_address
        if company_postal_code is not UNSET:
            field_dict["company_postal_code"] = company_postal_code
        if company_vat_number is not UNSET:
            field_dict["company_vat_number"] = company_vat_number
        if is_reseller is not UNSET:
            field_dict["is_reseller"] = is_reseller
        if blocked_domains is not UNSET:
            field_dict["blocked_domains"] = blocked_domains
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips
        if connection_limit is not UNSET:
            field_dict["connection_limit"] = connection_limit
        if new_password is not UNSET:
            field_dict["new_password"] = new_password
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_user_update_request_meta import PatchedUserUpdateRequestMeta

        d = dict(src_dict)
        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        country = d.pop("country", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        address = d.pop("address", UNSET)

        zip_ = d.pop("zip", UNSET)

        company_name = d.pop("company_name", UNSET)

        company_country = d.pop("company_country", UNSET)

        company_city = d.pop("company_city", UNSET)

        company_address = d.pop("company_address", UNSET)

        company_postal_code = d.pop("company_postal_code", UNSET)

        company_vat_number = d.pop("company_vat_number", UNSET)

        is_reseller = d.pop("is_reseller", UNSET)

        blocked_domains = cast(list[str], d.pop("blocked_domains", UNSET))

        allowed_ips = cast(list[str], d.pop("allowed_ips", UNSET))

        connection_limit = d.pop("connection_limit", UNSET)

        new_password = d.pop("new_password", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: PatchedUserUpdateRequestMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = PatchedUserUpdateRequestMeta.from_dict(_meta)

        patched_user_update_request = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            country=country,
            state=state,
            city=city,
            address=address,
            zip_=zip_,
            company_name=company_name,
            company_country=company_country,
            company_city=company_city,
            company_address=company_address,
            company_postal_code=company_postal_code,
            company_vat_number=company_vat_number,
            is_reseller=is_reseller,
            blocked_domains=blocked_domains,
            allowed_ips=allowed_ips,
            connection_limit=connection_limit,
            new_password=new_password,
            meta=meta,
        )

        patched_user_update_request.additional_properties = d
        return patched_user_update_request

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
