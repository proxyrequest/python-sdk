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
    from ..models.renewal_checkout_request import RenewalCheckoutRequest


T = TypeVar("T", bound="RenewalRequestRequest")


@_attrs_define
class RenewalRequestRequest:
    term_id: UUID
    invoice: RenewalCheckoutRequest
    """ Invoice transport validation with an explicitly composed application command. """
    endpoint_ids: list[UUID] | Unset = UNSET
    all_endpoints: bool | Unset = False
    idempotency_key: str | Unset = UNSET
    expected_total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.renewal_checkout_request import RenewalCheckoutRequest

        term_id = str(self.term_id)

        invoice = self.invoice.to_dict()

        endpoint_ids: list[str] | Unset = UNSET
        if not isinstance(self.endpoint_ids, Unset):
            endpoint_ids = []
            for endpoint_ids_item_data in self.endpoint_ids:
                endpoint_ids_item = str(endpoint_ids_item_data)
                endpoint_ids.append(endpoint_ids_item)

        all_endpoints = self.all_endpoints

        idempotency_key = self.idempotency_key

        expected_total = self.expected_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term_id": term_id,
                "invoice": invoice,
            }
        )
        if endpoint_ids is not UNSET:
            field_dict["endpoint_ids"] = endpoint_ids
        if all_endpoints is not UNSET:
            field_dict["all_endpoints"] = all_endpoints
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if expected_total is not UNSET:
            field_dict["expected_total"] = expected_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.renewal_checkout_request import RenewalCheckoutRequest

        d = dict(src_dict)
        term_id = UUID(d.pop("term_id"))

        invoice = RenewalCheckoutRequest.from_dict(d.pop("invoice"))

        _endpoint_ids = d.pop("endpoint_ids", UNSET)
        endpoint_ids: list[UUID] | Unset = UNSET
        if _endpoint_ids is not UNSET:
            endpoint_ids = []
            for endpoint_ids_item_data in _endpoint_ids:
                endpoint_ids_item = UUID(endpoint_ids_item_data)

                endpoint_ids.append(endpoint_ids_item)

        all_endpoints = d.pop("all_endpoints", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        expected_total = d.pop("expected_total", UNSET)

        renewal_request_request = cls(
            term_id=term_id,
            invoice=invoice,
            endpoint_ids=endpoint_ids,
            all_endpoints=all_endpoints,
            idempotency_key=idempotency_key,
            expected_total=expected_total,
        )

        renewal_request_request.additional_properties = d
        return renewal_request_request

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
