# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0017_task_short_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='short_text',
        ),
    ]
