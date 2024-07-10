# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ARMProxyResource
from ._models_py3 import ARMResourceProperties
from ._models_py3 import AccountKeyMetadata
from ._models_py3 import AnalyticalStorageConfiguration
from ._models_py3 import ApiProperties
from ._models_py3 import AuthenticationMethodLdapProperties
from ._models_py3 import AutoUpgradePolicyResource
from ._models_py3 import AutoscaleSettings
from ._models_py3 import AutoscaleSettingsResource
from ._models_py3 import BackupInformation
from ._models_py3 import BackupPolicy
from ._models_py3 import BackupPolicyMigrationState
from ._models_py3 import Capability
from ._models_py3 import Capacity
from ._models_py3 import CassandraClusterDataCenterNodeItem
from ._models_py3 import CassandraClusterPublicStatus
from ._models_py3 import CassandraClusterPublicStatusDataCentersItem
from ._models_py3 import CassandraError
from ._models_py3 import CassandraKeyspaceCreateUpdateParameters
from ._models_py3 import CassandraKeyspaceGetPropertiesOptions
from ._models_py3 import CassandraKeyspaceGetPropertiesResource
from ._models_py3 import CassandraKeyspaceGetResults
from ._models_py3 import CassandraKeyspaceListResult
from ._models_py3 import CassandraKeyspaceResource
from ._models_py3 import CassandraPartitionKey
from ._models_py3 import CassandraSchema
from ._models_py3 import CassandraTableCreateUpdateParameters
from ._models_py3 import CassandraTableGetPropertiesOptions
from ._models_py3 import CassandraTableGetPropertiesResource
from ._models_py3 import CassandraTableGetResults
from ._models_py3 import CassandraTableListResult
from ._models_py3 import CassandraTableResource
from ._models_py3 import Certificate
from ._models_py3 import ClientEncryptionIncludedPath
from ._models_py3 import ClientEncryptionKeyCreateUpdateParameters
from ._models_py3 import ClientEncryptionKeyGetPropertiesResource
from ._models_py3 import ClientEncryptionKeyGetResults
from ._models_py3 import ClientEncryptionKeyResource
from ._models_py3 import ClientEncryptionKeysListResult
from ._models_py3 import ClientEncryptionPolicy
from ._models_py3 import ClusterKey
from ._models_py3 import ClusterResource
from ._models_py3 import ClusterResourceProperties
from ._models_py3 import Column
from ._models_py3 import CommandOutput
from ._models_py3 import CommandPostBody
from ._models_py3 import CompositePath
from ._models_py3 import ComputedProperty
from ._models_py3 import ConflictResolutionPolicy
from ._models_py3 import ConnectionError
from ._models_py3 import ConsistencyPolicy
from ._models_py3 import ContainerPartitionKey
from ._models_py3 import ContinuousBackupInformation
from ._models_py3 import ContinuousBackupRestoreLocation
from ._models_py3 import ContinuousModeBackupPolicy
from ._models_py3 import ContinuousModeProperties
from ._models_py3 import CorsPolicy
from ._models_py3 import CreateUpdateOptions
from ._models_py3 import DataCenterResource
from ._models_py3 import DataCenterResourceProperties
from ._models_py3 import DataTransferRegionalServiceResource
from ._models_py3 import DataTransferServiceResource
from ._models_py3 import DataTransferServiceResourceCreateUpdateProperties
from ._models_py3 import DataTransferServiceResourceProperties
from ._models_py3 import DatabaseAccountConnectionString
from ._models_py3 import DatabaseAccountCreateUpdateParameters
from ._models_py3 import DatabaseAccountGetResults
from ._models_py3 import DatabaseAccountKeysMetadata
from ._models_py3 import DatabaseAccountListConnectionStringsResult
from ._models_py3 import DatabaseAccountListKeysResult
from ._models_py3 import DatabaseAccountListReadOnlyKeysResult
from ._models_py3 import DatabaseAccountRegenerateKeyParameters
from ._models_py3 import DatabaseAccountUpdateParameters
from ._models_py3 import DatabaseAccountsListResult
from ._models_py3 import DatabaseRestoreResource
from ._models_py3 import ErrorResponse
from ._models_py3 import ExcludedPath
from ._models_py3 import ExtendedResourceProperties
from ._models_py3 import FailoverPolicies
from ._models_py3 import FailoverPolicy
from ._models_py3 import GraphAPIComputeRegionalServiceResource
from ._models_py3 import GraphAPIComputeServiceResource
from ._models_py3 import GraphAPIComputeServiceResourceCreateUpdateProperties
from ._models_py3 import GraphAPIComputeServiceResourceProperties
from ._models_py3 import GremlinDatabaseCreateUpdateParameters
from ._models_py3 import GremlinDatabaseGetPropertiesOptions
from ._models_py3 import GremlinDatabaseGetPropertiesResource
from ._models_py3 import GremlinDatabaseGetResults
from ._models_py3 import GremlinDatabaseListResult
from ._models_py3 import GremlinDatabaseResource
from ._models_py3 import GremlinDatabaseRestoreResource
from ._models_py3 import GremlinGraphCreateUpdateParameters
from ._models_py3 import GremlinGraphGetPropertiesOptions
from ._models_py3 import GremlinGraphGetPropertiesResource
from ._models_py3 import GremlinGraphGetResults
from ._models_py3 import GremlinGraphListResult
from ._models_py3 import GremlinGraphResource
from ._models_py3 import IncludedPath
from ._models_py3 import Indexes
from ._models_py3 import IndexingPolicy
from ._models_py3 import IpAddressOrRange
from ._models_py3 import KeyWrapMetadata
from ._models_py3 import ListClusters
from ._models_py3 import ListDataCenters
from ._models_py3 import Location
from ._models_py3 import LocationGetResult
from ._models_py3 import LocationListResult
from ._models_py3 import LocationProperties
from ._models_py3 import ManagedCassandraARMResourceProperties
from ._models_py3 import ManagedCassandraManagedServiceIdentity
from ._models_py3 import ManagedCassandraReaperStatus
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import ManagedServiceIdentityUserAssignedIdentity
from ._models_py3 import MaterializedViewsBuilderRegionalServiceResource
from ._models_py3 import MaterializedViewsBuilderServiceResource
from ._models_py3 import MaterializedViewsBuilderServiceResourceCreateUpdateProperties
from ._models_py3 import MaterializedViewsBuilderServiceResourceProperties
from ._models_py3 import Metric
from ._models_py3 import MetricAvailability
from ._models_py3 import MetricDefinition
from ._models_py3 import MetricDefinitionsListResult
from ._models_py3 import MetricListResult
from ._models_py3 import MetricName
from ._models_py3 import MetricValue
from ._models_py3 import MongoDBCollectionCreateUpdateParameters
from ._models_py3 import MongoDBCollectionGetPropertiesOptions
from ._models_py3 import MongoDBCollectionGetPropertiesResource
from ._models_py3 import MongoDBCollectionGetResults
from ._models_py3 import MongoDBCollectionListResult
from ._models_py3 import MongoDBCollectionResource
from ._models_py3 import MongoDBDatabaseCreateUpdateParameters
from ._models_py3 import MongoDBDatabaseGetPropertiesOptions
from ._models_py3 import MongoDBDatabaseGetPropertiesResource
from ._models_py3 import MongoDBDatabaseGetResults
from ._models_py3 import MongoDBDatabaseListResult
from ._models_py3 import MongoDBDatabaseResource
from ._models_py3 import MongoIndex
from ._models_py3 import MongoIndexKeys
from ._models_py3 import MongoIndexOptions
from ._models_py3 import MongoRoleDefinitionCreateUpdateParameters
from ._models_py3 import MongoRoleDefinitionGetResults
from ._models_py3 import MongoRoleDefinitionListResult
from ._models_py3 import MongoUserDefinitionCreateUpdateParameters
from ._models_py3 import MongoUserDefinitionGetResults
from ._models_py3 import MongoUserDefinitionListResult
from ._models_py3 import NotebookWorkspace
from ._models_py3 import NotebookWorkspaceConnectionInfoResult
from ._models_py3 import NotebookWorkspaceCreateUpdateParameters
from ._models_py3 import NotebookWorkspaceListResult
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OptionsResource
from ._models_py3 import PartitionMetric
from ._models_py3 import PartitionMetricListResult
from ._models_py3 import PartitionUsage
from ._models_py3 import PartitionUsagesResult
from ._models_py3 import PercentileMetric
from ._models_py3 import PercentileMetricListResult
from ._models_py3 import PercentileMetricValue
from ._models_py3 import PeriodicModeBackupPolicy
from ._models_py3 import PeriodicModeProperties
from ._models_py3 import Permission
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointProperty
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionStateProperty
from ._models_py3 import Privilege
from ._models_py3 import PrivilegeResource
from ._models_py3 import ProxyResource
from ._models_py3 import RegionForOnlineOffline
from ._models_py3 import RegionalServiceResource
from ._models_py3 import Resource
from ._models_py3 import ResourceRestoreParameters
from ._models_py3 import RestorableDatabaseAccountGetResult
from ._models_py3 import RestorableDatabaseAccountsListResult
from ._models_py3 import RestorableGremlinDatabaseGetResult
from ._models_py3 import RestorableGremlinDatabasePropertiesResource
from ._models_py3 import RestorableGremlinDatabasesListResult
from ._models_py3 import RestorableGremlinGraphGetResult
from ._models_py3 import RestorableGremlinGraphPropertiesResource
from ._models_py3 import RestorableGremlinGraphsListResult
from ._models_py3 import RestorableGremlinResourcesGetResult
from ._models_py3 import RestorableGremlinResourcesListResult
from ._models_py3 import RestorableLocationResource
from ._models_py3 import RestorableMongodbCollectionGetResult
from ._models_py3 import RestorableMongodbCollectionPropertiesResource
from ._models_py3 import RestorableMongodbCollectionsListResult
from ._models_py3 import RestorableMongodbDatabaseGetResult
from ._models_py3 import RestorableMongodbDatabasePropertiesResource
from ._models_py3 import RestorableMongodbDatabasesListResult
from ._models_py3 import RestorableMongodbResourcesGetResult
from ._models_py3 import RestorableMongodbResourcesListResult
from ._models_py3 import RestorableSqlContainerGetResult
from ._models_py3 import RestorableSqlContainerPropertiesResource
from ._models_py3 import RestorableSqlContainerPropertiesResourceContainer
from ._models_py3 import RestorableSqlContainersListResult
from ._models_py3 import RestorableSqlDatabaseGetResult
from ._models_py3 import RestorableSqlDatabasePropertiesResource
from ._models_py3 import RestorableSqlDatabasePropertiesResourceDatabase
from ._models_py3 import RestorableSqlDatabasesListResult
from ._models_py3 import RestorableSqlResourcesGetResult
from ._models_py3 import RestorableSqlResourcesListResult
from ._models_py3 import RestorableTableGetResult
from ._models_py3 import RestorableTablePropertiesResource
from ._models_py3 import RestorableTableResourcesGetResult
from ._models_py3 import RestorableTableResourcesListResult
from ._models_py3 import RestorableTablesListResult
from ._models_py3 import RestoreParameters
from ._models_py3 import RestoreParametersBase
from ._models_py3 import Role
from ._models_py3 import SeedNode
from ._models_py3 import ServiceResource
from ._models_py3 import ServiceResourceCreateUpdateParameters
from ._models_py3 import ServiceResourceCreateUpdateProperties
from ._models_py3 import ServiceResourceListResult
from ._models_py3 import ServiceResourceProperties
from ._models_py3 import SpatialSpec
from ._models_py3 import SqlContainerCreateUpdateParameters
from ._models_py3 import SqlContainerGetPropertiesOptions
from ._models_py3 import SqlContainerGetPropertiesResource
from ._models_py3 import SqlContainerGetResults
from ._models_py3 import SqlContainerListResult
from ._models_py3 import SqlContainerResource
from ._models_py3 import SqlDatabaseCreateUpdateParameters
from ._models_py3 import SqlDatabaseGetPropertiesOptions
from ._models_py3 import SqlDatabaseGetPropertiesResource
from ._models_py3 import SqlDatabaseGetResults
from ._models_py3 import SqlDatabaseListResult
from ._models_py3 import SqlDatabaseResource
from ._models_py3 import SqlDedicatedGatewayRegionalServiceResource
from ._models_py3 import SqlDedicatedGatewayServiceResource
from ._models_py3 import SqlDedicatedGatewayServiceResourceCreateUpdateProperties
from ._models_py3 import SqlDedicatedGatewayServiceResourceProperties
from ._models_py3 import SqlRoleAssignmentCreateUpdateParameters
from ._models_py3 import SqlRoleAssignmentGetResults
from ._models_py3 import SqlRoleAssignmentListResult
from ._models_py3 import SqlRoleDefinitionCreateUpdateParameters
from ._models_py3 import SqlRoleDefinitionGetResults
from ._models_py3 import SqlRoleDefinitionListResult
from ._models_py3 import SqlStoredProcedureCreateUpdateParameters
from ._models_py3 import SqlStoredProcedureGetPropertiesResource
from ._models_py3 import SqlStoredProcedureGetResults
from ._models_py3 import SqlStoredProcedureListResult
from ._models_py3 import SqlStoredProcedureResource
from ._models_py3 import SqlTriggerCreateUpdateParameters
from ._models_py3 import SqlTriggerGetPropertiesResource
from ._models_py3 import SqlTriggerGetResults
from ._models_py3 import SqlTriggerListResult
from ._models_py3 import SqlTriggerResource
from ._models_py3 import SqlUserDefinedFunctionCreateUpdateParameters
from ._models_py3 import SqlUserDefinedFunctionGetPropertiesResource
from ._models_py3 import SqlUserDefinedFunctionGetResults
from ._models_py3 import SqlUserDefinedFunctionListResult
from ._models_py3 import SqlUserDefinedFunctionResource
from ._models_py3 import SystemData
from ._models_py3 import TableCreateUpdateParameters
from ._models_py3 import TableGetPropertiesOptions
from ._models_py3 import TableGetPropertiesResource
from ._models_py3 import TableGetResults
from ._models_py3 import TableListResult
from ._models_py3 import TableResource
from ._models_py3 import ThroughputPolicyResource
from ._models_py3 import ThroughputSettingsGetPropertiesResource
from ._models_py3 import ThroughputSettingsGetResults
from ._models_py3 import ThroughputSettingsResource
from ._models_py3 import ThroughputSettingsUpdateParameters
from ._models_py3 import UniqueKey
from ._models_py3 import UniqueKeyPolicy
from ._models_py3 import Usage
from ._models_py3 import UsagesResult
from ._models_py3 import VirtualNetworkRule

from ._cosmos_db_management_client_enums import AnalyticalStorageSchemaType
from ._cosmos_db_management_client_enums import ApiType
from ._cosmos_db_management_client_enums import AuthenticationMethod
from ._cosmos_db_management_client_enums import AzureConnectionType
from ._cosmos_db_management_client_enums import BackupPolicyMigrationStatus
from ._cosmos_db_management_client_enums import BackupPolicyType
from ._cosmos_db_management_client_enums import BackupStorageRedundancy
from ._cosmos_db_management_client_enums import CompositePathSortOrder
from ._cosmos_db_management_client_enums import ConflictResolutionMode
from ._cosmos_db_management_client_enums import ConnectionState
from ._cosmos_db_management_client_enums import ConnectorOffer
from ._cosmos_db_management_client_enums import ContinuousTier
from ._cosmos_db_management_client_enums import CreateMode
from ._cosmos_db_management_client_enums import CreatedByType
from ._cosmos_db_management_client_enums import DataType
from ._cosmos_db_management_client_enums import DatabaseAccountKind
from ._cosmos_db_management_client_enums import DedicatedGatewayType
from ._cosmos_db_management_client_enums import DefaultConsistencyLevel
from ._cosmos_db_management_client_enums import IndexKind
from ._cosmos_db_management_client_enums import IndexingMode
from ._cosmos_db_management_client_enums import KeyKind
from ._cosmos_db_management_client_enums import Kind
from ._cosmos_db_management_client_enums import ManagedCassandraProvisioningState
from ._cosmos_db_management_client_enums import ManagedCassandraResourceIdentityType
from ._cosmos_db_management_client_enums import MinimalTlsVersion
from ._cosmos_db_management_client_enums import MongoRoleDefinitionType
from ._cosmos_db_management_client_enums import NetworkAclBypass
from ._cosmos_db_management_client_enums import NodeState
from ._cosmos_db_management_client_enums import NodeStatus
from ._cosmos_db_management_client_enums import NotebookWorkspaceName
from ._cosmos_db_management_client_enums import OperationType
from ._cosmos_db_management_client_enums import PartitionKind
from ._cosmos_db_management_client_enums import PrimaryAggregationType
from ._cosmos_db_management_client_enums import PublicNetworkAccess
from ._cosmos_db_management_client_enums import ResourceIdentityType
from ._cosmos_db_management_client_enums import RestoreMode
from ._cosmos_db_management_client_enums import RoleDefinitionType
from ._cosmos_db_management_client_enums import ServerVersion
from ._cosmos_db_management_client_enums import ServiceSize
from ._cosmos_db_management_client_enums import ServiceStatus
from ._cosmos_db_management_client_enums import ServiceType
from ._cosmos_db_management_client_enums import SpatialType
from ._cosmos_db_management_client_enums import Status
from ._cosmos_db_management_client_enums import TriggerOperation
from ._cosmos_db_management_client_enums import TriggerType
from ._cosmos_db_management_client_enums import Type
from ._cosmos_db_management_client_enums import UnitType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ARMProxyResource",
    "ARMResourceProperties",
    "AccountKeyMetadata",
    "AnalyticalStorageConfiguration",
    "ApiProperties",
    "AuthenticationMethodLdapProperties",
    "AutoUpgradePolicyResource",
    "AutoscaleSettings",
    "AutoscaleSettingsResource",
    "BackupInformation",
    "BackupPolicy",
    "BackupPolicyMigrationState",
    "Capability",
    "Capacity",
    "CassandraClusterDataCenterNodeItem",
    "CassandraClusterPublicStatus",
    "CassandraClusterPublicStatusDataCentersItem",
    "CassandraError",
    "CassandraKeyspaceCreateUpdateParameters",
    "CassandraKeyspaceGetPropertiesOptions",
    "CassandraKeyspaceGetPropertiesResource",
    "CassandraKeyspaceGetResults",
    "CassandraKeyspaceListResult",
    "CassandraKeyspaceResource",
    "CassandraPartitionKey",
    "CassandraSchema",
    "CassandraTableCreateUpdateParameters",
    "CassandraTableGetPropertiesOptions",
    "CassandraTableGetPropertiesResource",
    "CassandraTableGetResults",
    "CassandraTableListResult",
    "CassandraTableResource",
    "Certificate",
    "ClientEncryptionIncludedPath",
    "ClientEncryptionKeyCreateUpdateParameters",
    "ClientEncryptionKeyGetPropertiesResource",
    "ClientEncryptionKeyGetResults",
    "ClientEncryptionKeyResource",
    "ClientEncryptionKeysListResult",
    "ClientEncryptionPolicy",
    "ClusterKey",
    "ClusterResource",
    "ClusterResourceProperties",
    "Column",
    "CommandOutput",
    "CommandPostBody",
    "CompositePath",
    "ComputedProperty",
    "ConflictResolutionPolicy",
    "ConnectionError",
    "ConsistencyPolicy",
    "ContainerPartitionKey",
    "ContinuousBackupInformation",
    "ContinuousBackupRestoreLocation",
    "ContinuousModeBackupPolicy",
    "ContinuousModeProperties",
    "CorsPolicy",
    "CreateUpdateOptions",
    "DataCenterResource",
    "DataCenterResourceProperties",
    "DataTransferRegionalServiceResource",
    "DataTransferServiceResource",
    "DataTransferServiceResourceCreateUpdateProperties",
    "DataTransferServiceResourceProperties",
    "DatabaseAccountConnectionString",
    "DatabaseAccountCreateUpdateParameters",
    "DatabaseAccountGetResults",
    "DatabaseAccountKeysMetadata",
    "DatabaseAccountListConnectionStringsResult",
    "DatabaseAccountListKeysResult",
    "DatabaseAccountListReadOnlyKeysResult",
    "DatabaseAccountRegenerateKeyParameters",
    "DatabaseAccountUpdateParameters",
    "DatabaseAccountsListResult",
    "DatabaseRestoreResource",
    "ErrorResponse",
    "ExcludedPath",
    "ExtendedResourceProperties",
    "FailoverPolicies",
    "FailoverPolicy",
    "GraphAPIComputeRegionalServiceResource",
    "GraphAPIComputeServiceResource",
    "GraphAPIComputeServiceResourceCreateUpdateProperties",
    "GraphAPIComputeServiceResourceProperties",
    "GremlinDatabaseCreateUpdateParameters",
    "GremlinDatabaseGetPropertiesOptions",
    "GremlinDatabaseGetPropertiesResource",
    "GremlinDatabaseGetResults",
    "GremlinDatabaseListResult",
    "GremlinDatabaseResource",
    "GremlinDatabaseRestoreResource",
    "GremlinGraphCreateUpdateParameters",
    "GremlinGraphGetPropertiesOptions",
    "GremlinGraphGetPropertiesResource",
    "GremlinGraphGetResults",
    "GremlinGraphListResult",
    "GremlinGraphResource",
    "IncludedPath",
    "Indexes",
    "IndexingPolicy",
    "IpAddressOrRange",
    "KeyWrapMetadata",
    "ListClusters",
    "ListDataCenters",
    "Location",
    "LocationGetResult",
    "LocationListResult",
    "LocationProperties",
    "ManagedCassandraARMResourceProperties",
    "ManagedCassandraManagedServiceIdentity",
    "ManagedCassandraReaperStatus",
    "ManagedServiceIdentity",
    "ManagedServiceIdentityUserAssignedIdentity",
    "MaterializedViewsBuilderRegionalServiceResource",
    "MaterializedViewsBuilderServiceResource",
    "MaterializedViewsBuilderServiceResourceCreateUpdateProperties",
    "MaterializedViewsBuilderServiceResourceProperties",
    "Metric",
    "MetricAvailability",
    "MetricDefinition",
    "MetricDefinitionsListResult",
    "MetricListResult",
    "MetricName",
    "MetricValue",
    "MongoDBCollectionCreateUpdateParameters",
    "MongoDBCollectionGetPropertiesOptions",
    "MongoDBCollectionGetPropertiesResource",
    "MongoDBCollectionGetResults",
    "MongoDBCollectionListResult",
    "MongoDBCollectionResource",
    "MongoDBDatabaseCreateUpdateParameters",
    "MongoDBDatabaseGetPropertiesOptions",
    "MongoDBDatabaseGetPropertiesResource",
    "MongoDBDatabaseGetResults",
    "MongoDBDatabaseListResult",
    "MongoDBDatabaseResource",
    "MongoIndex",
    "MongoIndexKeys",
    "MongoIndexOptions",
    "MongoRoleDefinitionCreateUpdateParameters",
    "MongoRoleDefinitionGetResults",
    "MongoRoleDefinitionListResult",
    "MongoUserDefinitionCreateUpdateParameters",
    "MongoUserDefinitionGetResults",
    "MongoUserDefinitionListResult",
    "NotebookWorkspace",
    "NotebookWorkspaceConnectionInfoResult",
    "NotebookWorkspaceCreateUpdateParameters",
    "NotebookWorkspaceListResult",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OptionsResource",
    "PartitionMetric",
    "PartitionMetricListResult",
    "PartitionUsage",
    "PartitionUsagesResult",
    "PercentileMetric",
    "PercentileMetricListResult",
    "PercentileMetricValue",
    "PeriodicModeBackupPolicy",
    "PeriodicModeProperties",
    "Permission",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateEndpointProperty",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionStateProperty",
    "Privilege",
    "PrivilegeResource",
    "ProxyResource",
    "RegionForOnlineOffline",
    "RegionalServiceResource",
    "Resource",
    "ResourceRestoreParameters",
    "RestorableDatabaseAccountGetResult",
    "RestorableDatabaseAccountsListResult",
    "RestorableGremlinDatabaseGetResult",
    "RestorableGremlinDatabasePropertiesResource",
    "RestorableGremlinDatabasesListResult",
    "RestorableGremlinGraphGetResult",
    "RestorableGremlinGraphPropertiesResource",
    "RestorableGremlinGraphsListResult",
    "RestorableGremlinResourcesGetResult",
    "RestorableGremlinResourcesListResult",
    "RestorableLocationResource",
    "RestorableMongodbCollectionGetResult",
    "RestorableMongodbCollectionPropertiesResource",
    "RestorableMongodbCollectionsListResult",
    "RestorableMongodbDatabaseGetResult",
    "RestorableMongodbDatabasePropertiesResource",
    "RestorableMongodbDatabasesListResult",
    "RestorableMongodbResourcesGetResult",
    "RestorableMongodbResourcesListResult",
    "RestorableSqlContainerGetResult",
    "RestorableSqlContainerPropertiesResource",
    "RestorableSqlContainerPropertiesResourceContainer",
    "RestorableSqlContainersListResult",
    "RestorableSqlDatabaseGetResult",
    "RestorableSqlDatabasePropertiesResource",
    "RestorableSqlDatabasePropertiesResourceDatabase",
    "RestorableSqlDatabasesListResult",
    "RestorableSqlResourcesGetResult",
    "RestorableSqlResourcesListResult",
    "RestorableTableGetResult",
    "RestorableTablePropertiesResource",
    "RestorableTableResourcesGetResult",
    "RestorableTableResourcesListResult",
    "RestorableTablesListResult",
    "RestoreParameters",
    "RestoreParametersBase",
    "Role",
    "SeedNode",
    "ServiceResource",
    "ServiceResourceCreateUpdateParameters",
    "ServiceResourceCreateUpdateProperties",
    "ServiceResourceListResult",
    "ServiceResourceProperties",
    "SpatialSpec",
    "SqlContainerCreateUpdateParameters",
    "SqlContainerGetPropertiesOptions",
    "SqlContainerGetPropertiesResource",
    "SqlContainerGetResults",
    "SqlContainerListResult",
    "SqlContainerResource",
    "SqlDatabaseCreateUpdateParameters",
    "SqlDatabaseGetPropertiesOptions",
    "SqlDatabaseGetPropertiesResource",
    "SqlDatabaseGetResults",
    "SqlDatabaseListResult",
    "SqlDatabaseResource",
    "SqlDedicatedGatewayRegionalServiceResource",
    "SqlDedicatedGatewayServiceResource",
    "SqlDedicatedGatewayServiceResourceCreateUpdateProperties",
    "SqlDedicatedGatewayServiceResourceProperties",
    "SqlRoleAssignmentCreateUpdateParameters",
    "SqlRoleAssignmentGetResults",
    "SqlRoleAssignmentListResult",
    "SqlRoleDefinitionCreateUpdateParameters",
    "SqlRoleDefinitionGetResults",
    "SqlRoleDefinitionListResult",
    "SqlStoredProcedureCreateUpdateParameters",
    "SqlStoredProcedureGetPropertiesResource",
    "SqlStoredProcedureGetResults",
    "SqlStoredProcedureListResult",
    "SqlStoredProcedureResource",
    "SqlTriggerCreateUpdateParameters",
    "SqlTriggerGetPropertiesResource",
    "SqlTriggerGetResults",
    "SqlTriggerListResult",
    "SqlTriggerResource",
    "SqlUserDefinedFunctionCreateUpdateParameters",
    "SqlUserDefinedFunctionGetPropertiesResource",
    "SqlUserDefinedFunctionGetResults",
    "SqlUserDefinedFunctionListResult",
    "SqlUserDefinedFunctionResource",
    "SystemData",
    "TableCreateUpdateParameters",
    "TableGetPropertiesOptions",
    "TableGetPropertiesResource",
    "TableGetResults",
    "TableListResult",
    "TableResource",
    "ThroughputPolicyResource",
    "ThroughputSettingsGetPropertiesResource",
    "ThroughputSettingsGetResults",
    "ThroughputSettingsResource",
    "ThroughputSettingsUpdateParameters",
    "UniqueKey",
    "UniqueKeyPolicy",
    "Usage",
    "UsagesResult",
    "VirtualNetworkRule",
    "AnalyticalStorageSchemaType",
    "ApiType",
    "AuthenticationMethod",
    "AzureConnectionType",
    "BackupPolicyMigrationStatus",
    "BackupPolicyType",
    "BackupStorageRedundancy",
    "CompositePathSortOrder",
    "ConflictResolutionMode",
    "ConnectionState",
    "ConnectorOffer",
    "ContinuousTier",
    "CreateMode",
    "CreatedByType",
    "DataType",
    "DatabaseAccountKind",
    "DedicatedGatewayType",
    "DefaultConsistencyLevel",
    "IndexKind",
    "IndexingMode",
    "KeyKind",
    "Kind",
    "ManagedCassandraProvisioningState",
    "ManagedCassandraResourceIdentityType",
    "MinimalTlsVersion",
    "MongoRoleDefinitionType",
    "NetworkAclBypass",
    "NodeState",
    "NodeStatus",
    "NotebookWorkspaceName",
    "OperationType",
    "PartitionKind",
    "PrimaryAggregationType",
    "PublicNetworkAccess",
    "ResourceIdentityType",
    "RestoreMode",
    "RoleDefinitionType",
    "ServerVersion",
    "ServiceSize",
    "ServiceStatus",
    "ServiceType",
    "SpatialType",
    "Status",
    "TriggerOperation",
    "TriggerType",
    "Type",
    "UnitType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
