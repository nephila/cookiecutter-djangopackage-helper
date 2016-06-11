=================================
cookiecutter-djangopackage-helper
=================================
.. image:: https://travis-ci.org/nephila/cookiecutter-djangopackage-helper.svg?branch=master
    :target: https://travis-ci.org/nephila/cookiecutter-djangopackage-helper

A cookiecutter_ template for creating reusable Django packages (installable apps) using djangocms-helper.

This a modified cookiecutter template built on top on the awesome `cookiecutter-djangopackage`_ template.

Most of the template code is exactly the same, with just the `djangocms-helper`_ spice added.

Features
--------

Inherited from `cookiecutter-djangopackage`_:

* Sane setup.py for easy PyPI registration/distribution
* Travis-CI configuration
* Codecov configuration
* Tox configuration
* Sphinx Documentation
* BSD licensed by default
* Basic model generation

Added:

* `djangocms-helper`_ integration
* Sphinx tests
* Tox configuration includes django CMS versions
* Basic gitlab-ci configuration
* Codeclimate, QuantifiedCoe configuration

Usage
-----

First, create your empty repo on Github (in our example below, we would call it ``blogging_for_humans``) and set up your virtual environment with your favorite method.

**Note**: Your project will be created with README.rst file containing a pypi badge, a travis-ci badge and a link to documentation on readthedocs.org. You don't need to have these accounts set up before using Cookiecutter or cookiecutter-djangopackage.

Now, get Cookiecutter_. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/nephila/cookiecutter-djangopackage-helper.git

You'll be prompted for some questions, answer them, then it will create a directory that is your new package.

Let's pretend you want to create a reusable Django app called "Blogging-for-Humans", with an app that can be placed
in ``INSTALLED_APPS`` as "blogging_for_humans". Rather than have to copy/paste from other people's projects and
then fight enthusiasm-destroying app layout issues like `setup.py` configuration and creating test
harnesses, you get Cookiecutter_ to do all the work.

**Warning**: After this point, change 'Jane Developer', 'janedev', etc to your own information.

It prompts you for information that it uses to create the app, with defaults in square brackets. Answer them::

    Cloning into 'cookiecutter-djangopackage'...
    remote: Counting objects: 49, done.
    remote: Compressing objects: 100% (33/33), done.
    remote: Total 49 (delta 6), reused 48 (delta 5)
    Unpacking objects: 100% (49/49), done.
    full_name [Your full name here]: Daniel Roy Greenfeld
    email [you@example.com]: pydanny@gmail.com
    github_username [yourname]: pydanny
    project_name [dj-package]: Blogging-for-Humans
    repo_name [blogging_for_humans]:
    app_name [blogging_for_humans]:
    project_short_description [Your project description goes here]: A sample Django package
    models [Comma-separated list of models]: Scoop, Flavor
    django_versions [1.8,1.9]:
    version [0.1.0]:
    create_example_project [N]:
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - ISCL
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]:

Enter the project and take a look around::

    $ cd blogging_for_humans/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit!"
    $ git remote add origin git@github.com:janedev/blogging-for-humans.git
    $ git push -u origin master

Now take a look at your repo. Awesome, right?

It's time to write the code!!!

Running Tests
~~~~~~~~~~~~~

Code has been written, but does it actually work? Let's find out!

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Register on PyPI
~~~~~~~~~~~~~~~~

Once you've got at least a prototype working and tests running, it's time to register the app on PyPI::

    python setup.py register


Releasing on PyPI
~~~~~~~~~~~~~~~~~

Time to release a new version? Easy! Just run::

    $ python setup.py publish

It will answer with something like::

    You probably want to also tag the version now:
          git tag -a 0.1.0 -m 'version 0.1.0'
          git push --tags

Go ahead and follow those instructions.

Add to Django Packages
~~~~~~~~~~~~~~~~~~~~~~

Once you have a release, and assuming you have an account there, just go to https://www.djangopackages.com/packages/add/ and add it there.


Thanks
------

Thanks to `Two Scoops Academy`_ for supporting the `cookiecutter`_ project and promoting Django best practices.

.. image:: https://s3.amazonaws.com/tsacademy/images/tsa-logo-250x60-transparent-01.png
   :name: Two Scoops Academy
   :align: center
   :alt: Two Scoops Academy
   :target: http://www.twoscoops.academy/


Follows Best Practices
~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png
   :name: Two Scoops Logo
   :align: center
   :alt: Two Scoops of Django
   :target: http://twoscoopspress.org/products/two-scoops-of-django-1-8

This project follows best practices as espoused in `Two Scoops of Django: Best Practices for Django 1.8`_.


.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage
.. _djangocms-helper: https://github.com/nephila/djangocms-helper
.. _Two Scoops Academy: http://www.twoscoops.academy/
.. _`Two Scoops of Django: Best Practices for Django 1.8`: http://twoscoopspress.org/products/two-scoops-of-django-1-8
