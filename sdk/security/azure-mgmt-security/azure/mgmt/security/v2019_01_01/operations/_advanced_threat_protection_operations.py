# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Literal, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(resource_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2019-01-01"))
    setting_name: Literal["current"] = kwargs.pop("setting_name", "current")
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/{resourceId}/providers/Microsoft.Security/advancedThreatProtectionSettings/{settingName}"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceId": _SERIALIZER.url("resource_id", resource_id, "str", skip_quote=True),
        "settingName": _SERIALIZER.url("setting_name", setting_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_request(resource_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2019-01-01"))
    setting_name: Literal["current"] = kwargs.pop("setting_name", "current")
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/{resourceId}/providers/Microsoft.Security/advancedThreatProtectionSettings/{settingName}"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceId": _SERIALIZER.url("resource_id", resource_id, "str", skip_quote=True),
        "settingName": _SERIALIZER.url("setting_name", setting_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


class AdvancedThreatProtectionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2019_01_01.SecurityCenter`'s
        :attr:`advanced_threat_protection` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def get(self, resource_id: str, **kwargs: Any) -> _models.AdvancedThreatProtectionSetting:
        """Gets the Advanced Threat Protection settings for the specified resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :return: AdvancedThreatProtectionSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-01-01"))
        setting_name: Literal["current"] = kwargs.pop("setting_name", "current")
        cls: ClsType[_models.AdvancedThreatProtectionSetting] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_id=resource_id,
            api_version=api_version,
            setting_name=setting_name,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdvancedThreatProtectionSetting", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create(
        self,
        resource_id: str,
        advanced_threat_protection_setting: _models.AdvancedThreatProtectionSetting,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AdvancedThreatProtectionSetting:
        """Creates or updates the Advanced Threat Protection settings on a specified resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param advanced_threat_protection_setting: Advanced Threat Protection Settings. Required.
        :type advanced_threat_protection_setting:
         ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AdvancedThreatProtectionSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self,
        resource_id: str,
        advanced_threat_protection_setting: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AdvancedThreatProtectionSetting:
        """Creates or updates the Advanced Threat Protection settings on a specified resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param advanced_threat_protection_setting: Advanced Threat Protection Settings. Required.
        :type advanced_threat_protection_setting: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AdvancedThreatProtectionSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self,
        resource_id: str,
        advanced_threat_protection_setting: Union[_models.AdvancedThreatProtectionSetting, IO[bytes]],
        **kwargs: Any
    ) -> _models.AdvancedThreatProtectionSetting:
        """Creates or updates the Advanced Threat Protection settings on a specified resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param advanced_threat_protection_setting: Advanced Threat Protection Settings. Is either a
         AdvancedThreatProtectionSetting type or a IO[bytes] type. Required.
        :type advanced_threat_protection_setting:
         ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting or IO[bytes]
        :return: AdvancedThreatProtectionSetting or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2019_01_01.models.AdvancedThreatProtectionSetting
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-01-01"))
        setting_name: Literal["current"] = kwargs.pop("setting_name", "current")
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AdvancedThreatProtectionSetting] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(advanced_threat_protection_setting, (IOBase, bytes)):
            _content = advanced_threat_protection_setting
        else:
            _json = self._serialize.body(advanced_threat_protection_setting, "AdvancedThreatProtectionSetting")

        _request = build_create_request(
            resource_id=resource_id,
            api_version=api_version,
            setting_name=setting_name,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdvancedThreatProtectionSetting", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
