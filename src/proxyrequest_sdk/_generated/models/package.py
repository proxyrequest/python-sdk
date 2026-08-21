from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.commission_type_enum import CommissionTypeEnum
from ..models.pricing_enum import PricingEnum
from ..models.pricing_unit_enum import PricingUnitEnum
from ..models.proxy_type_enum import ProxyTypeEnum
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.package_billing_model import PackageBillingModel
    from ..models.targeting_options import TargetingOptions


T = TypeVar("T", bound="Package")


@_attrs_define
class Package:
    name: str
    """ Unique display name for this package shown to customers and in the admin. Residential Starter Business Pro
    """
    alias: str
    """ Lowercase alphanumeric identifier used internally for package resolution and proxy username routing. Cannot
    be changed without affecting active connections. residential01 bizpro """
    features: list[Any]
    billing_cycle: int
    """ Number of days before purchased data expires. Set to -1 for data that never expires. 30 monthly -1 never
    expires """
    billing_model: PackageBillingModel
    targeting_options: TargetingOptions
    id: str | Unset = UNSET
    type_: ProxyTypeEnum | Unset = UNSET
    """ * `static` - Static * `residential` - Residential """
    order: int | Unset = UNSET
    """ Display order in the UI. Lower values appear first. """
    is_continent_targeting: bool | Unset = UNSET
    """ When enabled, users on this package can target proxies by continent. If disabled, they will only be able to
    target by country or city. """
    is_country_targeting: bool | Unset = UNSET
    """ Allow users to target a specific country in their proxy username. country-us country-de """
    is_region_targeting: bool | Unset = UNSET
    """ Allow users to target a specific region in their proxy username. Requires country targeting to be enabled.
    country-us-region-california """
    is_city_targeting: bool | Unset = UNSET
    """ Allow users to target a specific city in their proxy username. Requires country and region targeting to be
    enabled. country-us-region-california-city-los_angeles """
    is_asn_targeting: bool | Unset = UNSET
    """ Allow users to target a specific ASN in their proxy username. ASNs must be configured in the provider's
    location vocabulary. country-us-asn-3602 """
    description: str | Unset = UNSET
    """ Customer-facing description shown on the package listing page. """
    pricing: PricingEnum | Unset = UNSET
    """ * `fixed` - Fixed * `range` - Range """
    pricing_unit: PricingUnitEnum | Unset = UNSET
    """ * `data` - Data * `proxy` - Proxy """
    commission_rate: str | Unset = UNSET
    """ Reseller commission rate as a percentage of the sale price. Applies to all purchases of this package. 10.00
    → 10 percent commission on every purchase """
    commission_type: CommissionTypeEnum | Unset = UNSET
    """ * `flexible` - Flexible * `percentage` - Percentage * `fixed` - Fixed """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.package_billing_model import PackageBillingModel
        from ..models.targeting_options import TargetingOptions

        name = self.name

        alias = self.alias

        features = self.features

        billing_cycle = self.billing_cycle

        billing_model = self.billing_model.to_dict()

        targeting_options = self.targeting_options.to_dict()

        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        order = self.order

        is_continent_targeting = self.is_continent_targeting

        is_country_targeting = self.is_country_targeting

        is_region_targeting = self.is_region_targeting

        is_city_targeting = self.is_city_targeting

        is_asn_targeting = self.is_asn_targeting

        description = self.description

        pricing: str | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.value

        pricing_unit: str | Unset = UNSET
        if not isinstance(self.pricing_unit, Unset):
            pricing_unit = self.pricing_unit.value

        commission_rate = self.commission_rate

        commission_type: str | Unset = UNSET
        if not isinstance(self.commission_type, Unset):
            commission_type = self.commission_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "alias": alias,
                "features": features,
                "billing_cycle": billing_cycle,
                "billing_model": billing_model,
                "targeting_options": targeting_options,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if order is not UNSET:
            field_dict["order"] = order
        if is_continent_targeting is not UNSET:
            field_dict["is_continent_targeting"] = is_continent_targeting
        if is_country_targeting is not UNSET:
            field_dict["is_country_targeting"] = is_country_targeting
        if is_region_targeting is not UNSET:
            field_dict["is_region_targeting"] = is_region_targeting
        if is_city_targeting is not UNSET:
            field_dict["is_city_targeting"] = is_city_targeting
        if is_asn_targeting is not UNSET:
            field_dict["is_asn_targeting"] = is_asn_targeting
        if description is not UNSET:
            field_dict["description"] = description
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if pricing_unit is not UNSET:
            field_dict["pricing_unit"] = pricing_unit
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate
        if commission_type is not UNSET:
            field_dict["commission_type"] = commission_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_billing_model import PackageBillingModel
        from ..models.targeting_options import TargetingOptions

        d = dict(src_dict)
        name = d.pop("name")

        alias = d.pop("alias")

        features = cast(list[Any], d.pop("features"))

        billing_cycle = d.pop("billing_cycle")

        billing_model = PackageBillingModel.from_dict(d.pop("billing_model"))

        targeting_options = TargetingOptions.from_dict(d.pop("targeting_options"))

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ProxyTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProxyTypeEnum(_type_)

        order = d.pop("order", UNSET)

        is_continent_targeting = d.pop("is_continent_targeting", UNSET)

        is_country_targeting = d.pop("is_country_targeting", UNSET)

        is_region_targeting = d.pop("is_region_targeting", UNSET)

        is_city_targeting = d.pop("is_city_targeting", UNSET)

        is_asn_targeting = d.pop("is_asn_targeting", UNSET)

        description = d.pop("description", UNSET)

        _pricing = d.pop("pricing", UNSET)
        pricing: PricingEnum | Unset
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = PricingEnum(_pricing)

        _pricing_unit = d.pop("pricing_unit", UNSET)
        pricing_unit: PricingUnitEnum | Unset
        if isinstance(_pricing_unit, Unset):
            pricing_unit = UNSET
        else:
            pricing_unit = PricingUnitEnum(_pricing_unit)

        commission_rate = d.pop("commission_rate", UNSET)

        _commission_type = d.pop("commission_type", UNSET)
        commission_type: CommissionTypeEnum | Unset
        if isinstance(_commission_type, Unset):
            commission_type = UNSET
        else:
            commission_type = CommissionTypeEnum(_commission_type)

        package = cls(
            name=name,
            alias=alias,
            features=features,
            billing_cycle=billing_cycle,
            billing_model=billing_model,
            targeting_options=targeting_options,
            id=id,
            type_=type_,
            order=order,
            is_continent_targeting=is_continent_targeting,
            is_country_targeting=is_country_targeting,
            is_region_targeting=is_region_targeting,
            is_city_targeting=is_city_targeting,
            is_asn_targeting=is_asn_targeting,
            description=description,
            pricing=pricing,
            pricing_unit=pricing_unit,
            commission_rate=commission_rate,
            commission_type=commission_type,
        )

        package.additional_properties = d
        return package

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
