from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="PatchedProfileUpdateRequest")


@_attrs_define
class PatchedProfileUpdateRequest:
    """for updating user profile information with comprehensive validation. Handles personal profile data, company
    information, security settings, and password changes. All fields are optional, but at least one field must be
    provided for the update to be valid. Includes validation for domain patterns with support for wildcards
    (*.example.com) and subdomains.

    """

    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    country: str | Unset = UNSET
    state: str | Unset = UNSET
    city: str | Unset = UNSET
    address: str | Unset = UNSET
    zip_: str | Unset = UNSET
    company_name: str | Unset = UNSET
    company_country: str | Unset = UNSET
    company_city: str | Unset = UNSET
    company_address: str | Unset = UNSET
    company_postal_code: str | Unset = UNSET
    company_vat_number: str | Unset = UNSET
    blocked_domains: list[str] | Unset = UNSET
    allowed_ips: list[str] | Unset = UNSET
    new_password: str | Unset = UNSET
    old_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        blocked_domains: list[str] | Unset = UNSET
        if not isinstance(self.blocked_domains, Unset):
            blocked_domains = self.blocked_domains

        allowed_ips: list[str] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = self.allowed_ips

        new_password = self.new_password

        old_password = self.old_password

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
        if blocked_domains is not UNSET:
            field_dict["blocked_domains"] = blocked_domains
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips
        if new_password is not UNSET:
            field_dict["new_password"] = new_password
        if old_password is not UNSET:
            field_dict["old_password"] = old_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        blocked_domains = cast(list[str], d.pop("blocked_domains", UNSET))

        allowed_ips = cast(list[str], d.pop("allowed_ips", UNSET))

        new_password = d.pop("new_password", UNSET)

        old_password = d.pop("old_password", UNSET)

        patched_profile_update_request = cls(
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
            blocked_domains=blocked_domains,
            allowed_ips=allowed_ips,
            new_password=new_password,
            old_password=old_password,
        )

        patched_profile_update_request.additional_properties = d
        return patched_profile_update_request

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
