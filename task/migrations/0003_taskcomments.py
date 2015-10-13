# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_auto_20151009_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=500, verbose_name=b'Comentario')),
                ('taskId', models.ForeignKey(verbose_name=b'Tarea', to='task.Task')),
                ('userId', models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
