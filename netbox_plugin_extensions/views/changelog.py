from netbox_plugin_extensions.tables.objectchange import PluginObjectChangeTable

from extras.models import ObjectChange
from extras.views import ObjectChangeListView
from netbox_plugin_extensions.views.generic import PluginObjectListView


#
# Change logging
#
class PluginObjectChangeListView(PluginObjectListView, ObjectChangeListView):
    table = PluginObjectChangeTable
    template_name = 'extras/objectchange_list.html'
    action_buttons = ('export',)
