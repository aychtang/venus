# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.organization_id import OrganizationId
from ...commons.types.user_id import UserId


class AddUserToOrgRequest(pydantic.BaseModel):
    user_id: UserId = pydantic.Field(alias="userId")
    org_id: OrganizationId = pydantic.Field(alias="orgId")

    class Partial(typing_extensions.TypedDict):
        user_id: typing_extensions.NotRequired[UserId]
        org_id: typing_extensions.NotRequired[OrganizationId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @AddUserToOrgRequest.Validators.root
            def validate(values: AddUserToOrgRequest.Partial) -> AddUserToOrgRequest.Partial:
                ...

            @AddUserToOrgRequest.Validators.field("user_id")
            def validate_user_id(user_id: UserId, values: AddUserToOrgRequest.Partial) -> UserId:
                ...

            @AddUserToOrgRequest.Validators.field("org_id")
            def validate_org_id(org_id: OrganizationId, values: AddUserToOrgRequest.Partial) -> OrganizationId:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[AddUserToOrgRequest.Partial], AddUserToOrgRequest.Partial]]
        ] = []
        _user_id_validators: typing.ClassVar[typing.List[AddUserToOrgRequest.Validators.UserIdValidator]] = []
        _org_id_validators: typing.ClassVar[typing.List[AddUserToOrgRequest.Validators.OrgIdValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[AddUserToOrgRequest.Partial], AddUserToOrgRequest.Partial]
        ) -> typing.Callable[[AddUserToOrgRequest.Partial], AddUserToOrgRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["user_id"]
        ) -> typing.Callable[
            [AddUserToOrgRequest.Validators.UserIdValidator], AddUserToOrgRequest.Validators.UserIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["org_id"]
        ) -> typing.Callable[
            [AddUserToOrgRequest.Validators.OrgIdValidator], AddUserToOrgRequest.Validators.OrgIdValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "user_id":
                    cls._user_id_validators.append(validator)
                if field_name == "org_id":
                    cls._org_id_validators.append(validator)
                return validator

            return decorator

        class UserIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: UserId, __values: AddUserToOrgRequest.Partial) -> UserId:
                ...

        class OrgIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: OrganizationId, __values: AddUserToOrgRequest.Partial) -> OrganizationId:
                ...

    @pydantic.root_validator
    def _validate(cls, values: AddUserToOrgRequest.Partial) -> AddUserToOrgRequest.Partial:
        for validator in AddUserToOrgRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("user_id")
    def _validate_user_id(cls, v: UserId, values: AddUserToOrgRequest.Partial) -> UserId:
        for validator in AddUserToOrgRequest.Validators._user_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("org_id")
    def _validate_org_id(cls, v: OrganizationId, values: AddUserToOrgRequest.Partial) -> OrganizationId:
        for validator in AddUserToOrgRequest.Validators._org_id_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True