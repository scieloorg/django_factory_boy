#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django_factory_boy',
    version='0.0.1',
    author='SciELO',
    author_email='',
    url='http://github.com/scielooarg/django_factory_boy',
    description = 'Uses factory_boy to supply test data factory classes for all stock Django models.',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['factory_boy>=1.0.4'],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
