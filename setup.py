#!/usr/bin/env python

import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = ['swaggergenerator3']
requires = [
    'flex >= 5.4.1',  # https://github.com/pipermerriam/flex/pull/111
    'pyyaml',
]

with open('README.rst') as f:
    readme = f.read()

# This hack is from http://stackoverflow.com/a/7071358/1231454;
# the version is kept in a separate file and gets parsed - this
# way, setup.py doesn't have to import the package.
# source repo :: https://github.com/venmo/swaggergenerator

VERSIONFILE = 'swaggergenerator3/_version.py'

version_line = open(VERSIONFILE).read()
version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
match = re.search(version_re, version_line, re.M)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Could not find version in '%s'" % VERSIONFILE)

setup(
    name='swaggergenerator',
    version=version,
    description='Automatically generate swagger/OAS schemas from example api interactions.',
    long_description=readme,
    author='Simon Weber',
    author_email='simon@venmo.com',
    url='https://github.com/goibibo/swaggergenerator3',
    packages=packages,
    package_dir={'swaggergenerator3': 'swaggergenerator3'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ),
)
