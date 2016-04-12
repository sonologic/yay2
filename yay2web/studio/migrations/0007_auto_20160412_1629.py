# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0006_backgroundprocess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundprocess',
            name='pid',
            field=models.IntegerField(null=True),
        ),
    ]
