from setuptools import find_packages, setup

setup(
    name='netbox-plugin-extensions',
    version='1.0.4',
    description='Wrappers for Netbox Generic Objects',
    url='https://github.com/dansheps/netbox-plugin-extensions',
    author='Daniel Sheppard',
    license='All rights reserved',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)