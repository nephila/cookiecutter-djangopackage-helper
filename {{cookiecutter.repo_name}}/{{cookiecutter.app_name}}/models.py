# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
{% if cookiecutter.models != "Comma-separated list of models" %}
from django.db import models

from model_utils.models import TimeStampedModel

{% for model in cookiecutter.models.split(',') %}
class {{ model.strip() }}(TimeStampedModel):
    pass

{% endfor %}
{% endif %}
