from django.forms import BoundField
from django.urls import reverse

from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField


__all__ = (
    'PluginDynamicModelChoiceField',
    'PluginDynamicModelMultipleChoiceField'
)


class PluginDynamicModelChoiceField(DynamicModelChoiceField):
    pass


class PluginDynamicModelMultipleChoiceField(DynamicModelMultipleChoiceField):
    pass
