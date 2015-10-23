# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20151020_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='task',
            field=models.ForeignKey(default=0, verbose_name=b'Tarea', to='task.Task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Titulo de la tarea'),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='comment',
            field=models.CharField(max_length=5000, verbose_name=b'Comentario'),
        ),
    ]
