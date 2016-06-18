=============================
{{ cookiecutter.project_name }}
=============================

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg?style=flat-square
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/{{ cookiecutter.repo_name }}.svg?style=flat-square
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
    :alt: Monthly downloads

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}.svg?style=flat-square
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
    :alt: Python versions

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?style=flat-square
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Latest Travis CI build status

.. image:: https://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat-square
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master
    :alt: Test coverage

.. image:: https://img.shields.io/codecov/c/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/develop.svg?style=flat-square
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    :alt: Test coverage

.. image:: https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: Code Climate


{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at https://{{ cookiecutter.repo_name }}.readthedocs.io.

Quickstart
----------

Install {{ cookiecutter.project_name }}::

    pip install {{ cookiecutter.repo_name }}

Then add to ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        '{{ cookiecutter.app_name }}',
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python setup.py test

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage-helper`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage-helper`: https://github.com/nephila/cookiecutter-djangopackage-helper
