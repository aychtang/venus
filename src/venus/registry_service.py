from fastapi import Depends
from fern.nursery.pydantic.token import CreateTokenRequest
from fern.nursery.pydantic.token import RevokeTokenRequest

import venus.generated.server.resources as fern

from venus.auth.auth0_client import Auth0Client
from venus.generated.server.resources.commons.errors import UnauthorizedError
from venus.generated.server.resources.registry.service.service import (
    AbstractRegistryService,
)
from venus.generated.server.security import ApiAuth
from venus.global_dependencies import get_auth0
from venus.global_dependencies import get_nursery_client
from venus.nursery.client import NurseryApiClient
from venus.nursery.resources.token.types.get_token_metadata_request import (
    GetTokenMetadataRequest,
)
from venus.nursery_owner_data import read_nursery_org_data
from venus.utils import is_member_of_org


class RegistryService(AbstractRegistryService):
    def generate_registry_tokens(
        self,
        body: fern.GenerateRegistryTokensRequest,
        auth: ApiAuth,
        nursery_client: NurseryApiClient = Depends(get_nursery_client),
        auth0_client: Auth0Client = Depends(get_auth0),
    ) -> fern.RegistryTokens:
        is_member = is_member_of_org(
            body.organization_id.get_as_str(),
            auth,
            auth0_client,
            nursery_client,
        )
        if not is_member:
            raise UnauthorizedError()
        create_token_response = nursery_client.token.create(
            body=CreateTokenRequest(
                owner_id=body.organization_id.get_as_str(), prefix="fern"
            )
        )
        if create_token_response.ok:
            return fern.RegistryTokens(
                npm=fern.NpmRegistryToken(
                    token=create_token_response.body.token
                ),
                maven=fern.MavenRegistryToken(
                    username=body.organization_id.get_as_str(),
                    password=create_token_response.body.token,
                ),
            )
        else:
            raise Exception(
                f"Failed to generate token for org: {body.organization_id}",
                create_token_response.error,
            )

    def has_registry_permission(
        self,
        body: fern.CheckRegistryPermissionRequest,
        nursery_client: NurseryApiClient = Depends(get_nursery_client),
    ) -> bool:
        get_owner_response = nursery_client.owner.get(
            owner_id=body.organization_id.get_as_str()
        )
        if not get_owner_response.ok:
            raise Exception("Failed to load organization")
        nursery_org_data = read_nursery_org_data(get_owner_response.body.data)
        if not nursery_org_data.artifact_read_requires_token:
            return True
        elif body.token is None:
            raise Exception("Token is required to auth")
        else:
            token = body.token.visit(
                lambda npm: npm.token, lambda maven: maven.password
            )
            token_metadata_response = nursery_client.token.get_token_metadata(
                body=GetTokenMetadataRequest(token=token)
            )
            if token_metadata_response.ok:
                status = token_metadata_response.body.status.get_as_union()
                return status.type == "active"
            else:
                return False

    def revoke_token(
        self,
        body: fern.RevokeTokenRequest,
        auth: ApiAuth,
        nursery_client: NurseryApiClient = Depends(get_nursery_client),
        auth0_client: Auth0Client = Depends(get_auth0),
    ) -> None:
        is_member = is_member_of_org(
            body.organization_id.get_as_str(),
            auth,
            auth0_client,
            nursery_client,
        )
        if not is_member:
            raise UnauthorizedError()
        nursery_client.token.revoke_token(
            body=RevokeTokenRequest(token=body.token)
        )
