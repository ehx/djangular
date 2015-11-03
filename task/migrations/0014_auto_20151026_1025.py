# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_auto_20151023_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='module',
            field=models.ForeignKey(default=1, verbose_name=b'Modulo', to='task.Modules'),
            preserve_default=False,
        ),
    ]
