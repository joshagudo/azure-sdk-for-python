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

from enum import Enum


class StorageKeyType(Enum):

    storage_access_key = "StorageAccessKey"
    shared_access_key = "SharedAccessKey"


class AuthenticationType(Enum):

    sql = "SQL"
    ad_password = "ADPassword"


class ReplicationRole(Enum):

    primary = "Primary"
    secondary = "Secondary"
    non_readable_secondary = "NonReadableSecondary"
    source = "Source"
    copy = "Copy"


class ReplicationState(Enum):

    pending = "PENDING"
    seeding = "SEEDING"
    catch_up = "CATCH_UP"
    suspended = "SUSPENDED"


class ElasticPoolEditions(Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class CreateMode(Enum):

    copy = "Copy"
    default = "Default"
    non_readable_secondary = "NonReadableSecondary"
    online_secondary = "OnlineSecondary"
    point_in_time_restore = "PointInTimeRestore"
    recovery = "Recovery"
    restore = "Restore"
    restore_long_term_retention_backup = "RestoreLongTermRetentionBackup"


class DatabaseEditions(Enum):

    web = "Web"
    business = "Business"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    free = "Free"
    stretch = "Stretch"
    data_warehouse = "DataWarehouse"
    system = "System"


class ServiceObjectiveName(Enum):

    basic = "Basic"
    s0 = "S0"
    s1 = "S1"
    s2 = "S2"
    s3 = "S3"
    p1 = "P1"
    p2 = "P2"
    p3 = "P3"
    p4 = "P4"
    p6 = "P6"
    p11 = "P11"
    p15 = "P15"
    system = "System"
    elastic_pool = "ElasticPool"


class TableType(Enum):

    base_table = "BaseTable"
    view = "View"


class RecommendedIndexActions(Enum):

    create = "Create"
    drop = "Drop"
    rebuild = "Rebuild"


class RecommendedIndexStates(Enum):

    active = "Active"
    pending = "Pending"
    executing = "Executing"
    verifying = "Verifying"
    pending_revert = "Pending Revert"
    reverting = "Reverting"
    reverted = "Reverted"
    ignored = "Ignored"
    expired = "Expired"
    blocked = "Blocked"
    success = "Success"


class RecommendedIndexTypes(Enum):

    clustered = "CLUSTERED"
    nonclustered = "NONCLUSTERED"
    columnstore = "COLUMNSTORE"
    clusteredcolumnstore = "CLUSTERED COLUMNSTORE"


class TransparentDataEncryptionStates(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ReadScale(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class SampleName(Enum):

    adventure_works_lt = "AdventureWorksLT"


class ElasticPoolState(Enum):

    creating = "Creating"
    ready = "Ready"
    disabled = "Disabled"


class ServerVersion(Enum):

    two_full_stop_zero = "2.0"
    one_two_full_stop_zero = "12.0"


class ServerState(Enum):

    ready = "Ready"
    disabled = "Disabled"


class TargetElasticPoolEditions(Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class RestorePointTypes(Enum):

    discrete = "DISCRETE"
    continuous = "CONTINUOUS"


class TransparentDataEncryptionActivityStates(Enum):

    encrypting = "Encrypting"
    decrypting = "Decrypting"
