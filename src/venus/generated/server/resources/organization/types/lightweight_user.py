# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime


class LightweightUser(pydantic.BaseModel):
    user_id: str = pydantic.Field(alias="userId")
    display_name: str = pydantic.Field(alias="displayName")
    picture_url: typing.Optional[str]

    class Partial(typing_extensions.TypedDict):
        user_id: typing_extensions.NotRequired[str]
        display_name: typing_extensions.NotRequired[str]
        picture_url: typing_extensions.NotRequired[typing.Optional[str]]

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
        json_encoders = {dt.datetime: serialize_datetime}
