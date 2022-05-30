"""
Configuration file for the Sphinx documentation builder.

This file does only contain a selection of the most common options. For a
full list see the documentation:
https://www.sphinx-doc.org/en/master/config
"""

# Skip lint checks to preserve generated file sections and comments
# pylint: disable=invalid-name, wrong-import-position
# isort:skip_file

import os.path
import re
import sys

from configparser import ConfigParser

# Add parent dir to path for importing __version__ from packagename below
_project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(_project_path, 'src'))


_setup_cfg = ConfigParser()
_setup_cfg_path = os.path.join(_project_path, 'setup.cfg')
with open(_setup_cfg_path, encoding='utf8') as _setup_file:
    _setup_cfg.read_file(_setup_file)


# -- Project information -----------------------------------------------------

project = _setup_cfg.get('metadata', 'friendly_name')
author = '%s <%s>' % (  # pylint: disable=consider-using-f-string
    _setup_cfg.get('metadata', 'author'),
    _setup_cfg.get('metadata', 'author_email'),
)
# pylint: disable=redefined-builtin
copyright = _setup_cfg.get('metadata', 'copyright')
# pylint: enable=redefined-builtin

# The full version, including alpha/beta/rc tags
# pylint: disable=import-error
from packagename import __version__ as release  # noqa: E402

# pylint: enable=import-error

# The short X.Y version
_version_match = re.match('[0-9.]+', release)
assert _version_match is not None, '__version__ must start with a number'
version = _version_match.group(0)


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxarg.ext',
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# List of (domain, target) pairs to ignore warnings about in "nitpicky mode"
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpick_ignore
nitpick_ignore = [
    # Typeshed type for csv.writer() return value is _csv._writer, which is
    # not recognized by Sphinx <https://stackoverflow.com/q/51264355>
    ('py:class', '_csv._writer'),
]
# Same as nitpick_ignore, except domain and target are regular expressions.
# nitpick_ignore_regex = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Additional reStructuredText to include at the end of every source
# Define some useful substitutions:
rst_epilog = '\n'.join(
    '.. |' + name + '| replace:: ' + value
    for name, value in {'project': project}.items()
)


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'python-project-templatedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',
    #
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    #
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    #
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        'python-project-template.tex',
        'python-project-template Documentation',
        'Kevin Locke \\textless{}kevin@kevinlocke.name\\textgreater{}',
        'manual',
    )
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        'python-project-template',
        'python-project-template Documentation',
        [author],
        1,
    )
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'python-project-template',
        'python-project-template Documentation',
        author,
        'python-project-template',
        'One line description of project.',
        'Miscellaneous',
    )
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Map external identifiers to (base URI, inventory) pair.  None is objects.inv
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
