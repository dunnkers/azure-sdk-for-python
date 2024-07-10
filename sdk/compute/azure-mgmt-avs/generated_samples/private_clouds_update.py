# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.avs import AVSClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-avs
# USAGE
    python private_clouds_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AVSClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.private_clouds.begin_update(
        resource_group_name="group1",
        private_cloud_name="cloud1",
        private_cloud_update={
            "identity": {"type": "None"},
            "properties": {
                "encryption": {
                    "keyVaultProperties": {
                        "keyName": "keyname1",
                        "keyVaultUrl": "https://keyvault1-kmip-kvault.vault.azure.net/",
                        "keyVersion": "ver1.0",
                    },
                    "status": "Enabled",
                },
                "managementCluster": {"clusterSize": 4},
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/vmware/resource-manager/Microsoft.AVS/stable/2023-09-01/examples/PrivateClouds_Update.json
if __name__ == "__main__":
    main()
