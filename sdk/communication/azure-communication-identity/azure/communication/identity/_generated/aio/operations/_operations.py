# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ...operations._operations import (
    build_communication_identity_create_request,
    build_communication_identity_delete_request,
    build_communication_identity_exchange_teams_user_access_token_request,
    build_communication_identity_issue_access_token_request,
    build_communication_identity_revoke_access_tokens_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CommunicationIdentityOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.communication.identity.aio.CommunicationIdentityClient`'s
        :attr:`communication_identity` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create(
        self, body: Optional[JSON] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a new identity, and optionally, an access token.

        Create a new identity, and optionally, an access token.

        :param body: If specified, creates also a Communication Identity access token associated with
         the identity and containing the requested scopes. Default value is None.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "createTokenWithScopes": [
                        "str"  # Optional. Also create access token for the created identity.
                    ],
                    "expiresInMinutes": 1440  # Optional. Default value is 1440. Optional custom
                      validity period of the token within [60,1440] minutes range. If not provided, the
                      default value of 1440 minutes (24 hours) will be used.
                }

                # response body for status code(s): 201
                response == {
                    "identity": {
                        "id": "str"  # Identifier of the identity. Required.
                    },
                    "accessToken": {
                        "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                          Required.
                        "token": "str"  # The access token issued for the identity. Required.
                    }
                }
        """

    @overload
    async def create(self, body: Optional[IO] = None, *, content_type: str = "application/json", **kwargs: Any) -> JSON:
        """Create a new identity, and optionally, an access token.

        Create a new identity, and optionally, an access token.

        :param body: If specified, creates also a Communication Identity access token associated with
         the identity and containing the requested scopes. Default value is None.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 201
                response == {
                    "identity": {
                        "id": "str"  # Identifier of the identity. Required.
                    },
                    "accessToken": {
                        "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                          Required.
                        "token": "str"  # The access token issued for the identity. Required.
                    }
                }
        """

    @distributed_trace_async
    async def create(self, body: Optional[Union[JSON, IO]] = None, **kwargs: Any) -> JSON:
        """Create a new identity, and optionally, an access token.

        Create a new identity, and optionally, an access token.

        :param body: If specified, creates also a Communication Identity access token associated with
         the identity and containing the requested scopes. Is either a model type or a IO type. Default
         value is None.
        :type body: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 201
                response == {
                    "identity": {
                        "id": "str"  # Identifier of the identity. Required.
                    },
                    "accessToken": {
                        "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                          Required.
                        "token": "str"  # The access token issued for the identity. Required.
                    }
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            if body is not None:
                _json = body
            else:
                _json = None

        request = build_communication_identity_create_request(
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @distributed_trace_async
    async def delete(self, id: str, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Delete the identity, revoke all tokens for the identity and delete all associated data.

        Delete the identity, revoke all tokens for the identity and delete all associated data.

        :param id: Identifier of the identity to be deleted. Required.
        :type id: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_communication_identity_delete_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def revoke_access_tokens(  # pylint: disable=inconsistent-return-statements
        self, id: str, **kwargs: Any
    ) -> None:
        """Revoke all access tokens for the specific identity.

        Revoke all access tokens for the specific identity.

        :param id: Identifier of the identity. Required.
        :type id: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_communication_identity_revoke_access_tokens_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    async def exchange_teams_user_access_token(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        :param body: Request payload for the token exchange. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "appId": "str",  # Client ID of an Azure AD application to be verified
                      against the appid claim in the Azure AD access token. Required.
                    "token": "str",  # Azure AD access token of a Teams User to acquire a new
                      Communication Identity access token. Required.
                    "userId": "str"  # Object ID of an Azure AD user (Teams User) to be verified
                      against the oid claim in the Azure AD access token. Required.
                }

                # response body for status code(s): 200
                response == {
                    "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                      Required.
                    "token": "str"  # The access token issued for the identity. Required.
                }
        """

    @overload
    async def exchange_teams_user_access_token(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        :param body: Request payload for the token exchange. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                      Required.
                    "token": "str"  # The access token issued for the identity. Required.
                }
        """

    @distributed_trace_async
    async def exchange_teams_user_access_token(self, body: Union[JSON, IO], **kwargs: Any) -> JSON:
        """Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        Exchange an Azure Active Directory (Azure AD) access token of a Teams user for a new
        Communication Identity access token with a matching expiration time.

        :param body: Request payload for the token exchange. Is either a model type or a IO type.
         Required.
        :type body: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                      Required.
                    "token": "str"  # The access token issued for the identity. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = body

        request = build_communication_identity_exchange_teams_user_access_token_request(
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def issue_access_token(
        self, id: str, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Issue a new token for an identity.

        Issue a new token for an identity.

        :param id: Identifier of the identity to issue token for. Required.
        :type id: str
        :param body: Requested scopes for the new token. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "scopes": [
                        "str"  # List of scopes attached to the token. Required.
                    ],
                    "expiresInMinutes": 1440  # Optional. Default value is 1440. Optional custom
                      validity period of the token within [60,1440] minutes range. If not provided, the
                      default value of 1440 minutes (24 hours) will be used.
                }

                # response body for status code(s): 200
                response == {
                    "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                      Required.
                    "token": "str"  # The access token issued for the identity. Required.
                }
        """

    @overload
    async def issue_access_token(
        self, id: str, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Issue a new token for an identity.

        Issue a new token for an identity.

        :param id: Identifier of the identity to issue token for. Required.
        :type id: str
        :param body: Requested scopes for the new token. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                      Required.
                    "token": "str"  # The access token issued for the identity. Required.
                }
        """

    @distributed_trace_async
    async def issue_access_token(self, id: str, body: Union[JSON, IO], **kwargs: Any) -> JSON:
        """Issue a new token for an identity.

        Issue a new token for an identity.

        :param id: Identifier of the identity to issue token for. Required.
        :type id: str
        :param body: Requested scopes for the new token. Is either a model type or a IO type. Required.
        :type body: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "expiresOn": "2020-02-20 00:00:00",  # The expiry time of the token.
                      Required.
                    "token": "str"  # The access token issued for the identity. Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = body

        request = build_communication_identity_issue_access_token_request(
            id=id,
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)
