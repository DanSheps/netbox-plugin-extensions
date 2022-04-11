from django import template
from django.apps import apps
from django.urls import NoReverseMatch, reverse

from extras.plugins import PluginConfig
from utilities.templatetags.helpers import viewname, validated_viewname

register = template.Library()

__all__ = (
    'plugin_viewname',
    'plugin_validated_viewname',
)


def _resolve_namespace(instance):
    """
    Get the appropriate namespace for the app based on whether it is a Plugin or base application
    """

    app = apps.get_app_config(instance._meta.app_label)
    if isinstance(app, PluginConfig):
        return f'plugins:{app.label}'
    return f'{app.label}'


def get_returnurl(instance, parent=None):
    """
    Get an appropriate return url
    """
    if parent is None:
        return reverse(_get_plugin_viewname(instance, 'list'))
    else:
        return reverse(_get_plugin_viewname(parent), kwargs={'pk': parent.pk})


def _get_plugin_viewname(instance, action=None):
    """
    Return the appropriate viewname for adding, editing, viewing changelog or deleting an instance.
    """

    # Validate action
    if action is not None:
        assert action in ('add', 'edit', 'delete', 'list', 'changelog', 'import', 'export')
    app_label = _resolve_namespace(instance)
    if action is not None:
        viewname = f'{app_label}:{instance._meta.model_name}_{action}'
    else:
        viewname = f'{app_label}:{instance._meta.model_name}'
    return viewname


plugin_viewname = viewname
plugin_validated_viewname = validated_viewname
