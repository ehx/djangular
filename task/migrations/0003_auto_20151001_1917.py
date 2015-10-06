# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20150928_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
