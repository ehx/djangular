# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_auto_20151026_1025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Modules',
            new_name='Module',
        ),
    ]
