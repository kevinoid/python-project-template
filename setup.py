#!/usr/bin/env python3
# This file is part of packagename <https://github.com/kevinoid/packagename>
# Made available under CC0 1.0 Universal, see LICENSE.txt
# Copyright 2019 Kevin Locke <kevin@kevinlocke.name>
"""
Distutils/Setuptools Setup Script.

https://docs.python.org/3/distutils/setupscript.html
"""

import sys

# Allow lowercase "constants" for script
# pylint: disable=invalid-name

setuptools_version = None
try:
    from setuptools import setup, __version__ as setuptools_version
    from pkg_resources import parse_requirements

    # setup.cfg is supported if and only if setuptools.config can be imported.
    # Simpler and more reliable than version string parsing+comparison.
    # pylint: disable=unused-import,ungrouped-imports
    import setuptools.config  # noqa: F401
    # pylint: enable=unused-import,ungrouped-imports
except ImportError:
    # TODO: Use (partial) backport of setuptools.config.read_configuration?
    raise AssertionError(
        'setup.py requires setuptools with support for setup.cfg ' +
        '(%s < 30.3.0)' % (setuptools_version,)
    )


setup_requires = []

# Use pytest-runner for `setup.py test`.  Only install when testing.
# https://docs.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
# https://pypi.org/project/pytest-runner/#conditional-requirement
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires.append('pytest-runner')

# Test requirements in requirements-test.in for venv installation & pip-compile
# See https://github.com/jazzband/pip-tools/pull/492
with open('requirements-test.in') as test_req_file:
    # FIXME: Need a good way to handle install markers
    # See https://github.com/pypa/setuptools/issues/1080
    tests_require = [
        str(test_req) for test_req in parse_requirements(test_req_file)
    ]

setup(
    setup_requires=setup_requires,
)
