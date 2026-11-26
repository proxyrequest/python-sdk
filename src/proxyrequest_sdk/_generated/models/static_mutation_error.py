from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="StaticMutationError")


@_attrs_define
class StaticMutationError:
    code: str
    non_field_errors: list[str] | Unset = UNSET
    detail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        non_field_errors: list[str] | Unset = UNSET
        if not isinstance(self.non_field_errors, Unset):
            non_field_errors = self.non_field_errors

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if non_field_errors is not UNSET:
            field_dict["non_field_errors"] = non_field_errors
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        non_field_errors = cast(list[str], d.pop("non_field_errors", UNSET))

        detail = d.pop("detail", UNSET)

        static_mutation_error = cls(
            code=code,
            non_field_errors=non_field_errors,
            detail=detail,
        )

        static_mutation_error.additional_properties = d
        return static_mutation_error

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
