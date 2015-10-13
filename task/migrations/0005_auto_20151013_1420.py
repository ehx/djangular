# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_taskcomments_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomments',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 14, 20, 43, 587836, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
