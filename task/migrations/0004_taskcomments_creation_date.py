# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_taskcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcomments',
            name='creation_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
