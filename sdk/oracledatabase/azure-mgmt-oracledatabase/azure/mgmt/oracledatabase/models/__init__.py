# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ActivationLinks
from ._models_py3 import AddRemoveDbNode
from ._models_py3 import AllConnectionStringType
from ._models_py3 import ApexDetailsType
from ._models_py3 import AutonomousDatabase
from ._models_py3 import AutonomousDatabaseBackup
from ._models_py3 import AutonomousDatabaseBackupListResult
from ._models_py3 import AutonomousDatabaseBackupProperties
from ._models_py3 import AutonomousDatabaseBackupUpdate
from ._models_py3 import AutonomousDatabaseBackupUpdateProperties
from ._models_py3 import AutonomousDatabaseBaseProperties
from ._models_py3 import AutonomousDatabaseCharacterSet
from ._models_py3 import AutonomousDatabaseCharacterSetListResult
from ._models_py3 import AutonomousDatabaseCharacterSetProperties
from ._models_py3 import AutonomousDatabaseCloneProperties
from ._models_py3 import AutonomousDatabaseListResult
from ._models_py3 import AutonomousDatabaseNationalCharacterSet
from ._models_py3 import AutonomousDatabaseNationalCharacterSetListResult
from ._models_py3 import AutonomousDatabaseNationalCharacterSetProperties
from ._models_py3 import AutonomousDatabaseProperties
from ._models_py3 import AutonomousDatabaseStandbySummary
from ._models_py3 import AutonomousDatabaseUpdate
from ._models_py3 import AutonomousDatabaseUpdateProperties
from ._models_py3 import AutonomousDatabaseWalletFile
from ._models_py3 import AutonomousDbVersion
from ._models_py3 import AutonomousDbVersionListResult
from ._models_py3 import AutonomousDbVersionProperties
from ._models_py3 import CloudAccountDetails
from ._models_py3 import CloudExadataInfrastructure
from ._models_py3 import CloudExadataInfrastructureListResult
from ._models_py3 import CloudExadataInfrastructureProperties
from ._models_py3 import CloudExadataInfrastructureUpdate
from ._models_py3 import CloudExadataInfrastructureUpdateProperties
from ._models_py3 import CloudVmCluster
from ._models_py3 import CloudVmClusterListResult
from ._models_py3 import CloudVmClusterProperties
from ._models_py3 import CloudVmClusterUpdate
from ._models_py3 import CloudVmClusterUpdateProperties
from ._models_py3 import ConnectionStringType
from ._models_py3 import ConnectionUrlType
from ._models_py3 import CustomerContact
from ._models_py3 import DataCollectionOptions
from ._models_py3 import DayOfWeek
from ._models_py3 import DayOfWeekUpdate
from ._models_py3 import DbIormConfig
from ._models_py3 import DbNode
from ._models_py3 import DbNodeAction
from ._models_py3 import DbNodeListResult
from ._models_py3 import DbNodeProperties
from ._models_py3 import DbServer
from ._models_py3 import DbServerListResult
from ._models_py3 import DbServerPatchingDetails
from ._models_py3 import DbServerProperties
from ._models_py3 import DbSystemShape
from ._models_py3 import DbSystemShapeListResult
from ._models_py3 import DbSystemShapeProperties
from ._models_py3 import DnsPrivateView
from ._models_py3 import DnsPrivateViewListResult
from ._models_py3 import DnsPrivateViewProperties
from ._models_py3 import DnsPrivateZone
from ._models_py3 import DnsPrivateZoneListResult
from ._models_py3 import DnsPrivateZoneProperties
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import EstimatedPatchingTime
from ._models_py3 import ExadataIormConfig
from ._models_py3 import GenerateAutonomousDatabaseWalletDetails
from ._models_py3 import GiVersion
from ._models_py3 import GiVersionListResult
from ._models_py3 import GiVersionProperties
from ._models_py3 import LongTermBackUpScheduleDetails
from ._models_py3 import MaintenanceWindow
from ._models_py3 import Month
from ._models_py3 import NsgCidr
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OracleSubscription
from ._models_py3 import OracleSubscriptionListResult
from ._models_py3 import OracleSubscriptionProperties
from ._models_py3 import OracleSubscriptionUpdate
from ._models_py3 import OracleSubscriptionUpdateProperties
from ._models_py3 import PeerDbDetails
from ._models_py3 import Plan
from ._models_py3 import PlanUpdate
from ._models_py3 import PortRange
from ._models_py3 import PrivateIpAddressProperties
from ._models_py3 import PrivateIpAddressesFilter
from ._models_py3 import ProfileType
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import RestoreAutonomousDatabaseDetails
from ._models_py3 import SaasSubscriptionDetails
from ._models_py3 import ScheduledOperationsType
from ._models_py3 import ScheduledOperationsTypeUpdate
from ._models_py3 import SystemData
from ._models_py3 import SystemVersion
from ._models_py3 import SystemVersionListResult
from ._models_py3 import SystemVersionProperties
from ._models_py3 import SystemVersionsFilter
from ._models_py3 import TrackedResource
from ._models_py3 import ValidationError
from ._models_py3 import ValidationResult
from ._models_py3 import VirtualNetworkAddress
from ._models_py3 import VirtualNetworkAddressListResult
from ._models_py3 import VirtualNetworkAddressProperties

from ._oracle_database_mgmt_client_enums import ActionType
from ._oracle_database_mgmt_client_enums import AutonomousDatabaseBackupLifecycleState
from ._oracle_database_mgmt_client_enums import AutonomousDatabaseBackupType
from ._oracle_database_mgmt_client_enums import AutonomousDatabaseLifecycleState
from ._oracle_database_mgmt_client_enums import AutonomousMaintenanceScheduleType
from ._oracle_database_mgmt_client_enums import AzureResourceProvisioningState
from ._oracle_database_mgmt_client_enums import CloneType
from ._oracle_database_mgmt_client_enums import CloudAccountProvisioningState
from ._oracle_database_mgmt_client_enums import CloudExadataInfrastructureLifecycleState
from ._oracle_database_mgmt_client_enums import CloudVmClusterLifecycleState
from ._oracle_database_mgmt_client_enums import ComputeModel
from ._oracle_database_mgmt_client_enums import ConsumerGroup
from ._oracle_database_mgmt_client_enums import CreatedByType
from ._oracle_database_mgmt_client_enums import DataBaseType
from ._oracle_database_mgmt_client_enums import DataSafeStatusType
from ._oracle_database_mgmt_client_enums import DatabaseEditionType
from ._oracle_database_mgmt_client_enums import DayOfWeekName
from ._oracle_database_mgmt_client_enums import DbNodeActionEnum
from ._oracle_database_mgmt_client_enums import DbNodeMaintenanceType
from ._oracle_database_mgmt_client_enums import DbNodeProvisioningState
from ._oracle_database_mgmt_client_enums import DbServerPatchingStatus
from ._oracle_database_mgmt_client_enums import DbServerProvisioningState
from ._oracle_database_mgmt_client_enums import DisasterRecoveryType
from ._oracle_database_mgmt_client_enums import DiskRedundancy
from ._oracle_database_mgmt_client_enums import DnsPrivateViewsLifecycleState
from ._oracle_database_mgmt_client_enums import DnsPrivateZonesLifecycleState
from ._oracle_database_mgmt_client_enums import GenerateType
from ._oracle_database_mgmt_client_enums import HostFormatType
from ._oracle_database_mgmt_client_enums import Intent
from ._oracle_database_mgmt_client_enums import IormLifecycleState
from ._oracle_database_mgmt_client_enums import LicenseModel
from ._oracle_database_mgmt_client_enums import MonthName
from ._oracle_database_mgmt_client_enums import Objective
from ._oracle_database_mgmt_client_enums import OpenModeType
from ._oracle_database_mgmt_client_enums import OperationsInsightsStatusType
from ._oracle_database_mgmt_client_enums import OracleSubscriptionProvisioningState
from ._oracle_database_mgmt_client_enums import Origin
from ._oracle_database_mgmt_client_enums import PatchingMode
from ._oracle_database_mgmt_client_enums import PermissionLevelType
from ._oracle_database_mgmt_client_enums import Preference
from ._oracle_database_mgmt_client_enums import ProtocolType
from ._oracle_database_mgmt_client_enums import RefreshableModelType
from ._oracle_database_mgmt_client_enums import RefreshableStatusType
from ._oracle_database_mgmt_client_enums import RepeatCadenceType
from ._oracle_database_mgmt_client_enums import ResourceProvisioningState
from ._oracle_database_mgmt_client_enums import RoleType
from ._oracle_database_mgmt_client_enums import SessionModeType
from ._oracle_database_mgmt_client_enums import SourceType
from ._oracle_database_mgmt_client_enums import SyntaxFormatType
from ._oracle_database_mgmt_client_enums import TlsAuthenticationType
from ._oracle_database_mgmt_client_enums import UpdateAction
from ._oracle_database_mgmt_client_enums import ValidationStatus
from ._oracle_database_mgmt_client_enums import VirtualNetworkAddressLifecycleState
from ._oracle_database_mgmt_client_enums import WorkloadType
from ._oracle_database_mgmt_client_enums import ZoneType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ActivationLinks",
    "AddRemoveDbNode",
    "AllConnectionStringType",
    "ApexDetailsType",
    "AutonomousDatabase",
    "AutonomousDatabaseBackup",
    "AutonomousDatabaseBackupListResult",
    "AutonomousDatabaseBackupProperties",
    "AutonomousDatabaseBackupUpdate",
    "AutonomousDatabaseBackupUpdateProperties",
    "AutonomousDatabaseBaseProperties",
    "AutonomousDatabaseCharacterSet",
    "AutonomousDatabaseCharacterSetListResult",
    "AutonomousDatabaseCharacterSetProperties",
    "AutonomousDatabaseCloneProperties",
    "AutonomousDatabaseListResult",
    "AutonomousDatabaseNationalCharacterSet",
    "AutonomousDatabaseNationalCharacterSetListResult",
    "AutonomousDatabaseNationalCharacterSetProperties",
    "AutonomousDatabaseProperties",
    "AutonomousDatabaseStandbySummary",
    "AutonomousDatabaseUpdate",
    "AutonomousDatabaseUpdateProperties",
    "AutonomousDatabaseWalletFile",
    "AutonomousDbVersion",
    "AutonomousDbVersionListResult",
    "AutonomousDbVersionProperties",
    "CloudAccountDetails",
    "CloudExadataInfrastructure",
    "CloudExadataInfrastructureListResult",
    "CloudExadataInfrastructureProperties",
    "CloudExadataInfrastructureUpdate",
    "CloudExadataInfrastructureUpdateProperties",
    "CloudVmCluster",
    "CloudVmClusterListResult",
    "CloudVmClusterProperties",
    "CloudVmClusterUpdate",
    "CloudVmClusterUpdateProperties",
    "ConnectionStringType",
    "ConnectionUrlType",
    "CustomerContact",
    "DataCollectionOptions",
    "DayOfWeek",
    "DayOfWeekUpdate",
    "DbIormConfig",
    "DbNode",
    "DbNodeAction",
    "DbNodeListResult",
    "DbNodeProperties",
    "DbServer",
    "DbServerListResult",
    "DbServerPatchingDetails",
    "DbServerProperties",
    "DbSystemShape",
    "DbSystemShapeListResult",
    "DbSystemShapeProperties",
    "DnsPrivateView",
    "DnsPrivateViewListResult",
    "DnsPrivateViewProperties",
    "DnsPrivateZone",
    "DnsPrivateZoneListResult",
    "DnsPrivateZoneProperties",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "EstimatedPatchingTime",
    "ExadataIormConfig",
    "GenerateAutonomousDatabaseWalletDetails",
    "GiVersion",
    "GiVersionListResult",
    "GiVersionProperties",
    "LongTermBackUpScheduleDetails",
    "MaintenanceWindow",
    "Month",
    "NsgCidr",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OracleSubscription",
    "OracleSubscriptionListResult",
    "OracleSubscriptionProperties",
    "OracleSubscriptionUpdate",
    "OracleSubscriptionUpdateProperties",
    "PeerDbDetails",
    "Plan",
    "PlanUpdate",
    "PortRange",
    "PrivateIpAddressProperties",
    "PrivateIpAddressesFilter",
    "ProfileType",
    "ProxyResource",
    "Resource",
    "RestoreAutonomousDatabaseDetails",
    "SaasSubscriptionDetails",
    "ScheduledOperationsType",
    "ScheduledOperationsTypeUpdate",
    "SystemData",
    "SystemVersion",
    "SystemVersionListResult",
    "SystemVersionProperties",
    "SystemVersionsFilter",
    "TrackedResource",
    "ValidationError",
    "ValidationResult",
    "VirtualNetworkAddress",
    "VirtualNetworkAddressListResult",
    "VirtualNetworkAddressProperties",
    "ActionType",
    "AutonomousDatabaseBackupLifecycleState",
    "AutonomousDatabaseBackupType",
    "AutonomousDatabaseLifecycleState",
    "AutonomousMaintenanceScheduleType",
    "AzureResourceProvisioningState",
    "CloneType",
    "CloudAccountProvisioningState",
    "CloudExadataInfrastructureLifecycleState",
    "CloudVmClusterLifecycleState",
    "ComputeModel",
    "ConsumerGroup",
    "CreatedByType",
    "DataBaseType",
    "DataSafeStatusType",
    "DatabaseEditionType",
    "DayOfWeekName",
    "DbNodeActionEnum",
    "DbNodeMaintenanceType",
    "DbNodeProvisioningState",
    "DbServerPatchingStatus",
    "DbServerProvisioningState",
    "DisasterRecoveryType",
    "DiskRedundancy",
    "DnsPrivateViewsLifecycleState",
    "DnsPrivateZonesLifecycleState",
    "GenerateType",
    "HostFormatType",
    "Intent",
    "IormLifecycleState",
    "LicenseModel",
    "MonthName",
    "Objective",
    "OpenModeType",
    "OperationsInsightsStatusType",
    "OracleSubscriptionProvisioningState",
    "Origin",
    "PatchingMode",
    "PermissionLevelType",
    "Preference",
    "ProtocolType",
    "RefreshableModelType",
    "RefreshableStatusType",
    "RepeatCadenceType",
    "ResourceProvisioningState",
    "RoleType",
    "SessionModeType",
    "SourceType",
    "SyntaxFormatType",
    "TlsAuthenticationType",
    "UpdateAction",
    "ValidationStatus",
    "VirtualNetworkAddressLifecycleState",
    "WorkloadType",
    "ZoneType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
