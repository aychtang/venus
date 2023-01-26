# This file was auto-generated by Fern from our API Definition.

import datetime as dt
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

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: lambda v: v.isoformat()}
