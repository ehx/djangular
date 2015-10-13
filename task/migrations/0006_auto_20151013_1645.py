# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20151013_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='clientId',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='taskcomments',
            old_name='taskId',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='taskcomments',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='taskuser',
            old_name='taskId',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='taskuser',
            old_name='userId',
            new_name='user',
        ),
    ]
