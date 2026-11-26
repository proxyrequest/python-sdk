from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.credential_mode_enum import CredentialModeEnum
from ..models.static_rental_status_enum import StaticRentalStatusEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
    from ..models.rental_detail_capabilities import RentalDetailCapabilities
    from ..models.rental_detail_endpoint import RentalDetailEndpoint
    from ..models.rental_detail_group import RentalDetailGroup
    from ..models.rental_detail_invoice import RentalDetailInvoice
    from ..models.rental_detail_term import RentalDetailTerm
    from ..models.rental_gateway import RentalGateway
    from ..models.rental_quote import RentalQuote


T = TypeVar("T", bound="RentalDetail")


@_attrs_define
class RentalDetail:
    count: int
    next_: None | str
    previous: None | str
    results: list[RentalDetailEndpoint]
    groups: list[RentalDetailGroup]
    order_id: UUID
    user_id: UUID
    package_id: UUID
    package_name: str
    status: StaticRentalStatusEnum
    """ * `reserved` - reserved * `provisioning` - provisioning * `fulfilled` - fulfilled * `expired` - expired *
    `paid_unfulfilled` - paid_unfulfilled * `partially_fulfilled` - partially_fulfilled * `partially_refunded` -
    partially_refunded * `refunded` - refunded """
    renewable_count: int
    snapshot: RentalQuote
    invoice_id: None | UUID
    reserved_until: datetime.datetime | None
    terms: list[RentalDetailTerm]
    invoices: list[RentalDetailInvoice]
    credential_mode: CredentialModeEnum
    """ * `shared` - shared * `per_endpoint` - per_endpoint """
    capabilities: RentalDetailCapabilities
    requested: int | Unset = UNSET
    fulfilled: int | Unset = UNSET
    refunded: int | Unset = UNSET
    pending: int | Unset = UNSET
    refunded_cents: int | Unset = UNSET
    username: str | Unset = UNSET
    proxy_password: str | Unset = UNSET
    mobile: bool | Unset = UNSET
    gateways: list[RentalGateway] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rental_detail_capabilities import RentalDetailCapabilities
        from ..models.rental_detail_endpoint import RentalDetailEndpoint
        from ..models.rental_detail_group import RentalDetailGroup
        from ..models.rental_detail_invoice import RentalDetailInvoice
        from ..models.rental_detail_term import RentalDetailTerm
        from ..models.rental_gateway import RentalGateway
        from ..models.rental_quote import RentalQuote

        count = self.count

        next_: None | str
        next_ = self.next_

        previous: None | str
        previous = self.previous

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        order_id = str(self.order_id)

        user_id = str(self.user_id)

        package_id = str(self.package_id)

        package_name = self.package_name

        status = self.status.value

        renewable_count = self.renewable_count

        snapshot = self.snapshot.to_dict()

        invoice_id: None | str
        if isinstance(self.invoice_id, UUID):
            invoice_id = str(self.invoice_id)
        else:
            invoice_id = self.invoice_id

        reserved_until: None | str
        if isinstance(self.reserved_until, datetime.datetime):
            reserved_until = self.reserved_until.isoformat()
        else:
            reserved_until = self.reserved_until

        terms = []
        for terms_item_data in self.terms:
            terms_item = terms_item_data.to_dict()
            terms.append(terms_item)

        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()
            invoices.append(invoices_item)

        credential_mode = self.credential_mode.value

        capabilities = self.capabilities.to_dict()

        requested = self.requested

        fulfilled = self.fulfilled

        refunded = self.refunded

        pending = self.pending

        refunded_cents = self.refunded_cents

        username = self.username

        proxy_password = self.proxy_password

        mobile = self.mobile

        gateways: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = []
            for gateways_item_data in self.gateways:
                gateways_item = gateways_item_data.to_dict()
                gateways.append(gateways_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "next": next_,
                "previous": previous,
                "results": results,
                "groups": groups,
                "order_id": order_id,
                "user_id": user_id,
                "package_id": package_id,
                "package_name": package_name,
                "status": status,
                "renewable_count": renewable_count,
                "snapshot": snapshot,
                "invoice_id": invoice_id,
                "reserved_until": reserved_until,
                "terms": terms,
                "invoices": invoices,
                "credential_mode": credential_mode,
                "capabilities": capabilities,
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
        if username is not UNSET:
            field_dict["username"] = username
        if proxy_password is not UNSET:
            field_dict["proxy_password"] = proxy_password
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if gateways is not UNSET:
            field_dict["gateways"] = gateways

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rental_detail_capabilities import RentalDetailCapabilities
        from ..models.rental_detail_endpoint import RentalDetailEndpoint
        from ..models.rental_detail_group import RentalDetailGroup
        from ..models.rental_detail_invoice import RentalDetailInvoice
        from ..models.rental_detail_term import RentalDetailTerm
        from ..models.rental_gateway import RentalGateway
        from ..models.rental_quote import RentalQuote

        d = dict(src_dict)
        count = d.pop("count")

        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        def _parse_previous(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous = _parse_previous(d.pop("previous"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = RentalDetailEndpoint.from_dict(results_item_data)

            results.append(results_item)

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = RentalDetailGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        order_id = UUID(d.pop("order_id"))

        user_id = UUID(d.pop("user_id"))

        package_id = UUID(d.pop("package_id"))

        package_name = d.pop("package_name")

        status = StaticRentalStatusEnum(d.pop("status"))

        renewable_count = d.pop("renewable_count")

        snapshot = RentalQuote.from_dict(d.pop("snapshot"))

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

        terms = []
        _terms = d.pop("terms")
        for terms_item_data in _terms:
            terms_item = RentalDetailTerm.from_dict(terms_item_data)

            terms.append(terms_item)

        invoices = []
        _invoices = d.pop("invoices")
        for invoices_item_data in _invoices:
            invoices_item = RentalDetailInvoice.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        credential_mode = CredentialModeEnum(d.pop("credential_mode"))

        capabilities = RentalDetailCapabilities.from_dict(d.pop("capabilities"))

        requested = d.pop("requested", UNSET)

        fulfilled = d.pop("fulfilled", UNSET)

        refunded = d.pop("refunded", UNSET)

        pending = d.pop("pending", UNSET)

        refunded_cents = d.pop("refunded_cents", UNSET)

        username = d.pop("username", UNSET)

        proxy_password = d.pop("proxy_password", UNSET)

        mobile = d.pop("mobile", UNSET)

        _gateways = d.pop("gateways", UNSET)
        gateways: list[RentalGateway] | Unset = UNSET
        if _gateways is not UNSET:
            gateways = []
            for gateways_item_data in _gateways:
                gateways_item = RentalGateway.from_dict(gateways_item_data)

                gateways.append(gateways_item)

        rental_detail = cls(
            count=count,
            next_=next_,
            previous=previous,
            results=results,
            groups=groups,
            order_id=order_id,
            user_id=user_id,
            package_id=package_id,
            package_name=package_name,
            status=status,
            renewable_count=renewable_count,
            snapshot=snapshot,
            invoice_id=invoice_id,
            reserved_until=reserved_until,
            terms=terms,
            invoices=invoices,
            credential_mode=credential_mode,
            capabilities=capabilities,
            requested=requested,
            fulfilled=fulfilled,
            refunded=refunded,
            pending=pending,
            refunded_cents=refunded_cents,
            username=username,
            proxy_password=proxy_password,
            mobile=mobile,
            gateways=gateways,
        )

        rental_detail.additional_properties = d
        return rental_detail

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
