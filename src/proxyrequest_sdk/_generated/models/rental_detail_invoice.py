from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.blank_enum import BlankEnum
from ..models.kind_enum import KindEnum
from ..models.static_rental_invoice_status_enum import StaticRentalInvoiceStatusEnum
from ..models.static_rental_status_enum import StaticRentalStatusEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime


T = TypeVar("T", bound="RentalDetailInvoice")


@_attrs_define
class RentalDetailInvoice:
    id: UUID
    kind: KindEnum
    """ * `purchase` - purchase * `renewal` - renewal """
    status: StaticRentalInvoiceStatusEnum
    """ * `pending` - Pending * `paid` - Paid * `unpaid` - Unpaid * `error` - Error * `cancelled` - cancelled *
    `failed` - failed """
    fulfillment_status: BlankEnum | StaticRentalStatusEnum
    price_total: int
    currency: str
    created: datetime.datetime
    failed: int
    failure_reason: None | str
    fulfillment_deadline: datetime.datetime | None
    requested: int | Unset = UNSET
    fulfilled: int | Unset = UNSET
    refunded: int | Unset = UNSET
    pending: int | Unset = UNSET
    refunded_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        kind = self.kind.value

        status = self.status.value

        fulfillment_status: str
        if isinstance(self.fulfillment_status, StaticRentalStatusEnum):
            fulfillment_status = self.fulfillment_status.value
        else:
            fulfillment_status = self.fulfillment_status.value

        price_total = self.price_total

        currency = self.currency

        created = self.created.isoformat()

        failed = self.failed

        failure_reason: None | str
        failure_reason = self.failure_reason

        fulfillment_deadline: None | str
        if isinstance(self.fulfillment_deadline, datetime.datetime):
            fulfillment_deadline = self.fulfillment_deadline.isoformat()
        else:
            fulfillment_deadline = self.fulfillment_deadline

        requested = self.requested

        fulfilled = self.fulfilled

        refunded = self.refunded

        pending = self.pending

        refunded_cents = self.refunded_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "status": status,
                "fulfillment_status": fulfillment_status,
                "price_total": price_total,
                "currency": currency,
                "created": created,
                "failed": failed,
                "failure_reason": failure_reason,
                "fulfillment_deadline": fulfillment_deadline,
            }
        )
        if requested is not UNSET:
            field_dict["requested"] = requested
        if fulfilled is not UNSET:
            field_dict["fulfilled"] = fulfilled
        if refunded is not UNSET:
            field_dict["refunded"] = refunded
        if pending is not UNSET:
            field_dict["pending"] = pending
        if refunded_cents is not UNSET:
            field_dict["refunded_cents"] = refunded_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        kind = KindEnum(d.pop("kind"))

        status = StaticRentalInvoiceStatusEnum(d.pop("status"))

        def _parse_fulfillment_status(data: object) -> BlankEnum | StaticRentalStatusEnum:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fulfillment_status_type_0 = StaticRentalStatusEnum(data)

                return fulfillment_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            fulfillment_status_type_1 = BlankEnum(data)

            return fulfillment_status_type_1

        fulfillment_status = _parse_fulfillment_status(d.pop("fulfillment_status"))

        price_total = d.pop("price_total")

        currency = d.pop("currency")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        failed = d.pop("failed")

        def _parse_failure_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure_reason = _parse_failure_reason(d.pop("failure_reason"))

        def _parse_fulfillment_deadline(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fulfillment_deadline_type_0 = datetime.datetime.fromisoformat(data)

                return fulfillment_deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        fulfillment_deadline = _parse_fulfillment_deadline(d.pop("fulfillment_deadline"))

        requested = d.pop("requested", UNSET)

        fulfilled = d.pop("fulfilled", UNSET)

        refunded = d.pop("refunded", UNSET)

        pending = d.pop("pending", UNSET)

        refunded_cents = d.pop("refunded_cents", UNSET)

        rental_detail_invoice = cls(
            id=id,
            kind=kind,
            status=status,
            fulfillment_status=fulfillment_status,
            price_total=price_total,
            currency=currency,
            created=created,
            failed=failed,
            failure_reason=failure_reason,
            fulfillment_deadline=fulfillment_deadline,
            requested=requested,
            fulfilled=fulfilled,
            refunded=refunded,
            pending=pending,
            refunded_cents=refunded_cents,
        )

        rental_detail_invoice.additional_properties = d
        return rental_detail_invoice

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
