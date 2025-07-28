# PYTHON_ARGCOMPLETE_OK
# This file is part of python-project-template
# Made available under the terms of the MIT License, see LICENSE.txt
# Copyright 2019-2022 Kevin Locke <kevin@kevinlocke.name>
"""Command-line interface for packagename."""

import argparse
import logging
import os.path
import sys

from typing import Any, Sequence

try:
    from argcomplete import autocomplete

    _HAVE_AUTOCOMPLETE = True
except ImportError:
    _HAVE_AUTOCOMPLETE = False

from . import __version__

__all__ = [
    'main',
]

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


def _build_argument_parser(**kwargs: Any) -> argparse.ArgumentParser:
    """
    Build parser for command line options.

    :return: argument parser
    """
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] <file...>',
        description='Do packagename stuff.',
        # Use raw formatter to avoid mangling version text
        formatter_class=argparse.RawDescriptionHelpFormatter,
        **kwargs,
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


def main(argv: Sequence[str] = sys.argv) -> int:
    """
    Entry point for packagename command-line tool.

    :param argv: command-line arguments

    :return: exit code
    """
    parser = _build_argument_parser(
        prog=os.path.basename(argv[0]),
    )

    if _HAVE_AUTOCOMPLETE:
        exit_code = None

        def exit_method(code: int = 0) -> None:
            nonlocal exit_code
            exit_code = code

        autocomplete(parser, exit_method=exit_method)
        if exit_code is not None:
            return exit_code

    args = parser.parse_args(args=argv[1:])

    # Set log level based on verbosity requested (default of INFO)
    verbosity = (args.quiet or 0) - (args.verbose or 0)
    logging.basicConfig(level=logging.INFO + verbosity * 10)

    # Log version to aid debugging
    _logger.debug('packagename %s', __version__)

    try:
        # Do stuff here
        pass
    except Exception:  # pylint: disable=broad-except
        _logger.exception('Unhandled Error')
        return 1

    return 0
