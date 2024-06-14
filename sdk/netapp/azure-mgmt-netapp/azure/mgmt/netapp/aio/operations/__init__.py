# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._net_app_resource_operations import NetAppResourceOperations
from ._net_app_resource_quota_limits_operations import NetAppResourceQuotaLimitsOperations
from ._net_app_resource_region_infos_operations import NetAppResourceRegionInfosOperations
from ._accounts_operations import AccountsOperations
from ._pools_operations import PoolsOperations
from ._volumes_operations import VolumesOperations
from ._snapshots_operations import SnapshotsOperations
from ._snapshot_policies_operations import SnapshotPoliciesOperations
from ._backup_policies_operations import BackupPoliciesOperations
from ._volume_quota_rules_operations import VolumeQuotaRulesOperations
from ._volume_groups_operations import VolumeGroupsOperations
from ._subvolumes_operations import SubvolumesOperations
from ._backups_operations import BackupsOperations
from ._backup_vaults_operations import BackupVaultsOperations
from ._backups_under_backup_vault_operations import BackupsUnderBackupVaultOperations
from ._backups_under_volume_operations import BackupsUnderVolumeOperations
from ._backups_under_account_operations import BackupsUnderAccountOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "NetAppResourceOperations",
    "NetAppResourceQuotaLimitsOperations",
    "NetAppResourceRegionInfosOperations",
    "AccountsOperations",
    "PoolsOperations",
    "VolumesOperations",
    "SnapshotsOperations",
    "SnapshotPoliciesOperations",
    "BackupPoliciesOperations",
    "VolumeQuotaRulesOperations",
    "VolumeGroupsOperations",
    "SubvolumesOperations",
    "BackupsOperations",
    "BackupVaultsOperations",
    "BackupsUnderBackupVaultOperations",
    "BackupsUnderVolumeOperations",
    "BackupsUnderAccountOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
