from netbox.api import ChoiceField, ContentTypeField, SerializedPKRelatedField


class PluginChoiceField(ChoiceField):
    pass


class PluginContentTypeField(ContentTypeField):
    pass


class PluginSerializedPKRelatedField(SerializedPKRelatedField):
    pass
