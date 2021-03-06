#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    th-e-core
    ~~~~~~~~~
    
    
"""
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = path.abspath(path.dirname(__file__))
info = {}
with open(path.join("th_e_core", "_version.py")) as f: exec(f.read(), info)

VERSION = info['__version__']

DESCRIPTION = 'This repository provides a set of core functions for several projects of ISC Konstanz.'

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    README = f.read()

NAME = 'th-e-core'
LICENSE = 'LGPLv3'
AUTHOR = 'ISC Konstanz'
MAINTAINER_EMAIL = 'adrian.minde@isc-konstanz.de'
URL = 'https://github.com/isc-konstanz/th-e-core'

INSTALL_REQUIRES = ['numpy',
                    'pandas']

PACKAGES = ['th_e_core']

SETUPTOOLS_KWARGS = {
    'zip_safe': False,
    'include_package_data': True
}

setup(
    name = NAME,
    version = VERSION,
    license = LICENSE,
    description = DESCRIPTION,
    long_description=README,
    author = AUTHOR,
    author_email = MAINTAINER_EMAIL,
    url = URL,
    packages = PACKAGES,
    install_requires = INSTALL_REQUIRES,
    **SETUPTOOLS_KWARGS
)