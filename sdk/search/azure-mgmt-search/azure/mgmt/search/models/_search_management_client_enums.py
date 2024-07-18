# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AadAuthFailureMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes what response the data plane API of a search service would send for requests that
    failed authentication.
    """

    HTTP403 = "http403"
    """Indicates that requests that failed authentication should be presented with an HTTP status code
    of 403 (Forbidden)."""
    HTTP401_WITH_BEARER_CHALLENGE = "http401WithBearerChallenge"
    """Indicates that requests that failed authentication should be presented with an HTTP status code
    of 401 (Unauthorized) and present a Bearer Challenge."""


class AdminKeyKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AdminKeyKind."""

    PRIMARY = "primary"
    """The primary API key for the search service."""
    SECONDARY = "secondary"
    """The secondary API key for the search service."""


class HostingMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density
    partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed
    for any other SKU. For the standard3 SKU, the value is either 'default' or 'highDensity'. For
    all other SKUs, this value must be 'default'.
    """

    DEFAULT = "default"
    """The limit on number of indexes is determined by the default limits for the SKU."""
    HIGH_DENSITY = "highDensity"
    """Only application for standard3 SKU, where the search service can have up to 1000 indexes."""


class IdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes
    both an identity created by the system and a set of user assigned identities. The type 'None'
    will remove all identities from the service.
    """

    NONE = "None"
    """Indicates that any identity associated with the search service needs to be removed."""
    SYSTEM_ASSIGNED = "SystemAssigned"
    """Indicates that system-assigned identity for the search service will be enabled."""
    USER_ASSIGNED = "UserAssigned"
    """Indicates that one or more user assigned identities will be assigned to the search service."""
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    """Indicates that system-assigned identity for the search service will be enabled along with the
    assignment of one or more user assigned identities."""


class PrivateLinkServiceConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the private link service connection. Valid values are Updating,
    Deleting, Failed, Succeeded, Incomplete, or Canceled.
    """

    UPDATING = "Updating"
    """The private link service connection is in the process of being created along with other
    resources for it to be fully functional."""
    DELETING = "Deleting"
    """The private link service connection is in the process of being deleted."""
    FAILED = "Failed"
    """The private link service connection has failed to be provisioned or deleted."""
    SUCCEEDED = "Succeeded"
    """The private link service connection has finished provisioning and is ready for approval."""
    INCOMPLETE = "Incomplete"
    """Provisioning request for the private link service connection resource has been accepted but the
    process of creation has not commenced yet."""
    CANCELED = "Canceled"
    """Provisioning request for the private link service connection resource has been canceled."""


class PrivateLinkServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the the private link service connection. Valid values are Pending, Approved,
    Rejected, or Disconnected.
    """

    PENDING = "Pending"
    """The private endpoint connection has been created and is pending approval."""
    APPROVED = "Approved"
    """The private endpoint connection is approved and is ready for use."""
    REJECTED = "Rejected"
    """The private endpoint connection has been rejected and cannot be used."""
    DISCONNECTED = "Disconnected"
    """The private endpoint connection has been removed from the service."""


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the last provisioning operation performed on the search service. Provisioning is
    an intermediate state that occurs while service capacity is being established. After capacity
    is set up, provisioningState changes to either 'Succeeded' or 'Failed'. Client applications can
    poll provisioning status (the recommended polling interval is from 30 seconds to one minute) by
    using the Get Search Service operation to see when an operation is completed. If you are using
    the free service, this value tends to come back as 'Succeeded' directly in the call to Create
    search service. This is because the free service uses capacity that is already set up.
    """

    SUCCEEDED = "Succeeded"
    """The last provisioning operation has completed successfully."""
    PROVISIONING = "Provisioning"
    """The search service is being provisioned or scaled up or down."""
    FAILED = "Failed"
    """The last provisioning operation has failed."""


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This value can be set to 'enabled' to avoid breaking changes on existing customer resources and
    templates. If set to 'disabled', traffic over public interface is not allowed, and private
    endpoint connections would be the exclusive access method.
    """

    ENABLED = "enabled"
    """The search service is accessible from traffic originating from the public internet."""
    DISABLED = "disabled"
    """The search service is not accessible from traffic originating from the public internet. Access
    is only permitted over approved private endpoint connections."""


class SearchBypass(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Possible origins of inbound traffic that can bypass the rules defined in the 'ipRules' section."""

    NONE = "None"
    """Indicates that no origin can bypass the rules defined in the 'ipRules' section. This is the
    default."""
    AZURE_PORTAL = "AzurePortal"
    """Indicates that requests originating from the Azure portal can bypass the rules defined in the
    'ipRules' section."""
    AZURE_SERVICES = "AzureServices"
    """Indicates that requests originating from Azure trusted services can bypass the rules defined in
    the 'ipRules' section."""


class SearchDisabledDataExfiltrationOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A specific data exfiltration scenario that is disabled for the service."""

    ALL = "All"
    """Indicates that all data exfiltration scenarios are disabled."""


class SearchEncryptionComplianceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Returns the status of search service compliance with respect to non-CMK-encrypted objects. If a
    service has more than one unencrypted object, and enforcement is enabled, the service is marked
    as noncompliant.
    """

    COMPLIANT = "Compliant"
    """Indicates that the search service is compliant, either because the number of non-CMK-encrypted
    objects is zero or enforcement is disabled."""
    NON_COMPLIANT = "NonCompliant"
    """Indicates that the search service has more than one non-CMK-encrypted objects."""


class SearchEncryptionWithCmk(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes how a search service should enforce compliance if it finds objects that aren't
    encrypted with the customer-managed key.
    """

    DISABLED = "Disabled"
    """No enforcement of customer-managed key encryption will be made. Only the built-in
    service-managed encryption is used."""
    ENABLED = "Enabled"
    """Search service will be marked as non-compliant if one or more objects aren't encrypted with a
    customer-managed key."""
    UNSPECIFIED = "Unspecified"
    """Enforcement policy is not explicitly specified, with the behavior being the same as if it were
    set to 'Disabled'."""


class SearchSemanticSearch(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sets options that control the availability of semantic search. This configuration is only
    possible for certain Azure AI Search SKUs in certain locations.
    """

    DISABLED = "disabled"
    """Indicates that semantic reranker is disabled for the search service. This is the default."""
    FREE = "free"
    """Enables semantic reranker on a search service and indicates that it is to be used within the
    limits of the free plan. The free plan would cap the volume of semantic ranking requests and is
    offered at no extra charge. This is the default for newly provisioned search services."""
    STANDARD = "standard"
    """Enables semantic reranker on a search service as a billable feature, with higher throughput and
    volume of semantically reranked queries."""


class SearchServiceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the search service. Possible values include: 'running': The search service is
    running and no provisioning operations are underway. 'provisioning': The search service is
    being provisioned or scaled up or down. 'deleting': The search service is being deleted.
    'degraded': The search service is degraded. This can occur when the underlying search units are
    not healthy. The search service is most likely operational, but performance might be slow and
    some requests might be dropped. 'disabled': The search service is disabled. In this state, the
    service will reject all API requests. 'error': The search service is in an error state.
    'stopped': The search service is in a subscription that's disabled. If your service is in the
    degraded, disabled, or error states, it means the Azure AI Search team is actively
    investigating the underlying issue. Dedicated services in these states are still chargeable
    based on the number of search units provisioned.
    """

    RUNNING = "running"
    """The search service is running and no provisioning operations are underway."""
    PROVISIONING = "provisioning"
    """The search service is being provisioned or scaled up or down."""
    DELETING = "deleting"
    """The search service is being deleted."""
    DEGRADED = "degraded"
    """The search service is degraded because underlying search units are not healthy."""
    DISABLED = "disabled"
    """The search service is disabled and all API requests will be rejected."""
    ERROR = "error"
    """The search service is in error state, indicating either a failure to provision or to be
    deleted."""
    STOPPED = "stopped"
    """The search service is in a subscription that's disabled."""


class SharedPrivateLinkResourceAsyncOperationResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current status of the long running asynchronous shared private link resource operation."""

    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class SharedPrivateLinkResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the shared private link resource. Valid values are Updating,
    Deleting, Failed, Succeeded or Incomplete.
    """

    UPDATING = "Updating"
    """The shared private link resource is in the process of being created along with other resources
    for it to be fully functional."""
    DELETING = "Deleting"
    """The shared private link resource is in the process of being deleted."""
    FAILED = "Failed"
    """The shared private link resource has failed to be provisioned or deleted."""
    SUCCEEDED = "Succeeded"
    """The shared private link resource has finished provisioning and is ready for approval."""
    INCOMPLETE = "Incomplete"
    """Provisioning request for the shared private link resource has been accepted but the process of
    creation has not commenced yet."""


class SharedPrivateLinkResourceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the shared private link resource. Valid values are Pending, Approved, Rejected or
    Disconnected.
    """

    PENDING = "Pending"
    """The shared private link resource has been created and is pending approval."""
    APPROVED = "Approved"
    """The shared private link resource is approved and is ready for use."""
    REJECTED = "Rejected"
    """The shared private link resource has been rejected and cannot be used."""
    DISCONNECTED = "Disconnected"
    """The shared private link resource has been removed from the service."""


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU of the search service. Valid values include: 'free': Shared service. 'basic': Dedicated
    service with up to 3 replicas. 'standard': Dedicated service with up to 12 partitions and 12
    replicas. 'standard2': Similar to standard, but with more capacity per search unit.
    'standard3': The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3
    partitions with more indexes if you also set the hostingMode property to 'highDensity').
    'storage_optimized_l1': Supports 1TB per partition, up to 12 partitions.
    'storage_optimized_l2': Supports 2TB per partition, up to 12 partitions.'.
    """

    FREE = "free"
    """Free tier, with no SLA guarantees and a subset of the features offered on billable tiers."""
    BASIC = "basic"
    """Billable tier for a dedicated service having up to 3 replicas."""
    STANDARD = "standard"
    """Billable tier for a dedicated service having up to 12 partitions and 12 replicas."""
    STANDARD2 = "standard2"
    """Similar to 'standard', but with more capacity per search unit."""
    STANDARD3 = "standard3"
    """The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3 partitions
    with more indexes if you also set the hostingMode property to 'highDensity')."""
    STORAGE_OPTIMIZED_L1 = "storage_optimized_l1"
    """Billable tier for a dedicated service that supports 1TB per partition, up to 12 partitions."""
    STORAGE_OPTIMIZED_L2 = "storage_optimized_l2"
    """Billable tier for a dedicated service that supports 2TB per partition, up to 12 partitions."""


class UnavailableNameReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason why the name is not available. 'Invalid' indicates the name provided does not match
    the naming requirements (incorrect length, unsupported characters, etc.). 'AlreadyExists'
    indicates that the name is already in use and is therefore unavailable.
    """

    INVALID = "Invalid"
    """The search service name doesn't match naming requirements."""
    ALREADY_EXISTS = "AlreadyExists"
    """The search service name is already assigned to a different search service."""
