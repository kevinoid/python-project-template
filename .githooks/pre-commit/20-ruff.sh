#!/bin/sh
# Run ruff check (and format --check) on changed .py and .pyi files

set -Ceu

# Ensure ruff is available.
# Could use tox/venv, but they are too heavy/slow for my tastes
if ! command -v ruff >/dev/null ; then
	# shellcheck disable=SC2016
	echo 'Warning: ruff not on $PATH.  Skipping pre-commit check.' >&2
	exit 0
fi

git diff -z --cached --name-only --diff-filter=AM -- '*.py' '*.pyi' |
	xargs -0r ruff check --

git diff -z --cached --name-only --diff-filter=AM -- '*.py' '*.pyi' |
	xargs -0r ruff format --check --diff --
