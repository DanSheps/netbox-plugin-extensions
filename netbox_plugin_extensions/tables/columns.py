from utilities.tables import ButtonsColumn


class PluginButtonsColumn(ButtonsColumn):
    """
    Render edit, delete, and changelog buttons for an object.

    :param model: Model class to use for calculating URL view names
    :param prepend_content: Additional template content to render in the column (optional)
    :param return_url_extra: String to append to the return URL (e.g. for specifying a tab) (optional)
    """

    template_code = """
    {{% if "changelog" in buttons %}}
        <a href="{{% url 'plugins:{app_label}:{model_name}_changelog' pk=record.pk %}}" class="btn btn-outline-dark btn-sm" title="Change log">
            <i class="mdi mdi-history"></i>
        </a>
    {{% endif %}}
    {{% if "edit" in buttons and perms.{app_label}.change_{model_name} %}}
        <a href="{{% url 'plugins:{app_label}:{model_name}_edit' pk=record.pk %}}?return_url={{{{ request.path }}}}{{{{ return_url_extra }}}}" class="btn btn-sm btn-warning" title="Edit">
            <i class="mdi mdi-pencil"></i>
        </a>
    {{% endif %}}
    {{% if "delete" in buttons and perms.{app_label}.delete_{model_name} %}}
        <a href="{{% url 'plugins:{app_label}:{model_name}_delete' pk=record.pk %}}?return_url={{{{ request.path }}}}{{{{ return_url_extra }}}}" class="btn btn-sm btn-danger" title="Delete">
            <i class="mdi mdi-trash-can-outline"></i>
        </a>
    {{% endif %}}
    """
