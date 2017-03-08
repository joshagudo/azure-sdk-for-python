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


class ImportExtensionRequestParameters(Model):
    """Import database parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The name of the extension.
    :type name: str
    :param type: The type of the extension.
    :type type: str
    :param storage_key_type: The type of the storage key to use. Valid values
     are StorageAccessKey and SharedAccessKey. Possible values include:
     'StorageAccessKey', 'SharedAccessKey'
    :type storage_key_type: str or :class:`StorageKeyType
     <azure.mgmt.sql.models.StorageKeyType>`
    :param storage_key: The storage key to use.
    :type storage_key: str
    :param storage_uri: The storage uri to use.
    :type storage_uri: str
    :param administrator_login: The name of the SQL administrator.
    :type administrator_login: str
    :param administrator_login_password: The password of the SQL
     administrator.
    :type administrator_login_password: str
    :param authentication_type: The authentication type - if not specified,
     will default to SQL. Possible values include: 'SQL', 'ADPassword'
    :type authentication_type: str or :class:`AuthenticationType
     <azure.mgmt.sql.models.AuthenticationType>`
    :ivar operation_mode: The type of Import/Export operation being performed.
     This is always Import. Default value: "Import" .
    :vartype operation_mode: str
    """

    _validation = {
        'storage_key_type': {'required': True},
        'storage_key': {'required': True},
        'storage_uri': {'required': True},
        'administrator_login': {'required': True},
        'administrator_login_password': {'required': True},
        'operation_mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'storage_key_type': {'key': 'properties.storageKeyType', 'type': 'StorageKeyType'},
        'storage_key': {'key': 'properties.storageKey', 'type': 'str'},
        'storage_uri': {'key': 'properties.storageUri', 'type': 'str'},
        'administrator_login': {'key': 'properties.administratorLogin', 'type': 'str'},
        'administrator_login_password': {'key': 'properties.administratorLoginPassword', 'type': 'str'},
        'authentication_type': {'key': 'properties.authenticationType', 'type': 'AuthenticationType'},
        'operation_mode': {'key': 'properties.operationMode', 'type': 'str'},
    }

    operation_mode = "Import"

    def __init__(self, storage_key_type, storage_key, storage_uri, administrator_login, administrator_login_password, name=None, type=None, authentication_type=None):
        self.name = name
        self.type = type
        self.storage_key_type = storage_key_type
        self.storage_key = storage_key
        self.storage_uri = storage_uri
        self.administrator_login = administrator_login
        self.administrator_login_password = administrator_login_password
        self.authentication_type = authentication_type
