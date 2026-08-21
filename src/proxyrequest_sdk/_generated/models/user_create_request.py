from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.user_create_request_meta import UserCreateRequestMeta


T = TypeVar("T", bound="UserCreateRequest")


@_attrs_define
class UserCreateRequest:
    """Fields accepted when a reseller or administrator creates a customer account."""

    username: str
    """ Unique username for the account. Must be 4-128 characters. """
    password: str
    """ Account password. Must be 8-128 characters long. """
    email: str | Unset = UNSET
    """ User's email address. Must be unique if provided. """
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
    blocked_domains: list[str] | Unset = UNSET
    """ List of domains to block for this user. """
    allowed_ips: list[str] | Unset = UNSET
    """ List of source IP addresses allowed for this user. The maximum list size is configured per deployment. """
    connection_limit: int | Unset = UNSET
    """ Maximum number of concurrent connections allowed for the user. """
    is_reseller: bool | Unset = False
    """ Whether the user should have reseller privileges. Only superusers can create resellers. """
    is_top_level: bool | Unset = False
    """ Whether the user is a sub-user under the parent account. """
    data: int | Unset = UNSET
    """ Initial data allocation for the user (traditional auth mode only). """
    package_id: UUID | Unset = UNSET
    """ ProxyRequest package UUID to assign to the user (package-based auth mode only). Headless integrations
    resolve it from their local product mapping. """
    meta: UserCreateRequestMeta | Unset = UNSET
    """ Additional metadata for the user. Maximum 50 fields. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_create_request_meta import UserCreateRequestMeta

        username = self.username

        password = self.password

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        country = self.country

        state = self.state

        city = self.city

        address = self.address

        zip_ = self.zip_

        blocked_domains: list[str] | Unset = UNSET
        if not isinstance(self.blocked_domains, Unset):
            blocked_domains = self.blocked_domains

        allowed_ips: list[str] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = self.allowed_ips

        connection_limit = self.connection_limit

        is_reseller = self.is_reseller

        is_top_level = self.is_top_level

        data = self.data

        package_id: str | Unset = UNSET
        if not isinstance(self.package_id, Unset):
            package_id = str(self.package_id)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
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
        if blocked_domains is not UNSET:
            field_dict["blocked_domains"] = blocked_domains
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips
        if connection_limit is not UNSET:
            field_dict["connection_limit"] = connection_limit
        if is_reseller is not UNSET:
            field_dict["is_reseller"] = is_reseller
        if is_top_level is not UNSET:
            field_dict["is_top_level"] = is_top_level
        if data is not UNSET:
            field_dict["data"] = data
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_create_request_meta import UserCreateRequestMeta

        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        country = d.pop("country", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        address = d.pop("address", UNSET)

        zip_ = d.pop("zip", UNSET)

        blocked_domains = cast(list[str], d.pop("blocked_domains", UNSET))

        allowed_ips = cast(list[str], d.pop("allowed_ips", UNSET))

        connection_limit = d.pop("connection_limit", UNSET)

        is_reseller = d.pop("is_reseller", UNSET)

        is_top_level = d.pop("is_top_level", UNSET)

        data = d.pop("data", UNSET)

        _package_id = d.pop("package_id", UNSET)
        package_id: UUID | Unset
        if isinstance(_package_id, Unset):
            package_id = UNSET
        else:
            package_id = UUID(_package_id)

        _meta = d.pop("meta", UNSET)
        meta: UserCreateRequestMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = UserCreateRequestMeta.from_dict(_meta)

        user_create_request = cls(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            country=country,
            state=state,
            city=city,
            address=address,
            zip_=zip_,
            blocked_domains=blocked_domains,
            allowed_ips=allowed_ips,
            connection_limit=connection_limit,
            is_reseller=is_reseller,
            is_top_level=is_top_level,
            data=data,
            package_id=package_id,
            meta=meta,
        )

        user_create_request.additional_properties = d
        return user_create_request

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
