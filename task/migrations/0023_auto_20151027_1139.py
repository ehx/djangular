# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0022_auto_20151027_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomment',
            name='docfile',
            field=models.FileField(null=True, upload_to=b'attachment/%Y-%m-%d'),
        ),
    ]
