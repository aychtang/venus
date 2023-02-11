# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .maven_registry_token import MavenRegistryToken
from .npm_registry_token import NpmRegistryToken


class RegistryTokens(pydantic.BaseModel):
    npm: NpmRegistryToken
    maven: MavenRegistryToken

    class Partial(typing_extensions.TypedDict):
        npm: typing_extensions.NotRequired[NpmRegistryToken]
        maven: typing_extensions.NotRequired[MavenRegistryToken]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
