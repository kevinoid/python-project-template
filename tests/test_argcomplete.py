"""unit tests for argument completion."""

import os
import sys

from io import StringIO
from typing import Any, Callable
from unittest.mock import Mock, mock_open, patch

from packagename import cli


def _make_fdopen_mock() -> Callable[..., Any]:
    """
    Create a function which returns a Mock only for a given file.

    :param for_file: file for which a Mock should be returned.

    :return: side_effect function which returns a Mock when called with
             for_file and delegates to open() otherwise.
    """

    def maybe_mock_fdopen(fd: int, mode: str) -> Any:
        r"""
        Open a file or create a Mock for the file.

        :param fd: file descriptor to open
        :param mode: mode in which the file descriptor is opened

        :return: a Mock if file is 8 or 9 and mode is "w".
        """
        assert fd in (8, 9)
        assert mode == 'w'

        if fd == 8:
            return maybe_mock_fdopen.completion_file

        return maybe_mock_fdopen.error_file

    # Save created Mocks so the caller can test them
    maybe_mock_fdopen.completion_file = mock_open().return_value
    maybe_mock_fdopen.error_file = mock_open().return_value
    return maybe_mock_fdopen


@patch.dict(
    os.environ,
    {
        '_ARGCOMPLETE': '1',
        'COMP_LINE': 'packagename -',
        'COMP_POINT': '13',
        'COMP_TYPE': '33',
    },
)
@patch('os.fdopen', side_effect=_make_fdopen_mock())
@patch('sys.argv', ['packagename'])
@patch('sys.stdout', new_callable=StringIO)
@patch('sys.stderr', new_callable=StringIO)
def test_argcomplete_dash_options(
    mock_stderr: Mock, mock_stdout: Mock, mock_fdopen_comp: Mock
) -> None:
    assert cli.main(sys.argv) == 0
    assert not mock_stderr.getvalue()
    assert not mock_stdout.getvalue()

    mock_fdopen_comp.assert_any_call(8, 'w')
    mock_fdopen_comp.assert_any_call(9, 'w')
    assert mock_fdopen_comp.call_count == 2

    mock_fdopen_comp.side_effect.error_file.write.assert_not_called()

    mock_fdopen_comp.side_effect.completion_file.write.assert_called_once_with(
        '\v'.join(
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
            )
        )
    )


@patch.dict(
    os.environ,
    {
        '_ARGCOMPLETE': '1',
        'COMP_LINE': 'packagename --output L',
        'COMP_POINT': '22',
        'COMP_TYPE': '33',
    },
)
@patch('os.fdopen', side_effect=_make_fdopen_mock())
@patch('sys.argv', ['packagename'])
@patch('sys.stdout', new_callable=StringIO)
@patch('sys.stderr', new_callable=StringIO)
def test_argcomplete_output_files(
    mock_stderr: Mock, mock_stdout: Mock, mock_fdopen_comp: Mock
) -> None:
    assert cli.main(sys.argv) == 0
    assert not mock_stderr.getvalue()
    assert not mock_stdout.getvalue()

    mock_fdopen_comp.assert_any_call(8, 'w')
    mock_fdopen_comp.assert_any_call(9, 'w')
    assert mock_fdopen_comp.call_count == 2

    mock_fdopen_comp.side_effect.error_file.write.assert_not_called()

    mock_fdopen_comp.side_effect.completion_file.write.assert_called_once_with(
        'LICENSE.txt '
    )
