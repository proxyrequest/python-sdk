from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.products_enum import ProductsEnum
from typing import cast

if TYPE_CHECKING:
    from ..models.network_metadata import NetworkMetadata


T = TypeVar("T", bound="Products")


@_attrs_define
class Products:
    products: list[ProductsEnum]
    networks: list[NetworkMetadata]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.network_metadata import NetworkMetadata

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.value
            products.append(products_item)

        networks = []
        for networks_item_data in self.networks:
            networks_item = networks_item_data.to_dict()
            networks.append(networks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
                "networks": networks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_metadata import NetworkMetadata

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = ProductsEnum(products_item_data)

            products.append(products_item)

        networks = []
        _networks = d.pop("networks")
        for networks_item_data in _networks:
            networks_item = NetworkMetadata.from_dict(networks_item_data)

            networks.append(networks_item)

        products = cls(
            products=products,
            networks=networks,
        )

        products.additional_properties = d
        return products

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
