from netbox.models import PrimaryModel, OrganizationalModel, NestedGroupModel, ChangeLoggedModel, BigIDModel

__all__ = (
    'PluginBigIDModel',
    'PluginChangeLoggedModel',
    'PluginNestedGroupModel',
    'PluginOrganizationalModel',
    'PluginPrimaryModel',
)


class PluginBigIDModel(BigIDModel):

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


class PluginPrimaryModel(PrimaryModel):

    class Meta:
        abstract = True
