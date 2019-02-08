================
Project Template
================

.. image:: https://img.shields.io/travis/kevinoid/python-project-template/master.svg?style=flat&label=build+on+linux
   :alt: Build Status: Linux
   :target: https://travis-ci.org/kevinoid/python-project-template
.. image:: https://img.shields.io/appveyor/ci/kevinoid/python-project-template/master.svg?style=flat&label=build+on+windows
   :alt: Build Status: Windows
   :target: https://ci.appveyor.com/project/kevinoid/python-project-template
.. image:: https://img.shields.io/codecov/c/github/kevinoid/python-project-template.svg?style=flat
   :alt: Coverage
   :target: https://codecov.io/github/kevinoid/python-project-template?branch=master
.. image:: https://img.shields.io/david/kevinoid/python-project-template.svg?style=flat
   :alt: Dependency Status
   :target: https://david-dm.org/kevinoid/python-project-template
.. image:: https://img.shields.io/pypi/pyversions/python-project-template.svg?style=flat
   :alt: Python Versions
   :target: https://pypi.org/project/python-project-template/
.. image:: https://img.shields.io/pypi/v/python-project-template.svg?style=flat
   :alt: Version on PyPI
   :target: https://pypi.org/project/python-project-template/

A Python project template with pytest_, tox_, AppVeyor_, `Travis CI`_,
coveralls_, Codecov_, and several linters (including pylama_, Bandit_, pyroma_,
and others).

This template is the basis of my own Python projects, representing my current
preferences.  I am not advocating for these choices nor this template
specifically, although I am happy to discuss or explain any choices made
herein.  It is being published both for my own convenience and in case it may
be useful to others with similar tastes.


Introductory Example
====================

.. code:: python

   import modulename

   modulename.foo()


(Mis-)Features
==============

* Minimally constrained top-level dependencies are declared in
  ``install_requires`` in ``setup.cfg``.  Test and development tool
  dependencies are declared in ``requirements-test.in`` and
  ``requirements-dev.in`` respectively.  Full, exact, known-good dependency
  versions are stored in ``requirements.txt``, ``requirements-test.txt``, and
  ``requirements-dev.txt``.  These can be generated using ``pip-compile`` from
  pip-tools_ or ``pip install && pip freeze`` in a fresh virtual environment:

  .. code:: sh

      pip-compile -o requirements.txt setup.py
      pip-compile -o requirements-test.txt requirements-test.in
      pip-compile -o requirements-dev.txt requirements-dev.in

  I have experimented with several other approaches, including `pip constraint
  files`_ (``constraints.txt``), Pipenv_ (``Pipfile``/``Pipfile.lock``),
  Poetry_ (``pyproject.toml``), and a few others, along with other tools to
  sync with or generate ``requirements.txt`` and ``setup.cfg``.  Although these
  tools are useful, I think the additional complexity (both inherent and when
  integrating with other tools like tox) currently outweighs their value.


Installation
============

`This package`_ can be installed using pip_, by running:

.. code:: sh

   pip install python-project-template


Recipes
=======


API Docs
========

To use this module as a library, see the generated `API Documentation`_.


Contributing
============

Contributions are welcome and very much appreciated!  See the `contributing
guidelines`_ for recommendations.


License
=======

This template is available under the terms of `CC0 1.0 Universal`_.

.. _API documentation: https://kevinoid.github.io/python-project-template/api
.. _AppVeyor: https://appveyor.com/
.. _Bandit: https://github.com/PyCQA/bandit
.. _CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/
.. _Codecov: https://codecov.io/
.. _Pipenv: https://pipenv.readthedocs.io/
.. _Poetry: https://poetry.eustace.io/
.. _Travis CI: https://travis-ci.org/
.. _contributing guidelines: CONTRIBUTING.rst
.. _coveralls: https://coveralls.io/
.. _pip constraint files: https://pip.pypa.io/en/stable/user_guide/#constraints-files
.. _pip-tools: https://github.com/jazzband/pip-tools
.. _pip: https://pip.pypa.io/
.. _pylama: https://github.com/klen/pylama
.. _pyroma: https://github.com/regebro/pyroma
.. _pytest: https://pytest.org/
.. _this package: https://pypi.org/project/python-project-template/
.. _tox: https://tox.readthedocs.io
