# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0024_auto_20151027_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(verbose_name=b'Orden'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=1, verbose_name=b'Estado', to='task.Status'),
            preserve_default=False,
        ),
    ]
