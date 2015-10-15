# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20151015_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 15, 17, 55, 42, 747705, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
