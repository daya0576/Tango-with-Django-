# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='category',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
