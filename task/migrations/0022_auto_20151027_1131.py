# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0021_auto_20151027_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomment',
            name='docfile',
            field=models.FileField(upload_to=b'attachment/%Y-%m-%d'),
        ),
    ]
