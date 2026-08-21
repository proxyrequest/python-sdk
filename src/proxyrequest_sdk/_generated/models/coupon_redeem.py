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


T = TypeVar("T", bound="CouponRedeem")


@_attrs_define
class CouponRedeem:
    user: UUID
    invoice_amount: float | None
    discount_applied: float | None
    created: datetime.datetime
    id: str | Unset = UNSET
    invoice: None | str | Unset = UNSET
    redeemed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = str(self.user)

        invoice_amount: float | None
        invoice_amount = self.invoice_amount

        discount_applied: float | None
        discount_applied = self.discount_applied

        created = self.created.isoformat()

        id = self.id

        invoice: None | str | Unset
        if isinstance(self.invoice, Unset):
            invoice = UNSET
        else:
            invoice = self.invoice

        redeemed_at: None | str | Unset
        if isinstance(self.redeemed_at, Unset):
            redeemed_at = UNSET
        elif isinstance(self.redeemed_at, datetime.datetime):
            redeemed_at = self.redeemed_at.isoformat()
        else:
            redeemed_at = self.redeemed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "invoice_amount": invoice_amount,
                "discount_applied": discount_applied,
                "created": created,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if redeemed_at is not UNSET:
            field_dict["redeemed_at"] = redeemed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = UUID(d.pop("user"))

        def _parse_invoice_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        invoice_amount = _parse_invoice_amount(d.pop("invoice_amount"))

        def _parse_discount_applied(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        discount_applied = _parse_discount_applied(d.pop("discount_applied"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = d.pop("id", UNSET)

        def _parse_invoice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice = _parse_invoice(d.pop("invoice", UNSET))

        def _parse_redeemed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                redeemed_at_type_0 = datetime.datetime.fromisoformat(data)

                return redeemed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        redeemed_at = _parse_redeemed_at(d.pop("redeemed_at", UNSET))

        coupon_redeem = cls(
            user=user,
            invoice_amount=invoice_amount,
            discount_applied=discount_applied,
            created=created,
            id=id,
            invoice=invoice,
            redeemed_at=redeemed_at,
        )

        coupon_redeem.additional_properties = d
        return coupon_redeem

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
