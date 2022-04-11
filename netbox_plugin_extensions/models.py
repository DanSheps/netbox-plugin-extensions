from django.db import models
from netbox.models import OrganizationalModel, NestedGroupModel, ChangeLoggedModel, NetBoxModel

__all__ = (
    'PluginBigIDModel',
    'PluginChangeLoggedModel',
    'PluginNestedGroupModel',
    'PluginOrganizationalModel',
    'PluginPrimaryModel',
)


class PluginBigIDModel(models.Model):

    """
    Abstract base model for all data objects. Ensures the use of a 64-bit PK.
    """
    id = models.BigAutoField(
        primary_key=True
    )

    class Meta:
        abstract = True


class PluginChangeLoggedModel(ChangeLoggedModel):

    class Meta:
        abstract = True


class PluginNestedGroupModel(NestedGroupModel):

    class Meta:
        abstract = True


class PluginOrganizationalModel(OrganizationalModel):

    class Meta:
        abstract = True


class PluginPrimaryModel(NetBoxModel):

    class Meta:
        abstract = True
