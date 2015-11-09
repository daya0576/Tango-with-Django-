# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20151106_1551'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cateogry',
            new_name='Category',
        ),
    ]
