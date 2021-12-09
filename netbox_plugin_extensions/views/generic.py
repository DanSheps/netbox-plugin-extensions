from netbox.views import generic

__all__ = (
    'PluginObjectListView',
    'PluginObjectView',
    'PluginObjectEditView',
    'PluginObjectDeleteView',
    'PluginObjectImportView',
    'PluginObjectBulkCreateView',
    'PluginObjectBulkEditView',
    'PluginObjectBulkDeleteView',
    'PluginObjectBulkRenameView',
    'PluginObjectBulkImportView'
)


class PluginObjectListView(generic.ObjectListView):
    template_name = 'netbox_plugin_extensions/generic/object_list.html'


class PluginObjectView(generic.ObjectView):
    pass


class PluginObjectEditView(generic.ObjectEditView):
    template_name = 'netbox_plugin_extensions/generic/object_edit.html'


class PluginObjectDeleteView(generic.ObjectDeleteView):
    template_name = 'netbox_plugin_extensions/generic/object_delete.html'


class PluginObjectImportView(generic.ObjectImportView):
    template_name = 'netbox_plugin_extensions/generic/object_import.html'


class PluginObjectBulkImportView(generic.BulkImportView):
    template_name = 'netbox_plugin_extensions/generic/object_bulk_import.html'


class PluginObjectBulkCreateView(generic.BulkCreateView):
    pass


class PluginObjectBulkEditView(generic.BulkEditView):
    template_name = 'netbox_plugin_extensions/generic/object_bulk_edit.html'


class PluginObjectBulkDeleteView(generic.BulkDeleteView):
    template_name = 'netbox_plugin_extensions/generic/object_bulk_delete.html'


class PluginObjectBulkRenameView(generic.BulkRenameView):
    template_name = 'netbox_plugin_extensions/generic/object_bulk_rename.html'
