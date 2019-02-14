#!/usr/bin/env python3
# This file is part of python-project-template
# Made available under CC0 1.0 Universal, see LICENSE.txt
# Copyright 2019 Kevin Locke <kevin@kevinlocke.name>
"""Entry point for running packagename as a command-line tool."""

import sys

from .cli import main

sys.exit(main(*sys.argv))
