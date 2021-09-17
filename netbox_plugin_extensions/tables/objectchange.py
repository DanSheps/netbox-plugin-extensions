from extras.models import ObjectChange
from netbox_plugin_extensions.tables import PluginButtonsColumn
from extras.tables import ObjectChangeTable


class PluginObjectChangeTable(ObjectChangeTable):

    actions = PluginButtonsColumn(ObjectChange)
