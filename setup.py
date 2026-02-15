#!/usr/bin/env python3
# This file is part of packagename <https://github.com/kevinoid/packagename>
# Made available under the terms of the MIT License, see LICENSE.txt
# Copyright 2019-2026 Kevin Locke <kevin@kevinlocke.name>
"""
Distutils/Setuptools Setup Script.

https://docs.python.org/3/distutils/setupscript.html
"""

import sys

# Allow lowercase "constants" for script
# pylint: disable=invalid-name

setuptools_version = '0.0.0'
try:
    # isort: off
    from setuptools import __version__ as setuptools_version, setup

    # isort: on

    # setup.cfg is supported if and only if setuptools.config can be imported.
    # Simpler and more reliable than version string parsing+comparison.
    import setuptools.config  # noqa: F401 pylint: disable=unused-import
except ImportError:
    # TODO: Use (partial) backport of setuptools.config.read_configuration?
    raise AssertionError(  # pylint: disable=raise-missing-from
        'setup.py requires setuptools with support for setup.cfg '
        + f'({setuptools_version} < 30.3.0)'
    )


setup_requires = []

# Use pytest-runner for `setup.py test`.  Only install when testing.
# https://docs.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
# https://pypi.org/project/pytest-runner/#conditional-requirement
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires.append('pytest-runner')

setup(
    setup_requires=setup_requires,
)
