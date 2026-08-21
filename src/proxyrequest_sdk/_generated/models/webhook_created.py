from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_scope_enum import WebhookScopeEnum
from ..types import UNSET, Unset
from typing import cast
import datetime


T = TypeVar("T", bound="WebhookCreated")


@_attrs_define
class WebhookCreated:
    endpoint: str
    """ HTTPS URL that receives webhook POST requests when events are triggered. https://example.com/webhooks/proxy
    The endpoint must be publicly accessible and respond within the configured read timeout. """
    created: datetime.datetime
    id: str | Unset = UNSET
    type_: WebhookScopeEnum | Unset = UNSET
    """ * `user` - User * `reseller` - Reseller * `system` - System """
    secret: str | Unset = UNSET
    """ Secret used to sign each webhook payload. The receiving endpoint should verify the signature to confirm the
    request originated from this platform. Auto-generated if left blank. Store this value securely on the receiving
    end. """
    read_timeout: int | Unset = UNSET
    """ Maximum time to wait for the endpoint to return a response. Requests that exceed this limit are treated as
    failed and may be retried. """
    write_timeout: int | Unset = UNSET
    """ Maximum time to wait while sending the payload to the endpoint. Requests that exceed this limit are treated
    as failed and may be retried. """
    retries: int | Unset = UNSET
    """ Number of additional delivery attempts after an initial failure. Set to 0 to disable retries. 3 → up to 4
    total delivery attempts """
    retry_timeout: int | Unset = UNSET
    """ How long to wait before each retry attempt after a failed delivery. 10 → retry after 10 seconds """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        created = self.created.isoformat()

        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        secret = self.secret

        read_timeout = self.read_timeout

        write_timeout = self.write_timeout

        retries = self.retries

        retry_timeout = self.retry_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "created": created,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if secret is not UNSET:
            field_dict["secret"] = secret
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
        endpoint = d.pop("endpoint")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: WebhookScopeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WebhookScopeEnum(_type_)

        secret = d.pop("secret", UNSET)

        read_timeout = d.pop("read_timeout", UNSET)

        write_timeout = d.pop("write_timeout", UNSET)

        retries = d.pop("retries", UNSET)

        retry_timeout = d.pop("retry_timeout", UNSET)

        webhook_created = cls(
            endpoint=endpoint,
            created=created,
            id=id,
            type_=type_,
            secret=secret,
            read_timeout=read_timeout,
            write_timeout=write_timeout,
            retries=retries,
            retry_timeout=retry_timeout,
        )

        webhook_created.additional_properties = d
        return webhook_created

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
