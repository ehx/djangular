# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_auto_20151026_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='tag',
            field=models.CharField(default=1, max_length=50, verbose_name=b'Nombre corto'),
            preserve_default=False,
        ),
    ]
