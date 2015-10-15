# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20151014_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(default=0, verbose_name=b'Tarea', to='task.Task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='user',
            field=models.ForeignKey(default=0, verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
