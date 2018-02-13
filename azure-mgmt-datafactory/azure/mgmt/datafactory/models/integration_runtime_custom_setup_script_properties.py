# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IntegrationRuntimeCustomSetupScriptProperties(Model):
    """Custom setup script properties for a managed dedicated integration runtime.

    :param blob_container_uri: The URI of the Azure blob container that
     contains the custom setup script.
    :type blob_container_uri: str
    :param sas_token: The SAS token of the Azure blob container.
    :type sas_token: ~azure.mgmt.datafactory.models.SecureString
    """

    _attribute_map = {
        'blob_container_uri': {'key': 'blobContainerUri', 'type': 'str'},
        'sas_token': {'key': 'sasToken', 'type': 'SecureString'},
    }

    def __init__(self, blob_container_uri=None, sas_token=None):
        super(IntegrationRuntimeCustomSetupScriptProperties, self).__init__()
        self.blob_container_uri = blob_container_uri
        self.sas_token = sas_token
