#!/usr/bin/env python3
# This file is part of packagename <https://github.com/kevinoid/packagename>
# Made available under CC0 1.0 Universal, see LICENSE.txt
# Copyright 2019-2020 Kevin Locke <kevin@kevinlocke.name>
"""
Distutils/Setuptools Setup Script.

https://docs.python.org/3/distutils/setupscript.html
"""

import sys

# Allow lowercase "constants" for script
# pylint: disable=invalid-name

setuptools_version = None
try:
    # isort: off
    from setuptools import __version__ as setuptools_version

    # isort: on

    # setup.cfg is supported if and only if setuptools.config can be imported.
    # Simpler and more reliable than version string parsing+comparison.
    import setuptools.config  # noqa: F401 pylint: disable=unused-import

    from pkg_resources import parse_requirements
    from setuptools import setup
except ImportError:
    # TODO: Use (partial) backport of setuptools.config.read_configuration?
    raise AssertionError(  # pylint: disable=raise-missing-from
        'setup.py requires setuptools with support for setup.cfg '
        + '(%s < 30.3.0)' % (setuptools_version,)
    )


def _load_requirements(req_path):
    """
    Read requirements specifications from a given file path.

    :param req_path: path of requirements file to load
    :type req_path: str

    :return: list of requirement specifications (as strings) in ``req_path``
    :rtype: List[str]
    """
    with open(req_path) as req_file:
        # FIXME: Move deps with markers to extra_depends for old setuptools?
        # https://hynek.me/articles/conditional-python-dependencies/#fixing-sdist
        # https://github.com/pypa/setuptools/issues/1080
        return [str(req) for req in parse_requirements(req_file)]


setup_requires = []

# Use pytest-runner for `setup.py test`.  Only install when testing.
# https://docs.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
# https://pypi.org/project/pytest-runner/#conditional-requirement
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires.append('pytest-runner')

setup(
    install_requires=_load_requirements('requirements.in'),
    setup_requires=setup_requires,
    tests_require=_load_requirements('requirements-test.in'),
)
