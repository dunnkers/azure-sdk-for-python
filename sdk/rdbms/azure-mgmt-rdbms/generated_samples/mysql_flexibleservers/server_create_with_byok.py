# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.rdbms.mysql_flexibleservers import MySQLManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-rdbms
# USAGE
    python server_create_with_byok.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MySQLManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="ffffffff-ffff-ffff-ffff-ffffffffffff",
    )

    response = client.servers.begin_create(
        resource_group_name="testrg",
        server_name="mysqltestserver",
        parameters={
            "identity": {
                "type": "UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/testrg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/test-identity": {}
                },
            },
            "location": "southeastasia",
            "properties": {
                "administratorLogin": "cloudsa",
                "administratorLoginPassword": "your_password",
                "availabilityZone": "1",
                "backup": {"backupRetentionDays": 7, "geoRedundantBackup": "Disabled"},
                "createMode": "Default",
                "dataEncryption": {
                    "geoBackupKeyURI": "https://test-geo.vault.azure.net/keys/key/c8a92236622244c0a4fdb892666f671a",
                    "geoBackupUserAssignedIdentityId": "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/testrg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/test-geo-identity",
                    "primaryKeyURI": "https://test.vault.azure.net/keys/key/c8a92236622244c0a4fdb892666f671a",
                    "primaryUserAssignedIdentityId": "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/testrg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/test-identity",
                    "type": "AzureKeyVault",
                },
                "highAvailability": {"mode": "ZoneRedundant", "standbyAvailabilityZone": "3"},
                "storage": {"autoGrow": "Disabled", "iops": 600, "storageSizeGB": 100},
                "version": "5.7",
            },
            "sku": {"name": "Standard_D2ds_v4", "tier": "GeneralPurpose"},
            "tags": {"num": "1"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/mysql/resource-manager/Microsoft.DBforMySQL/FlexibleServers/preview/2023-06-01-preview/examples/ServerCreateWithBYOK.json
if __name__ == "__main__":
    main()
