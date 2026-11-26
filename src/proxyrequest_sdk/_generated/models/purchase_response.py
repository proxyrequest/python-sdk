from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.static_rental_status_enum import StaticRentalStatusEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.rental_quote import RentalQuote


T = TypeVar("T", bound="PurchaseResponse")


@_attrs_define
class PurchaseResponse:
    id: UUID
    status: StaticRentalStatusEnum
    """ * `reserved` - reserved * `provisioning` - provisioning * `fulfilled` - fulfilled * `expired` - expired *
    `paid_unfulfilled` - paid_unfulfilled * `partially_fulfilled` - partially_fulfilled * `partially_refunded` -
    partially_refunded * `refunded` - refunded """
    snapshot: RentalQuote
    reserved_until: datetime.datetime | None
    invoice_id: None | UUID
    order_id: None | UUID
    requested: int | Unset = UNSET
    fulfilled: int | Unset = UNSET
    refunded: int | Unset = UNSET
    pending: int | Unset = UNSET
    refunded_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rental_quote import RentalQuote

        id = str(self.id)

        status = self.status.value

        snapshot = self.snapshot.to_dict()

        reserved_until: None | str
        if isinstance(self.reserved_until, datetime.datetime):
            reserved_until = self.reserved_until.isoformat()
        else:
            reserved_until = self.reserved_until

        invoice_id: None | str
        if isinstance(self.invoice_id, UUID):
            invoice_id = str(self.invoice_id)
        else:
            invoice_id = self.invoice_id

        order_id: None | str
        if isinstance(self.order_id, UUID):
            order_id = str(self.order_id)
        else:
            order_id = self.order_id

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
                "status": status,
                "snapshot": snapshot,
                "reserved_until": reserved_until,
                "invoice_id": invoice_id,
                "order_id": order_id,
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
        from ..models.rental_quote import RentalQuote

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = StaticRentalStatusEnum(d.pop("status"))

        snapshot = RentalQuote.from_dict(d.pop("snapshot"))

        def _parse_reserved_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reserved_until_type_0 = datetime.datetime.fromisoformat(data)

                return reserved_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        reserved_until = _parse_reserved_until(d.pop("reserved_until"))

        def _parse_invoice_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoice_id_type_0 = UUID(data)

                return invoice_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        invoice_id = _parse_invoice_id(d.pop("invoice_id"))

        def _parse_order_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_id_type_0 = UUID(data)

                return order_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        order_id = _parse_order_id(d.pop("order_id"))

        requested = d.pop("requested", UNSET)

        fulfilled = d.pop("fulfilled", UNSET)

        refunded = d.pop("refunded", UNSET)

        pending = d.pop("pending", UNSET)

        refunded_cents = d.pop("refunded_cents", UNSET)

        purchase_response = cls(
            id=id,
            status=status,
            snapshot=snapshot,
            reserved_until=reserved_until,
            invoice_id=invoice_id,
            order_id=order_id,
            requested=requested,
            fulfilled=fulfilled,
            refunded=refunded,
            pending=pending,
            refunded_cents=refunded_cents,
        )

        purchase_response.additional_properties = d
        return purchase_response

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
