from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID


T = TypeVar("T", bound="InvoicesCreateResponse502")


@_attrs_define
class InvoicesCreateResponse502:
    invoice_id: UUID
    gateway: str
    retryable: bool
    non_field_errors: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoice_id = str(self.invoice_id)

        gateway = self.gateway

        retryable = self.retryable

        non_field_errors = self.non_field_errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice_id": invoice_id,
                "gateway": gateway,
                "retryable": retryable,
                "non_field_errors": non_field_errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invoice_id = UUID(d.pop("invoice_id"))

        gateway = d.pop("gateway")

        retryable = d.pop("retryable")

        non_field_errors = cast(list[str], d.pop("non_field_errors"))

        invoices_create_response_502 = cls(
            invoice_id=invoice_id,
            gateway=gateway,
            retryable=retryable,
            non_field_errors=non_field_errors,
        )

        invoices_create_response_502.additional_properties = d
        return invoices_create_response_502

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
