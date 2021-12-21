# Netbox Plugin Extensions
A collection of plugin extensions for netbox, including generic wrappers around NetBox objects.

### Features

* Compatible views for:
  * Objects (List, Detail, Edit, Delete)
* Database models
  * Primary Models
  * Organizational (NestedGroup)
* Forms
* Fields

### Requirements

* Netbox 3.0+
* Python 3.7+

### Compatibility Matrix

|        | Netbox 2.10 | Netbox 2.11 | Netbox 3.0  | Netbox 3.1.0-1  | Netbox 3.1.2> |
|--------|-------------|-------------|-------------|-----------------|---------------|
| <1.0.4 |      X      |             |             |                 |               |
| 1.0.5  |      X      |      X      |             |                 |               |
| 1.0.6  |      X      |      X      |      X      |        X        |               |
| 1.0.9  |             |             |      X      |        X        |               |
| 1.1.0  |             |             |             |                 |       X       |

### Installation

To install, simply include this plugin in the "install_requires" section of your plugin.

Example:
```python
    install_requires=[
        'netbox-plugin-extensions'
    ],
```

### Configuration

None

### Usage

It is recommended you use fully qualified imports in your code:

`from netbox_plugin_extensions.views import PluginObjectListView`

### Additional Notes

To ease addon development, it is recommended to fully include all fields for your setup.py and include importlib as a
required dependancy to ease generation of the PluginConfig file.

#### setup.py
```python
from setuptools import find_packages, setup

setup(
    name='netbox-plugin-extensions',
    version='1.0.6',
    description='NetBox Plugin Extensions',
    long_description='Wrappers for Netbox Generic Objects',
    url='https://github.com/dansheps/netbox-plugin-extensions/',
    download_url='https://pypi.org/project/netbox-plugin-extensions/',
    author='Daniel Sheppard',
    author_email='dans@dansheps.com',
    maintainer='Daniel Sheppard',
    maintainer_email='dans@dansheps.com',
    license='All rights reserved',
    platform=[],
    keywords=['netbox', 'netbox-plugin'],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'importlib',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
```

#### __init__.py
```python
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

```

### Contribute

Contributions are always welcome!  Please open an issue first before contributing as the scope is going to be kept
intentionally narrow


