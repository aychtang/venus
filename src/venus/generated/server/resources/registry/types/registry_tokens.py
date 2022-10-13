# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .maven_registry_token import MavenRegistryToken
from .npm_registry_token import NpmRegistryToken


class RegistryTokens(pydantic.BaseModel):
    npm: NpmRegistryToken
    maven: MavenRegistryToken

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @RegistryTokens.Validators.field("npm")
            def validate_npm(v: NpmRegistryToken, values: RegistryTokens.Partial) -> NpmRegistryToken:
                ...

            @RegistryTokens.Validators.field("maven")
            def validate_maven(v: MavenRegistryToken, values: RegistryTokens.Partial) -> MavenRegistryToken:
                ...
        """

        _npm_validators: typing.ClassVar[typing.List[RegistryTokens.Validators.NpmValidator]] = []
        _maven_validators: typing.ClassVar[typing.List[RegistryTokens.Validators.MavenValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["npm"]
        ) -> typing.Callable[[RegistryTokens.Validators.NpmValidator], RegistryTokens.Validators.NpmValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["maven"]
        ) -> typing.Callable[[RegistryTokens.Validators.MavenValidator], RegistryTokens.Validators.MavenValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "npm":
                    cls._npm_validators.append(validator)
                if field_name == "maven":
                    cls._maven_validators.append(validator)
                return validator

            return decorator

        class NpmValidator(typing_extensions.Protocol):
            def __call__(self, v: NpmRegistryToken, *, values: RegistryTokens.Partial) -> NpmRegistryToken:
                ...

        class MavenValidator(typing_extensions.Protocol):
            def __call__(self, v: MavenRegistryToken, *, values: RegistryTokens.Partial) -> MavenRegistryToken:
                ...

    @pydantic.validator("npm")
    def _validate_npm(cls, v: NpmRegistryToken, values: RegistryTokens.Partial) -> NpmRegistryToken:
        for validator in RegistryTokens.Validators._npm_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("maven")
    def _validate_maven(cls, v: MavenRegistryToken, values: RegistryTokens.Partial) -> MavenRegistryToken:
        for validator in RegistryTokens.Validators._maven_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        npm: typing_extensions.NotRequired[NpmRegistryToken]
        maven: typing_extensions.NotRequired[MavenRegistryToken]

    class Config:
        frozen = True