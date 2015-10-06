# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'titulo')),
                ('description', models.CharField(max_length=255, verbose_name=b'descripcion')),
                ('done', models.IntegerField(default=0, verbose_name=b'completado')),
                ('creation_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskId', models.ForeignKey(to='task.Task')),
                ('userId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
