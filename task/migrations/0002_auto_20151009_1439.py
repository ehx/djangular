# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('address', models.CharField(max_length=50, verbose_name=b'Direccion')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='organizationId',
            field=models.ForeignKey(default=1, verbose_name=b'Organizacion', to='task.Organization'),
            preserve_default=False,
        ),
    ]
