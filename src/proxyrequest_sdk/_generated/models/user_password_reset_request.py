from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID


T = TypeVar("T", bound="UserPasswordResetRequest")


@_attrs_define
class UserPasswordResetRequest:
    package_id: UUID | Unset = UNSET
    """ Package whose proxy password should be rotated. Required only when package-based authentication is enabled.
    """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_id: str | Unset = UNSET
        if not isinstance(self.package_id, Unset):
            package_id = str(self.package_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_id is not UNSET:
            field_dict["package_id"] = package_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _package_id = d.pop("package_id", UNSET)
        package_id: UUID | Unset
        if isinstance(_package_id, Unset):
            package_id = UNSET
        else:
            package_id = UUID(_package_id)

        user_password_reset_request = cls(
            package_id=package_id,
        )

        user_password_reset_request.additional_properties = d
        return user_password_reset_request

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
