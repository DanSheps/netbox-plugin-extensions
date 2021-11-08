from extras.plugins import PluginConfig


try:
    from importlib.metadata import metadata
except ModuleNotFoundError:
    from importlib_metadata import metadata

plugin = metadata('netbox_plugin_extensions')


class NetboxPluginExtensions(PluginConfig):
    name = plugin.get('Name').replace('-', '_')
    verbose_name = plugin.get('Summary')
    description = plugin.get('Description')
    version = plugin.get('Version')
    author = plugin.get('Author')
    author_email = plugin.get('Author-email')
    base_url = 'netbox-plugin-extensions'
    min_version = '3.0'
    required_settings = []
    caching_config = {}
    default_settings = {}


config = NetboxPluginExtensions
