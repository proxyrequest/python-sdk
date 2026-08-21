from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="LoginGoogleCreateResponse400")


@_attrs_define
class LoginGoogleCreateResponse400:
    """Validation and API error payload. Field names may be added dynamically; field errors are returned as arrays of
    human-readable messages.

    """

    detail: str | Unset = UNSET
    non_field_errors: list[str] | Unset = UNSET
    additional_properties: dict[str, list[str] | str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        non_field_errors: list[str] | Unset = UNSET
        if not isinstance(self.non_field_errors, Unset):
            non_field_errors = self.non_field_errors

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = prop

            else:
                field_dict[prop_name] = prop

        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail
        if non_field_errors is not UNSET:
            field_dict["non_field_errors"] = non_field_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail = d.pop("detail", UNSET)

        non_field_errors = cast(list[str], d.pop("non_field_errors", UNSET))

        login_google_create_response_400 = cls(
            detail=detail,
            non_field_errors=non_field_errors,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> list[str] | str:
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_1 = cast(list[str], data)

                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(list[str] | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        login_google_create_response_400.additional_properties = additional_properties
        return login_google_create_response_400

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[str] | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[str] | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
