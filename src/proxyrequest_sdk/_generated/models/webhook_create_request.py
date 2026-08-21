from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_scope_enum import WebhookScopeEnum
from ..types import UNSET, Unset


T = TypeVar("T", bound="WebhookCreateRequest")


@_attrs_define
class WebhookCreateRequest:
    type_: WebhookScopeEnum
    """ * `user` - User * `reseller` - Reseller * `system` - System """
    endpoint: str
    read_timeout: int | Unset = 5
    write_timeout: int | Unset = 5
    retries: int | Unset = 3
    retry_timeout: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        endpoint = self.endpoint

        read_timeout = self.read_timeout

        write_timeout = self.write_timeout

        retries = self.retries

        retry_timeout = self.retry_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "endpoint": endpoint,
            }
        )
        if read_timeout is not UNSET:
            field_dict["read_timeout"] = read_timeout
        if write_timeout is not UNSET:
            field_dict["write_timeout"] = write_timeout
        if retries is not UNSET:
            field_dict["retries"] = retries
        if retry_timeout is not UNSET:
            field_dict["retry_timeout"] = retry_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = WebhookScopeEnum(d.pop("type"))

        endpoint = d.pop("endpoint")

        read_timeout = d.pop("read_timeout", UNSET)

        write_timeout = d.pop("write_timeout", UNSET)

        retries = d.pop("retries", UNSET)

        retry_timeout = d.pop("retry_timeout", UNSET)

        webhook_create_request = cls(
            type_=type_,
            endpoint=endpoint,
            read_timeout=read_timeout,
            write_timeout=write_timeout,
            retries=retries,
            retry_timeout=retry_timeout,
        )

        webhook_create_request.additional_properties = d
        return webhook_create_request

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
