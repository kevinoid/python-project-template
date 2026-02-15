================
Project Template
================

.. image:: https://img.shields.io/github/actions/workflow/status/kevinoid/python-project-template/tox.yml?branch=main&style=flat&label=build
   :alt: Build Status
   :target: https://github.com/kevinoid/python-project-template/actions/workflows/tox.yml?query=branch%3Amain
.. image:: https://img.shields.io/gitlab/pipeline-status/kevinoid/python-project-template.svg?branch=main&style=flat&label=build
   :alt: Build Status
   :target: https://gitlab.com/kevinoid/python-project-template/-/pipelines?ref=main
.. image:: https://img.shields.io/codecov/c/github/kevinoid/python-project-template.svg?style=flat
   :alt: Coverage
   :target: https://codecov.io/github/kevinoid/python-project-template?branch=main
.. image:: https://img.shields.io/gitlab/coverage/kevinoid/python-project-template/main.svg?style=flat
   :alt: Coverage
   :target: https://gitlab.com/kevinoid/python-project-template/-/graphs/main/charts
.. image:: https://img.shields.io/librariesio/release/pypi/python-project-template.svg?style=flat
   :alt: Dependency Status
   :target: https://libraries.io/github/kevinoid/python-project-template
.. image:: https://readthedocs.org/projects/python-project-template/badge/?version=latest
   :target: https://python-project-template.readthedocs.io/en/latest/
   :alt: Documentation Status
.. image:: https://img.shields.io/pypi/pyversions/python-project-template.svg?style=flat
   :alt: Python Versions
   :target: https://pypi.org/project/python-project-template/
.. image:: https://img.shields.io/pypi/v/python-project-template.svg?style=flat
   :alt: Version on PyPI
   :target: https://pypi.org/project/python-project-template/

A Python project template with pytest_, tox_, Sphinx_ (with sphinx-apidoc_ and
sphinx-argparse_), `GitHub Actions`_, `GitLab CI`_, coveralls_, Codecov_, and
several linters including flake8_ (with many plugins), Bandit_, Black_,
pyroma_, and others.

This template is the basis of my own Python projects, representing my current
preferences.  I am not advocating for these choices nor this template
specifically, although I am happy to discuss or explain any choices made
herein.  It is being published both for my own convenience and in case it may
be useful to others with similar tastes.


Introductory Example
====================

.. code:: python

   import packagename

   packagename.foo()


(Mis-)Features
==============

* All module sources are in ``src`` rather than the top-level directory.
  I was initially against this idea, but was swayed by Ionel Cristian Mărieș'
  `Packaging a python library`_, Hynek Schlawack's `Testing & Packaging`_, and
  pytest `Good Integration Practices`_.
* Minimally constrained top-level dependencies are declared in
  ``requirements/*.in`` files.  Full, exact, hash-checked_, known-good
  dependency versions are stored in ``requirements/*.txt``.  These can be
  generated using ``pip-compile`` from pip-tools_ or (if hashes are not
  required) ``pip install && pip freeze`` in a fresh virtual environment:

  .. code:: sh

      for requirements in requirements/*.in; do
          pip-compile --generate-hashes "$requirements"
      done

  This system has the benefit of allowing easy installation of fully or
  minimally constrained dependencies from many tools (``pip``, ``tox``, etc.)
  without duplication.

  I have experimented with several other approaches, including `pip constraint
  files`_ (``constraints.txt``), Pipenv_ (``Pipfile``/``Pipfile.lock``),
  Poetry_ (``pyproject.toml``), and a few others, along with other tools to
  sync with or generate ``requirements.txt`` and ``setup.cfg``.  Although these
  approaches have several benefits, I think the additional complexity (both
  inherent and when integrating with other tools like tox) currently outweighs
  their value.
* `tox`_ (used for CI) is configured to use minimally constrained dependencies.
  This is desirable for library packages, since user installs are minimally
  constrained.  If the package will be deployed as an application using
  ``requirements.txt``, consider changing ``requirements*.in`` to
  ``requirements*.txt`` in ``tox.ini`` to test using exact dependency versions.


Installation
============

`This package`_ can be installed using pip_, by running:

.. code:: sh

   pip install python-project-template


Recipes
=======

.. code:: python

   import packagename

   packagename.bar(packagename.baz())

.. === End of Sphinx index content ===


Documentation
=============

The `project documentation`_ is hosted on `Read the Docs`_.  See the `CLI
documentation`_ for command-line options and usage, and the `API documentation`_
for the Python API.


Contributing
============

Contributions are welcome and very much appreciated!  See the `contributing
guidelines`_ for recommendations.


License
=======

This project is available under the terms of the `MIT License`_.
See the `summary at TLDRLegal`_

The `template`_ upon which this project is based is available under the
terms of `CC0 1.0 Universal`_.

.. === Begin reference names ===

.. _API documentation: https://python-project-template.readthedocs.io/en/latest/api/modules.html
.. _Bandit: https://github.com/PyCQA/bandit
.. _Black: https://github.com/ambv/black
.. _CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/
.. _CLI documentation: https://python-project-template.readthedocs.io/en/latest/cli.html
.. _Codecov: https://codecov.io/
.. _GitHub Actions: https://docs.github.com/actions
.. _GitLab CI: https://docs.gitlab.com/ee/ci/
.. _Good Integration Practices: https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code
.. _MIT License: https://github.com/kevinoid/python-project-template/blob/main/LICENSE.txt
.. _Packaging a python library: https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
.. _Pipenv: https://pipenv.readthedocs.io/
.. _Poetry: https://poetry.eustace.io/
.. _Read the Docs: https://readthedocs.org/
.. _Sphinx: https://www.sphinx-doc.org/
.. _Testing & Packaging: https://hynek.me/articles/testing-packaging/
.. _contributing guidelines: https://github.com/kevinoid/python-project-template/blob/main/CONTRIBUTING.rst
.. _coveralls: https://coveralls.io/
.. _flake8: https://flake8.readthedocs.io/
.. _hash-checked: https://pip.pypa.io/en/stable/reference/pip_install/#hash-checking-mode
.. _pip constraint files: https://pip.pypa.io/en/stable/user_guide/#constraints-files
.. _pip-tools: https://github.com/jazzband/pip-tools
.. _pip: https://pip.pypa.io/
.. _project documentation: https://python-project-template.readthedocs.io/
.. _pyroma: https://github.com/regebro/pyroma
.. _pytest: https://pytest.org/
.. _sphinx-apidoc: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
.. _sphinx-argparse: https://sphinx-argparse.readthedocs.io
.. _summary at TLDRLegal: https://tldrlegal.com/license/mit-license
.. _template: https://github.com/kevinoid/python-project-template
.. _this package: https://pypi.org/project/python-project-template/
.. _tox: https://tox.readthedocs.io
