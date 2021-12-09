from setuptools import find_packages, setup

setup(
    name='netbox-plugin-extensions',
    version='1.0.8',
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
