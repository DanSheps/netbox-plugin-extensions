from netbox.api.serializers import ValidatedModelSerializer, WritableNestedSerializer, OrganizationalModelSerializer, \
    PrimaryModelSerializer, NestedGroupModelSerializer, BulkOperationSerializer


class PluginValidatedModelSerializer(ValidatedModelSerializer):
    pass


#
# Nested serializers
#

class PluginWritableNestedSerializer(WritableNestedSerializer):
    pass


#
# Base model serializers
#

class PluginOrganizationalModelSerializer(OrganizationalModelSerializer):
    pass


class PluginPrimaryModelSerializer(PrimaryModelSerializer):
    pass


class PluginNestedGroupModelSerializer(NestedGroupModelSerializer):
    pass


class PluginBulkOperationSerializer(BulkOperationSerializer):
    pass
