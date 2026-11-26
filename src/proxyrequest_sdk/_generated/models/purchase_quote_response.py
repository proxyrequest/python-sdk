from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime


T = TypeVar("T", bound="PurchaseQuoteResponse")


@_attrs_define
class PurchaseQuoteResponse:
    base_price: int
    total: int
    vat_amount: int
    currency: str
    pricing_plan_id: UUID | Unset = UNSET
    speed_mbps: int | Unset = UNSET
    duration_days: int | Unset = UNSET
    operation: str | Unset = UNSET
    credit_minor: int | Unset = UNSET
    service_value_minor: int | Unset = UNSET
    discount_amount: int | Unset = UNSET
    due_minor: int | Unset = UNSET
    starts_at: datetime.datetime | Unset = UNSET
    ends_at: datetime.datetime | Unset = UNSET
    quote_token: str | Unset = UNSET
    quote_valid_for_seconds: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_price = self.base_price

        total = self.total

        vat_amount = self.vat_amount

        currency = self.currency

        pricing_plan_id: str | Unset = UNSET
        if not isinstance(self.pricing_plan_id, Unset):
            pricing_plan_id = str(self.pricing_plan_id)

        speed_mbps = self.speed_mbps

        duration_days = self.duration_days

        operation = self.operation

        credit_minor = self.credit_minor

        service_value_minor = self.service_value_minor

        discount_amount = self.discount_amount

        due_minor = self.due_minor

        starts_at: str | Unset = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        ends_at: str | Unset = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        quote_token = self.quote_token

        quote_valid_for_seconds: int | None | Unset
        if isinstance(self.quote_valid_for_seconds, Unset):
            quote_valid_for_seconds = UNSET
        else:
            quote_valid_for_seconds = self.quote_valid_for_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_price": base_price,
                "total": total,
                "vat_amount": vat_amount,
                "currency": currency,
            }
        )
        if pricing_plan_id is not UNSET:
            field_dict["pricing_plan_id"] = pricing_plan_id
        if speed_mbps is not UNSET:
            field_dict["speed_mbps"] = speed_mbps
        if duration_days is not UNSET:
            field_dict["duration_days"] = duration_days
        if operation is not UNSET:
            field_dict["operation"] = operation
        if credit_minor is not UNSET:
            field_dict["credit_minor"] = credit_minor
        if service_value_minor is not UNSET:
            field_dict["service_value_minor"] = service_value_minor
        if discount_amount is not UNSET:
            field_dict["discount_amount"] = discount_amount
        if due_minor is not UNSET:
            field_dict["due_minor"] = due_minor
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if quote_token is not UNSET:
            field_dict["quote_token"] = quote_token
        if quote_valid_for_seconds is not UNSET:
            field_dict["quote_valid_for_seconds"] = quote_valid_for_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_price = d.pop("base_price")

        total = d.pop("total")

        vat_amount = d.pop("vat_amount")

        currency = d.pop("currency")

        _pricing_plan_id = d.pop("pricing_plan_id", UNSET)
        pricing_plan_id: UUID | Unset
        if isinstance(_pricing_plan_id, Unset):
            pricing_plan_id = UNSET
        else:
            pricing_plan_id = UUID(_pricing_plan_id)

        speed_mbps = d.pop("speed_mbps", UNSET)

        duration_days = d.pop("duration_days", UNSET)

        operation = d.pop("operation", UNSET)

        credit_minor = d.pop("credit_minor", UNSET)

        service_value_minor = d.pop("service_value_minor", UNSET)

        discount_amount = d.pop("discount_amount", UNSET)

        due_minor = d.pop("due_minor", UNSET)

        _starts_at = d.pop("starts_at", UNSET)
        starts_at: datetime.datetime | Unset
        if isinstance(_starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = datetime.datetime.fromisoformat(_starts_at)

        _ends_at = d.pop("ends_at", UNSET)
        ends_at: datetime.datetime | Unset
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = datetime.datetime.fromisoformat(_ends_at)

        quote_token = d.pop("quote_token", UNSET)

        def _parse_quote_valid_for_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quote_valid_for_seconds = _parse_quote_valid_for_seconds(
            d.pop("quote_valid_for_seconds", UNSET)
        )

        purchase_quote_response = cls(
            base_price=base_price,
            total=total,
            vat_amount=vat_amount,
            currency=currency,
            pricing_plan_id=pricing_plan_id,
            speed_mbps=speed_mbps,
            duration_days=duration_days,
            operation=operation,
            credit_minor=credit_minor,
            service_value_minor=service_value_minor,
            discount_amount=discount_amount,
            due_minor=due_minor,
            starts_at=starts_at,
            ends_at=ends_at,
            quote_token=quote_token,
            quote_valid_for_seconds=quote_valid_for_seconds,
        )

        purchase_quote_response.additional_properties = d
        return purchase_quote_response

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
