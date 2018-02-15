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


class WorkItemCreateConfiguration(Model):
    """Work item configuration creation payload.

    :param connector_id: Unique connector id
    :type connector_id: str
    :param connector_data_configuration: Serialized JSON object for detaile d
     properties
    :type connector_data_configuration: str
    :param validate_only: Boolean indicating validate only
    :type validate_only: bool
    :param work_item_properties: Custom work item properties
    :type work_item_properties: str
    """

    _attribute_map = {
        'connector_id': {'key': 'ConnectorId', 'type': 'str'},
        'connector_data_configuration': {'key': 'ConnectorDataConfiguration', 'type': 'str'},
        'validate_only': {'key': 'ValidateOnly', 'type': 'bool'},
        'work_item_properties': {'key': 'WorkItemProperties', 'type': 'str'},
    }

    def __init__(self, connector_id=None, connector_data_configuration=None, validate_only=None, work_item_properties=None):
        super(WorkItemCreateConfiguration, self).__init__()
        self.connector_id = connector_id
        self.connector_data_configuration = connector_data_configuration
        self.validate_only = validate_only
        self.work_item_properties = work_item_properties
