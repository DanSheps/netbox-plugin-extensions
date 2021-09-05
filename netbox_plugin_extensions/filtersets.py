from netbox.filtersets import BaseFilterSet, OrganizationalModelFilterSet, PrimaryModelFilterSet, \
    ChangeLoggedModelFilterSet


class PluginBaseFilterSet(BaseFilterSet):
    pass


class PluginChangeLoggedModelFilterSet(ChangeLoggedModelFilterSet):
    pass


class PluginPrimaryModelFilterSet(PrimaryModelFilterSet):
    pass


class PluginOrganizationalModelFilterSet(OrganizationalModelFilterSet):
    pass
