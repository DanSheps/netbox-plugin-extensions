from netbox.filtersets import BaseFilterSet, OrganizationalModelFilterSet, NetBoxModelFilterSet, \
    ChangeLoggedModelFilterSet


class PluginBaseFilterSet(BaseFilterSet):
    pass


class PluginChangeLoggedModelFilterSet(ChangeLoggedModelFilterSet):
    pass


class PluginPrimaryModelFilterSet(NetBoxModelFilterSet):
    pass


class PluginOrganizationalModelFilterSet(OrganizationalModelFilterSet):
    pass
