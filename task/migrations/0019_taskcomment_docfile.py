# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0018_remove_task_short_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcomment',
            name='docfile',
            field=models.FileField(default=1, upload_to=b'documents/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
