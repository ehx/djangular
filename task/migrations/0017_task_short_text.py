# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0016_module_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='short_text',
            field=redactor.fields.RedactorField(default=1, verbose_name='Text'),
            preserve_default=False,
        ),
    ]
