"""unit tests for argument completion."""

import os
import sys

from io import StringIO
from typing import Final, cast
from unittest import skipIf
from unittest.mock import Mock, mock_open, patch

from packagename import cli

# argcomplete writes completions to file descriptor 8:
# https://github.com/kislyuk/argcomplete/blob/v3.6.3/argcomplete/finders.py#L131
# which is subsequently redirected to stdout for bash-completion:
# https://github.com/kislyuk/argcomplete/blob/v3.6.3/argcomplete/shell_integration.py#L27
_ARGCOMPLETE_OUT_FD: Final = 8

# argcomplete writes debug output to file descriptor 9:
# https://github.com/kislyuk/argcomplete/blob/v3.6.3/argcomplete/finders.py#L200
# which is subsequently redirected to stderr for bash-completion:
# https://github.com/kislyuk/argcomplete/blob/v3.6.3/argcomplete/shell_integration.py#L27
_ARGCOMPLETE_ERR_FD: Final = 9


class ArgcompleteFdopenMock:  # pylint: disable=too-few-public-methods
    """A callable object for mocking os.fdopen for argcomplete."""

    def __init__(self) -> None:
        """Construct an ArgcompleteFdopenMock."""
        self.completion_file: Mock = mock_open().return_value
        self.error_file: Mock = mock_open().return_value

    def __call__(self, fd: int, mode: str) -> Mock:  # noqa: ARG002
        r"""
        Open a mock file descriptor.

        :param fd: file descriptor to open
        :param mode: mode in which the file descriptor is opened

        :return: a file Mock.
        """
        if fd == _ARGCOMPLETE_OUT_FD:
            return self.completion_file

        if fd == _ARGCOMPLETE_ERR_FD:
            return self.error_file

        return cast('Mock', mock_open().return_value)


@patch.dict(
    os.environ,
    {
        '_ARGCOMPLETE': '1',
        'COMP_LINE': 'packagename -',
        'COMP_POINT': '13',
        'COMP_TYPE': '33',
    },
)
@patch('os.fdopen', side_effect=ArgcompleteFdopenMock())
@patch('sys.argv', ['packagename'])
@patch('sys.stdout', new_callable=StringIO)
@patch('sys.stderr', new_callable=StringIO)
def test_argcomplete_dash_options(
    mock_stderr: Mock,
    mock_stdout: Mock,
    mock_fdopen_comp: Mock,
) -> None:
    assert cli.main(sys.argv) == 0
    assert not mock_stderr.getvalue()
    assert not mock_stdout.getvalue()

    mock_fdopen_comp.assert_any_call(_ARGCOMPLETE_OUT_FD, 'w')
    mock_fdopen_comp.assert_any_call(_ARGCOMPLETE_ERR_FD, 'w')
    assert mock_fdopen_comp.call_count == 2  # noqa: PLR2004

    mock_fdopen_comp.side_effect.error_file.write.assert_not_called()

    mock_fdopen_comp.side_effect.completion_file.write.assert_called_once_with(
        '\v'.join(  # noqa: FLY002
            (
                '-h',
                '--help',
                '-o',
                '--output',
                '-q',
                '--quiet',
                '-v',
                '--verbose',
                '-V',
                '--version',
            ),
        ),
    )


@skipIf(os.name == 'nt', 'Not working.  Needs investigation.')
@patch.dict(
    os.environ,
    {
        '_ARGCOMPLETE': '1',
        'COMP_LINE': 'packagename --output L',
        'COMP_POINT': '22',
        'COMP_TYPE': '33',
    },
)
@patch('os.fdopen', side_effect=ArgcompleteFdopenMock())
@patch('sys.argv', ['packagename'])
@patch('sys.stdout', new_callable=StringIO)
@patch('sys.stderr', new_callable=StringIO)
def test_argcomplete_output_files(
    mock_stderr: Mock,
    mock_stdout: Mock,
    mock_fdopen_comp: Mock,
) -> None:
    assert cli.main(sys.argv) == 0
    assert not mock_stderr.getvalue()
    assert not mock_stdout.getvalue()

    mock_fdopen_comp.assert_any_call(_ARGCOMPLETE_OUT_FD, 'w')
    mock_fdopen_comp.assert_any_call(_ARGCOMPLETE_ERR_FD, 'w')
    assert mock_fdopen_comp.call_count == 2  # noqa: PLR2004

    mock_fdopen_comp.side_effect.error_file.write.assert_not_called()

    mock_fdopen_comp.side_effect.completion_file.write.assert_called_once_with(
        'LICENSE.txt ',
    )
