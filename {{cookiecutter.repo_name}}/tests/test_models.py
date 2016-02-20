# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from {{ cookiecutter.app_name }} import models

from .base import Base{{ cookiecutter.app_name|capitalize }}


class Test{{ cookiecutter.app_name|capitalize }}(Base{{ cookiecutter.app_name|capitalize }}):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass
