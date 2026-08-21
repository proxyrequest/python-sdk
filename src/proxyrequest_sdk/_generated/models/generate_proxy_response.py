from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.generated_proxy import GeneratedProxy


T = TypeVar("T", bound="GenerateProxyResponse")


@_attrs_define
class GenerateProxyResponse:
    count: int
    proxies: list[GeneratedProxy]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generated_proxy import GeneratedProxy

        count = self.count

        proxies = []
        for proxies_item_data in self.proxies:
            proxies_item = proxies_item_data.to_dict()
            proxies.append(proxies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "proxies": proxies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generated_proxy import GeneratedProxy

        d = dict(src_dict)
        count = d.pop("count")

        proxies = []
        _proxies = d.pop("proxies")
        for proxies_item_data in _proxies:
            proxies_item = GeneratedProxy.from_dict(proxies_item_data)

            proxies.append(proxies_item)

        generate_proxy_response = cls(
            count=count,
            proxies=proxies,
        )

        generate_proxy_response.additional_properties = d
        return generate_proxy_response

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
