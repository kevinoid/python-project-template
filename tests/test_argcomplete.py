"""unit tests for argument completion."""

import os
import sys
import warnings

from io import StringIO

from packagename import cli

try:
    from unittest.mock import mock_open, patch
except ImportError:
    from mock import mock_open, patch

# Note: Path not created on the filesystem.  Only used for mocking.
_COMPLETIONS_FILENAME = 'unittest/mock/argcomplete'


def _open_mock_for(for_file):
    """
    Create a function which returns a Mock only for a given file.

    :param for_file: file for which a Mock should be returned.
    :type for_file: str

    :return: side_effect function which returns a Mock when called with
             for_file and delegates to open() otherwise.
    :rtype: Callable
    """

    def maybe_mock_open(file, *args, **kwargs):
        r"""
        Open a file or create a Mock for the file.

        :param file: path of file to open
        :type file: str
        :param \*args: arguments passed to open()
        :type \*args: Any
        :param \**kwargs: keyword arguments passed to open()
        :type \**kwargs: Any

        :return: a new Mock if file is for_file, open(...) otherwise.
        :rtype: io.TextIOWrapper
        """
        if file == for_file:
            mock_file = mock_open().return_value
            maybe_mock_open.mock_files.append(mock_file)
            return mock_file

        # Note: Tests run with -X warn_default_encoding which raises
        # EncodingWarning for open() without encoding=
        # https://docs.python.org/3/library/io.html#io-encoding-warning
        # Suppress this warning when open() is used for mocking.
        with warnings.catch_warnings():
            try:
                warnings.simplefilter('ignore', EncodingWarning)
            except NameError:
                # EncodingWarning added in Python 3.10.
                # No need to ignore it if it doesn't exist
                pass

            # pylint: disable-next=unspecified-encoding
            return open(file, *args, **kwargs)

    # Save created Mocks so the caller can test them
    maybe_mock_open.mock_files = []
    return maybe_mock_open


@patch.dict(
    os.environ,
    {
        '_ARGCOMPLETE': '1',
        '_ARGCOMPLETE_STDOUT_FILENAME': _COMPLETIONS_FILENAME,
        'COMP_LINE': 'packagename -',
        'COMP_POINT': '13',
        'COMP_TYPE': '33',
    },
)
@patch('argcomplete.open', side_effect=_open_mock_for(_COMPLETIONS_FILENAME))
@patch('sys.argv', ['packagename'])
@patch('sys.stdout', new_callable=StringIO)
@patch('sys.stderr', new_callable=StringIO)
def test_argcomplete_dash_options(mock_stderr, mock_stdout, mock_open_comp):
    assert cli.main(sys.argv) == 0
    assert not mock_stderr.getvalue()
    assert not mock_stdout.getvalue()
    open_args, _open_kwargs = mock_open_comp.call_args_list[0]
    assert open_args[0] == _COMPLETIONS_FILENAME
    assert open_args[1] in ('w', 'wb')
    mock_files = mock_open_comp.side_effect.mock_files
    assert len(mock_files) == 1

    expect_comp = '\v'.join(
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
    mock_files[0].write.assert_called_once_with(
        expect_comp if open_args[1] == 'w' else expect_comp.encode('utf-8')
    )
