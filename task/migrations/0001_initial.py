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
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name=b'Apellido')),
                ('address', models.CharField(max_length=50, verbose_name=b'Direccion')),
                ('telephone', models.IntegerField(verbose_name=b'Telefono')),
                ('mail', models.EmailField(max_length=254, verbose_name=b'Mail')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Titulo de la tarea')),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('turnover_code', models.CharField(max_length=50, verbose_name=b'Codigo en Turnover')),
                ('priority', models.IntegerField(verbose_name=b'Prioridad')),
                ('urgency', models.IntegerField(verbose_name=b'Urgencia')),
                ('start_date', models.DateField(null=True, verbose_name=b'Fecha de Inicio', blank=True)),
                ('finish_date', models.DateField(null=True, verbose_name=b'Fecha Comprometida', blank=True)),
                ('estimation_hours', models.IntegerField(verbose_name=b'Horas Estimada')),
                ('description', models.CharField(max_length=255, verbose_name=b'Descripcion')),
                ('sar', models.IntegerField(default=0, verbose_name=b'Incidente')),
                ('done', models.BooleanField(default=0, verbose_name=b'Completado')),
                ('clientId', models.ForeignKey(verbose_name=b'Cliente', to='task.Client')),
                ('userId', models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
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
