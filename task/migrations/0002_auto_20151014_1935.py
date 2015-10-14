# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(verbose_name=b'Tarea', blank=True, to='task.Task', null=True),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usuario', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
