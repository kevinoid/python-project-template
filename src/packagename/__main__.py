#!/usr/bin/env python3
# This file is part of python-project-template
# Made available under the terms of the MIT License, see LICENSE.txt
# Copyright 2019-2022 Kevin Locke <kevin@kevinlocke.name>
"""Entry point for running packagename as a command-line tool."""

import sys

from .cli import main

sys.exit(main(*sys.argv))
