# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_auto_20151023_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.ForeignKey(verbose_name=b'Tarea', to='task.Task', null=True),
        ),
    ]
