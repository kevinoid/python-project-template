"""packagename.cli unit tests."""

from io import StringIO
from unittest.mock import Mock, patch

import pytest

from packagename import cli


@patch('sys.stdout', new_callable=StringIO)
@patch('sys.stderr', new_callable=StringIO)
def test_main_help_prints_usage_then_exits(
    mock_stderr: Mock,
    mock_stdout: Mock,
) -> None:
    with pytest.raises(SystemExit) as excinfo:
        cli.main(['packagename', '--help'])
    stderr_content = mock_stderr.getvalue()
    stdout_content = mock_stdout.getvalue()
    assert not stderr_content
    assert 'packagename' in stdout_content
    assert '--help' in stdout_content
    assert excinfo.value.code == 0
