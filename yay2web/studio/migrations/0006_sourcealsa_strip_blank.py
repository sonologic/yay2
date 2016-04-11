# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0005_configuration_log_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcealsa',
            name='strip_blank',
            field=models.FloatField(default=None, null=True),
        ),
    ]
