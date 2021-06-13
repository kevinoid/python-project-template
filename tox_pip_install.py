#!/usr/bin/env python
# This file is part of packagename <https://github.com/kevinoid/packagename>
# Made available under CC0 1.0 Universal, see LICENSE.txt
# Copyright 2019-2020 Kevin Locke <kevin@kevinlocke.name>
"""
Script to reinstall pip before running `pip install`.

Workaround for https://bugs.debian.org/962654
"""

import os
import subprocess
import sys

# Must be invoked with pip package (optionally version-constrained) as first
# argument, install options+packages as subsequent options.
if len(sys.argv) < 3 or not sys.argv[1].startswith('pip'):
    sys.stderr.write(
        'Usage: ' + sys.argv[0] + ' <pip version> [options] <packages...>\n'
    )
    sys.exit(1)

# Workaround is only needed on Debian (and derivatives)
if os.path.exists('/etc/debian_version'):
    pip_result = subprocess.run([
        sys.executable,
        '-m',
        'pip',
        'install',
        '--force',
        sys.argv[1],
    ])
    if pip_result.returncode != 0:
        sys.exit(pip_result.returncode)

# Note: os.exec exits parent process without waiting for child on Windows.
# Do not use (caller would think install is complete when it is not).
pip_result = subprocess.run([
    sys.executable,
    '-m',
    'pip',
    'install',
] + sys.argv[2:])
sys.exit(pip_result.returncode)
