from django import template
from django.urls import reverse
from netbox_plugin_extensions.templatetags.plugin_helpers import get_returnurl

from extras.models import ExportTemplate
from utilities.utils import prepare_cloned_fields
from .plugin_helpers import _get_plugin_viewname

register = template.Library()


#
# Instance buttons
#

@register.inclusion_tag('buttons/clone.html')
def plugin_clone_button(instance):
    url = reverse(_get_plugin_viewname(instance, 'add'))

    # Populate cloned field values
    param_string = prepare_cloned_fields(instance)
    if param_string:
        url = f'{url}?{param_string}'

    return {
        'url': url,
    }


@register.inclusion_tag('buttons/edit.html')
def plugin_edit_button(instance):
    viewname = _get_plugin_viewname(instance, 'edit')
    url = reverse(viewname, kwargs={'pk': instance.pk})

    return {
        'url': url,
    }


@register.inclusion_tag('buttons/delete.html')
def plugin_delete_button(instance):
    viewname = _get_plugin_viewname(instance, 'delete')
    url = reverse(viewname, kwargs={'pk': instance.pk})

    return {
        'url': url,
    }


#
# List buttons
#

@register.inclusion_tag('buttons/add.html')
def plugin_add_button(instance):
    viewname = _get_plugin_viewname(instance, 'add')
    url = reverse(viewname)

    return {
        'add_url': url,
    }


@register.inclusion_tag('buttons/import.html')
def plugin_import_button(instance):
    viewname = _get_plugin_viewname(instance, 'import')

    return {
        'import_url': viewname,
    }


@register.inclusion_tag('buttons/export.html', takes_context=True)
def plugin_export_button(context, content_type=None):
    add_exporttemplate_link = None

    if content_type is not None:
        user = context['request'].user
        export_templates = ExportTemplate.objects.restrict(user, 'view').filter(content_type=content_type)
        if user.is_staff and user.has_perm('extras.add_exporttemplate'):
            add_exporttemplate_link = f"{reverse('extras:exporttemplate_add')}?content_type={content_type.pk}"
    else:
        export_templates = []

    return {
        'url_params': context['request'].GET,
        'export_templates': export_templates,
        'add_exporttemplate_link': add_exporttemplate_link,
    }

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
