from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.targeting_options import TargetingOptions


T = TypeVar("T", bound="PackageShort")


@_attrs_define
class PackageShort:
    name: str
    """ Unique display name for this package shown to customers and in the admin. Residential Starter Business Pro
    """
    alias: str
    """ Lowercase alphanumeric identifier used internally for package resolution and proxy username routing. Cannot
    be changed without affecting active connections. residential01 bizpro """
    targeting_options: TargetingOptions
    id: str | Unset = UNSET
    is_unlimited_data: bool | Unset = UNSET
    """ When enabled, users on this package have no data cap. The proxy will not enforce any bandwidth limit. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.targeting_options import TargetingOptions

        name = self.name

        alias = self.alias

        targeting_options = self.targeting_options.to_dict()

        id = self.id

        is_unlimited_data = self.is_unlimited_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "alias": alias,
                "targeting_options": targeting_options,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_unlimited_data is not UNSET:
            field_dict["is_unlimited_data"] = is_unlimited_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.targeting_options import TargetingOptions

        d = dict(src_dict)
        name = d.pop("name")

        alias = d.pop("alias")

        targeting_options = TargetingOptions.from_dict(d.pop("targeting_options"))

        id = d.pop("id", UNSET)

        is_unlimited_data = d.pop("is_unlimited_data", UNSET)

        package_short = cls(
            name=name,
            alias=alias,
            targeting_options=targeting_options,
            id=id,
            is_unlimited_data=is_unlimited_data,
        )

        package_short.additional_properties = d
        return package_short

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
