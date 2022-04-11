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
    pass


class PluginObjectView(generic.ObjectView):
    pass


class PluginObjectEditView(generic.ObjectEditView):
    pass


class PluginObjectDeleteView(generic.ObjectDeleteView):
    pass


class PluginObjectImportView(generic.ObjectImportView):
    pass


class PluginObjectBulkImportView(generic.BulkImportView):
    pass


class PluginObjectBulkCreateView(generic.BulkCreateView):
    pass


class PluginObjectBulkEditView(generic.BulkEditView):
    pass


class PluginObjectBulkDeleteView(generic.BulkDeleteView):
    pass


class PluginObjectBulkRenameView(generic.BulkRenameView):
    pass
