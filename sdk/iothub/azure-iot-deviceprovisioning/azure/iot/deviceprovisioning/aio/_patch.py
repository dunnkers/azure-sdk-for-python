# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from typing import TYPE_CHECKING, Any, Union, List

from azure.core.credentials import AzureNamedKeyCredential, AzureSasCredential
from azure.core.pipeline import AsyncPipeline
from azure.core.pipeline.policies import (
    AsyncBearerTokenCredentialPolicy,
    AsyncRetryPolicy,
    ContentDecodePolicy,
    DistributedTracingPolicy,
    HeadersPolicy,
    HttpLoggingPolicy,
    NetworkTraceLoggingPolicy,
    UserAgentPolicy,
)
from azure.core.utils import parse_connection_string

from .._api_version import DEFAULT_VERSION, ApiVersion
from .._auth import SasCredentialPolicy, SharedKeyCredentialPolicy
from .._version import VERSION
from ._client import (
    DeviceProvisioningClient as GeneratedDeviceProvisioningClient,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class DeviceProvisioningClient(
    GeneratedDeviceProvisioningClient
):  # pylint: disable=client-accepts-api-version-keyword
    """
    API for connecting to, and conducting operations on a Device Provisioning Service instance

    :param str endpoint: The HTTP endpoint of the Device Provisioning Service instance
    :param credential: The credential type used to authenticate with the Device Provisioning Service instance
    :type credential:
        ~azure.core.credentials.AzureNamedKeyCredential or
        ~azure.core.credentials.AzureSasCredential or
        ~azure.core.credentials_async.AsyncTokenCredential
    :keyword api_version: The Device Provisioning Service API version to use for requests. Default value is the most
        recent service version that is compatible with the current SDK. Setting to an older version may result
        in reduced feature compatibility.
    :paramtype api_version: str or ApiVersion
    :ivar enrollment: EnrollmentOperations operations
    :vartype enrollment:
        ~azure.iot.deviceprovisioningservice.aio.operations.EnrollmentOperations
    :ivar enrollment_group: EnrollmentGroupOperations operations
    :vartype enrollment_group:
        ~azure.iot.deviceprovisioningservice.aio.operations.EnrollmentGroupOperations
    :ivar device_registration_state: DeviceRegistrationStateOperations operations
    :vartype device_registration_state:
        ~azure.iot.deviceprovisioningservice.aio.operations.DeviceRegistrationStateOperations
    """

    def __init__(
        self,
        endpoint: str,
        credential: Union[
            "AzureNamedKeyCredential",
            "AzureSasCredential",
            "AsyncTokenCredential",
        ],
        *,
        api_version: Union[str, ApiVersion] = DEFAULT_VERSION,
        **kwargs: Any,
    ) -> None:
        self._pipeline = self._create_pipeline(
            credential=credential, base_url=endpoint, **kwargs
        )

        # Validate endpoint
        try:
            if not endpoint.lower().startswith("http"):
                endpoint = "https://" + endpoint
        except AttributeError:
            raise ValueError("Endpoint URL must be a string.")
        endpoint = endpoint.rstrip("/")

        # Validate api-version
        try:
            api_version = ApiVersion(api_version).value
        except ValueError:
            raise ValueError(f"Invalid api-version {api_version} specified")

        # Generate protocol client
        super().__init__(
            credential=credential,  # type: ignore
            endpoint=endpoint,
            pipeline=self._pipeline,
            api_version=api_version,
            **kwargs,
        )

    @classmethod
    def from_connection_string(
        cls,
        connection_string: str,
        *,
        api_version: Union[str, ApiVersion] = DEFAULT_VERSION,
        **kwargs: Any,
    ) -> "DeviceProvisioningClient":
        """
        Create a Provisioning Service Client from a connection string

        :param str connection_string: The connection string for the Device Provisioning Service instance
        :keyword api_version: The Device Provisioning Service API version to use for requests. Default value is the most
            recent service version that is compatible with the current SDK. Setting to an older version may result
            in reduced feature compatibility.
        :paramtype api_version: str or ApiVersion
        :return: A new instance of :class:`DeviceProvisioningClient
            <azure.iot.deviceprovisioningservice.aio.DeviceProvisioningClient>`
        :rtype: :class:`DeviceProvisioningClient
            <azure.iot.deviceprovisioningservice.aio.DeviceProvisioningClient>`
        :raises: ValueError if connection string is invalid
        """
        cs_args = parse_connection_string(connection_string)
        for k in ["hostname", "sharedaccesskeyname", "sharedaccesskey"]:
            if not cs_args.get(k):
                raise ValueError(f"IoT DPS connection string has missing property: {k}")

        host_name, shared_access_key_name, shared_access_key = (
            cs_args["hostname"],
            cs_args["sharedaccesskeyname"],
            cs_args["sharedaccesskey"],
        )

        # Create credential from keys
        credential = AzureNamedKeyCredential(
            name=shared_access_key_name, key=shared_access_key
        )

        return cls(endpoint=host_name, credential=credential, api_version=api_version, **kwargs)  # type: ignore

    def _create_pipeline(
        self,
        credential: Union[
            "AzureNamedKeyCredential",
            "AzureSasCredential",
            "AsyncTokenCredential",
        ],
        base_url: str,
        **kwargs: Any,
    ) -> AsyncPipeline:
        transport = kwargs.get("transport")
        user_agent_policy = kwargs.get("user_agent_policy") or UserAgentPolicy(
            sdk_moniker=f"az-iot-dps-python/{VERSION}", **kwargs
        )

        # Choose appropriate credential policy
        self._credential_policy = None  # type: ignore
        if hasattr(credential, "get_token"):
            self._credential_policy = AsyncBearerTokenCredentialPolicy(  # type: ignore
                credential, "https://azure-devices-provisioning.net/.default"  # type: ignore
            )
        elif isinstance(credential, AzureSasCredential):
            self._credential_policy = SasCredentialPolicy(credential=credential)  # type: ignore
        elif isinstance(credential, AzureNamedKeyCredential):
            name = credential.named_key.name
            key = credential.named_key.key
            self._credential_policy = SharedKeyCredentialPolicy(  # type: ignore
                endpoint=base_url, key=key, policy_name=name
            )
        elif credential is not None:
            raise TypeError(f"Unsupported credential: {type(credential)}")

        transport = kwargs.get("transport", None)
        if not transport:
            try:
                from azure.core.pipeline.transport import AioHttpTransport
            except ImportError:
                raise ImportError(
                    "Unable to create async transport. Please check aiohttp is installed."
                )
            transport = AioHttpTransport(**kwargs)

        policies = [
            user_agent_policy,
            self._credential_policy,  # type: ignore
            HeadersPolicy(**kwargs),
            UserAgentPolicy(**kwargs),
            ContentDecodePolicy(**kwargs),
            AsyncRetryPolicy(**kwargs),
            HttpLoggingPolicy(**kwargs),
            DistributedTracingPolicy(**kwargs),
            NetworkTraceLoggingPolicy(**kwargs),
        ]
        # add additional policies from kwargs
        if kwargs.get("_additional_pipeline_policies"):
            policies.extend([kwargs.get("_additional_pipeline_policies")])

        return AsyncPipeline(transport, policies=policies)  # type: ignore

__all__: List[str] = [
    "DeviceProvisioningClient"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
