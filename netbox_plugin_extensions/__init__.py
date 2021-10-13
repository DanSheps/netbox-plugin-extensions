from extras.plugins import PluginConfig


class NetboxPluginExtensions(PluginConfig):
    name = 'netbox_plugin_extensions'
    verbose_name = 'Netbox Plugin Extensions'
    description = 'Wrappers for Netbox Generic Objects'
    version = '1.0.4'
    author = 'Daniel Sheppard'
    author_email = 'dans@dansheps.com'
    base_url = 'netbox-plugin-extensions'
    min_version = '3.0'
    required_settings = []
    caching_config = {}
    default_settings = {}


config = NetboxPluginExtensions
