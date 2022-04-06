from netbox_plugin_extensions.tables.objectchange import PluginObjectChangeTable

from extras.views import ObjectChangeListView
from netbox_plugin_extensions.views.generic import PluginObjectListView


#
# Change logging
#
class PluginObjectChangeListView(ObjectChangeListView):
    pass
