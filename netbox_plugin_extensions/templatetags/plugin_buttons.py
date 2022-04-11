from django import template
from django.urls import reverse
from netbox_plugin_extensions.templatetags.plugin_helpers import get_returnurl

from extras.models import ExportTemplate
from utilities.utils import prepare_cloned_fields
from .plugin_helpers import _get_plugin_viewname
from utilities.templatetags.buttons import clone_button, edit_button, delete_button, add_button, import_button, \
    export_button

register = template.Library()


#
# Instance buttons
#
plugin_clone_button = clone_button
plugin_edit_button = edit_button
plugin_delete_button = delete_button


#
# List buttons
#
plugin_add_button = add_button
plugin_import_button = import_button
plugin_export_button = export_button


#
# Table buttons
#
@register.inclusion_tag('netbox_plugin_extensions/buttons/tr_edit.html')
def plugin_tr_edit_button(instance, extra=None, parent=None):
    viewname = _get_plugin_viewname(instance, 'edit')
    return_url = get_returnurl(instance, parent)
    url = reverse(viewname, kwargs={'pk': instance.pk})
    url = f'{url}?return_url={return_url}'

    if extra is not None:
        url = f'{url}{extra}'

    return {
        'url': url,
    }


@register.inclusion_tag('netbox_plugin_extensions/buttons/tr_delete.html')
def plugin_tr_delete_button(instance, extra=None, parent=None):
    viewname = _get_plugin_viewname(instance, 'delete')
    return_url = get_returnurl(instance, parent)
    url = reverse(viewname, kwargs={'pk': instance.pk})
    url = f'{url}?return_url={return_url}'

    if extra is not None:
        url = f'{url}{extra}'

    return {
        'url': url,
    }


@register.inclusion_tag('netbox_plugin_extensions/buttons/tr_changelog.html')
def plugin_tr_changelog_button(instance, extra=None, parent=None):
    viewname = _get_plugin_viewname(instance, 'changelog')
    url = reverse(viewname, kwargs={'pk': instance.pk})
    url = f'{url}'

    return {
        'url': url,
    }
