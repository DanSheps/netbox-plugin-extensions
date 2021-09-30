from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.utils.http import is_safe_url

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

class PluginGetReturnURLMixin:
    """
    Provides logic for determining where a user should be redirected after processing a form.
    """
    default_return_url = None

    def get_return_url(self, request, obj=None):

        # First, see if `return_url` was specified as a query parameter or form data. Use this URL only if it's
        # considered safe.
        query_param = request.GET.get('return_url') or request.POST.get('return_url')
        if query_param and is_safe_url(url=query_param, allowed_hosts=request.get_host()):
            return query_param

        # Next, check if the object being modified (if any) has an absolute URL.
        if obj is not None and obj.pk and hasattr(obj, 'get_absolute_url'):
            return obj.get_absolute_url()

        # Fall back to the default URL (if specified) for the view.
        if self.default_return_url is not None:
            return reverse(self.default_return_url)

        # Attempt to dynamically resolve the list view for the object
        if hasattr(self, 'queryset'):
            model_opts = self.queryset.model._meta
            try:
                return reverse(f'plugins:{model_opts.app_label}:{model_opts.model_name}_list')
            except NoReverseMatch:
                pass

        # If all else fails, return home. Ideally this should never happen.
        return reverse('home')


class PluginObjectListView(generic.ObjectListView):
    template_name = 'netbox_plugin_extensions/generic/object_list.html'


class PluginObjectView(generic.ObjectView):
    template_name = 'netbox_plugin_extensions/generic/object.html'


class PluginObjectEditView(PluginGetReturnURLMixin, generic.ObjectEditView):
    template_name = 'netbox_plugin_extensions/generic/object_edit.html'


class PluginObjectDeleteView(PluginGetReturnURLMixin, generic.ObjectDeleteView):
    template_name = 'netbox_plugin_extensions/generic/object_delete.html'


class PluginObjectImportView(PluginGetReturnURLMixin, generic.ObjectImportView):
    template_name = 'netbox_plugin_extensions/generic/object_import.html'


class PluginObjectBulkImportView(PluginGetReturnURLMixin, generic.BulkImportView):
    template_name = 'netbox_plugin_extensions/generic/object_bulk_import.html'


class PluginObjectBulkCreateView(PluginGetReturnURLMixin, generic.BulkCreateView):
    pass


class PluginObjectBulkEditView(PluginGetReturnURLMixin, generic.BulkEditView):
    template_name = 'netbox_plugin_extensions/generic/object_bulk_edit.html'


class PluginObjectBulkDeleteView(PluginGetReturnURLMixin, generic.BulkDeleteView):
    template_name = 'netbox_plugin_extensions/generic/object_bulk_delete.html'


class PluginObjectBulkRenameView(PluginGetReturnURLMixin, generic.BulkRenameView):
    template_name = 'netbox_plugin_extensions/generic/object_bulk_rename.html'
