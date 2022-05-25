# This file is part of python-project-template
# Made available under the terms of the MIT License, see LICENSE.txt
# Copyright 2019-2022 Kevin Locke <kevin@kevinlocke.name>
"""Command-line interface for packagename."""

from __future__ import absolute_import, division, print_function

import argparse
import logging
import sys

from . import __version__

# Short license message varies by license.
# The text below is based on the GPL short text, modified for the MIT License.
# Change as appropriate.
_VERSION_MESSAGE = (
    '%(prog)s '
    + __version__
    + '''

Copyright 2019-2022 Kevin Locke <kevin@kevinlocke.name>

%(prog)s is free software; you can redistribute it and/or modify
it under the terms of the MIT License.

%(prog)s is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
the terms of the MIT License for more details.'''
)

_logger = logging.getLogger(__name__)


def _setup_logging(level=None):
    """
    Initialize the logging framework with a root logger for the console.

    :param level: log level suitable for :py:func:`logging.Logger.setLevel`
    :type level: int
    """
    handler = logging.StreamHandler()
    rootlogger = logging.getLogger()
    rootlogger.addHandler(handler)
    if level is not None:
        rootlogger.setLevel(level)


def _build_argument_parser():
    """
    Build parser for command line options.

    :return: argument parser
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] <file...>',
        description='Do packagename stuff.',
        # Use raw formatter to avoid mangling version text
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '-o',
        '--output',
        type=argparse.FileType('w'),
        default='-',
        help='Output file (default: -)',
    )
    parser.add_argument(
        '-q',
        '--quiet',
        action='count',
        help='Decrease verbosity (less detailed output)',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        help='Increase verbosity (more detailed output)',
    )
    parser.add_argument(
        '-V',
        '--version',
        action='version',
        help='Output version and license information',
        version=_VERSION_MESSAGE,
    )
    parser.add_argument(
        'input_files',
        nargs='+',
        metavar='file...',
        help='File(s) on which to do packagename stuff',
    )
    return parser


def main(argv=sys.argv):  # pylint: disable=dangerous-default-value
    """
    Entry point for packagename command-line tool.

    :param argv: command-line arguments
    :type argv: list[str]

    :return: exit code
    :rtype: int
    """
    parser = _build_argument_parser()
    args = parser.parse_args(args=argv[1:])

    # Set log level based on verbosity requested (default of INFO)
    verbosity = (args.quiet or 0) - (args.verbose or 0)
    _setup_logging(logging.INFO + verbosity * 10)

    # Log version to aid debugging
    _logger.debug('packagename %s', __version__)

    try:
        # Do stuff here
        pass
    except Exception as exc:  # pylint: disable=broad-except
        _logger.error('Unhandled Error: %s', exc, exc_info=True)
        return 1

    return 0
