# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0010_sourcefallback_sourcefallbacksource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcealsa',
            name='strip_blank',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sourcefallback',
            name='strip_blank',
            field=models.FloatField(null=True),
        ),
    ]
