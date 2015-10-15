# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 15, 20, 4, 12, 500791, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=0, verbose_name=b'Completado'),
        ),
    ]
