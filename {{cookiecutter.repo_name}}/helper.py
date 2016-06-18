#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from tempfile import mkdtemp

HELPER_SETTINGS = dict(
    INSTALLED_APPS=[
    ],
    FILE_UPLOAD_TEMP_DIR=mkdtemp(),
)


def run():
    from djangocms_helper import runner
    runner.run('{{ cookiecutter.app_name }}')


def setup():
    import sys
    from djangocms_helper import runner
    runner.setup('{{ cookiecutter.app_name }}', sys.modules[__name__], use_cms=False)

if __name__ == "__main__":
    run()
