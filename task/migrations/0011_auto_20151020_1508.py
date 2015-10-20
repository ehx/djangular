# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20151020_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='organizationId',
            new_name='organization',
        ),
    ]
