# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notificationId',
        ),
        migrations.AddField(
            model_name='notification',
            name='notification',
            field=models.IntegerField(default=1, verbose_name=b'Notification'),
            preserve_default=False,
        ),
    ]
