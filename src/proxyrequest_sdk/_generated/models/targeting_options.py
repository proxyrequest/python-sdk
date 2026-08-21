from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="TargetingOptions")


@_attrs_define
class TargetingOptions:
    package: str
    split_char: str
    value_char: str
    continent: str
    country: str
    region: str
    city: str
    asn: str
    isp: str
    username: str
    pool: str
    location: str
    location_format: str
    session: str
    session_mode_tag: str
    session_ttl: str
    session_ttl_format: int
    os: str
    os_combined: bool
    os_split_char: str
    os_linux: str
    os_windows: str
    os_ios: str
    os_macos: str
    os_android: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package = self.package

        split_char = self.split_char

        value_char = self.value_char

        continent = self.continent

        country = self.country

        region = self.region

        city = self.city

        asn = self.asn

        isp = self.isp

        username = self.username

        pool = self.pool

        location = self.location

        location_format = self.location_format

        session = self.session

        session_mode_tag = self.session_mode_tag

        session_ttl = self.session_ttl

        session_ttl_format = self.session_ttl_format

        os = self.os

        os_combined = self.os_combined

        os_split_char = self.os_split_char

        os_linux = self.os_linux

        os_windows = self.os_windows

        os_ios = self.os_ios

        os_macos = self.os_macos

        os_android = self.os_android

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package": package,
                "split_char": split_char,
                "value_char": value_char,
                "continent": continent,
                "country": country,
                "region": region,
                "city": city,
                "asn": asn,
                "isp": isp,
                "username": username,
                "pool": pool,
                "location": location,
                "location_format": location_format,
                "session": session,
                "session_mode_tag": session_mode_tag,
                "session_ttl": session_ttl,
                "session_ttl_format": session_ttl_format,
                "os": os,
                "os_combined": os_combined,
                "os_split_char": os_split_char,
                "os_linux": os_linux,
                "os_windows": os_windows,
                "os_ios": os_ios,
                "os_macos": os_macos,
                "os_android": os_android,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package = d.pop("package")

        split_char = d.pop("split_char")

        value_char = d.pop("value_char")

        continent = d.pop("continent")

        country = d.pop("country")

        region = d.pop("region")

        city = d.pop("city")

        asn = d.pop("asn")

        isp = d.pop("isp")

        username = d.pop("username")

        pool = d.pop("pool")

        location = d.pop("location")

        location_format = d.pop("location_format")

        session = d.pop("session")

        session_mode_tag = d.pop("session_mode_tag")

        session_ttl = d.pop("session_ttl")

        session_ttl_format = d.pop("session_ttl_format")

        os = d.pop("os")

        os_combined = d.pop("os_combined")

        os_split_char = d.pop("os_split_char")

        os_linux = d.pop("os_linux")

        os_windows = d.pop("os_windows")

        os_ios = d.pop("os_ios")

        os_macos = d.pop("os_macos")

        os_android = d.pop("os_android")

        targeting_options = cls(
            package=package,
            split_char=split_char,
            value_char=value_char,
            continent=continent,
            country=country,
            region=region,
            city=city,
            asn=asn,
            isp=isp,
            username=username,
            pool=pool,
            location=location,
            location_format=location_format,
            session=session,
            session_mode_tag=session_mode_tag,
            session_ttl=session_ttl,
            session_ttl_format=session_ttl_format,
            os=os,
            os_combined=os_combined,
            os_split_char=os_split_char,
            os_linux=os_linux,
            os_windows=os_windows,
            os_ios=os_ios,
            os_macos=os_macos,
            os_android=os_android,
        )

        targeting_options.additional_properties = d
        return targeting_options

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
