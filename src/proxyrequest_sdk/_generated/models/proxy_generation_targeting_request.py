from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="ProxyGenerationTargetingRequest")


@_attrs_define
class ProxyGenerationTargetingRequest:
    continent: str | Unset = UNSET
    """ Target continent code. """
    country: str | Unset = UNSET
    """ Target country code. """
    region: str | Unset = UNSET
    """ Target region or state code. """
    city: str | Unset = UNSET
    """ Target city code. """
    pool: str | Unset = UNSET
    """ Proxy pool identifier. """
    asn: int | Unset = UNSET
    """ Target autonomous system number. """
    isp: str | Unset = UNSET
    """ Target internet service provider. """
    os: str | Unset = UNSET
    """ Target operating system: linux, windows, ios, macos, android. Use comma-separated values only when combined
    OS targeting is enabled. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        continent = self.continent

        country = self.country

        region = self.region

        city = self.city

        pool = self.pool

        asn = self.asn

        isp = self.isp

        os = self.os

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if continent is not UNSET:
            field_dict["continent"] = continent
        if country is not UNSET:
            field_dict["country"] = country
        if region is not UNSET:
            field_dict["region"] = region
        if city is not UNSET:
            field_dict["city"] = city
        if pool is not UNSET:
            field_dict["pool"] = pool
        if asn is not UNSET:
            field_dict["asn"] = asn
        if isp is not UNSET:
            field_dict["isp"] = isp
        if os is not UNSET:
            field_dict["os"] = os

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        continent = d.pop("continent", UNSET)

        country = d.pop("country", UNSET)

        region = d.pop("region", UNSET)

        city = d.pop("city", UNSET)

        pool = d.pop("pool", UNSET)

        asn = d.pop("asn", UNSET)

        isp = d.pop("isp", UNSET)

        os = d.pop("os", UNSET)

        proxy_generation_targeting_request = cls(
            continent=continent,
            country=country,
            region=region,
            city=city,
            pool=pool,
            asn=asn,
            isp=isp,
            os=os,
        )

        proxy_generation_targeting_request.additional_properties = d
        return proxy_generation_targeting_request

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
