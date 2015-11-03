# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0019_taskcomment_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomment',
            name='docfile',
            field=models.FileField(upload_to=b'attachment/%Y-%m-%d'),
        ),
    ]
