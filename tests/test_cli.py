"""packagename.cli unit tests."""

from __future__ import absolute_import, division, print_function

import pytest

from packagename import cli

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


@patch('sys.stdout', new_callable=StringIO)
@patch('sys.stderr', new_callable=StringIO)
def test_main_help_prints_usage_then_exits(mock_stderr, mock_stdout):
    with pytest.raises(SystemExit) as excinfo:
        cli.main('packagename', '--help')
    stderr_content = mock_stderr.getvalue()
    stdout_content = mock_stdout.getvalue()
    assert not stderr_content
    assert 'packagename' in stdout_content
    assert '--help' in stdout_content
    assert excinfo.value.code == 0
