# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0011_auto_20160411_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcealsa',
            name='strip_blank',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sourcefallback',
            name='strip_blank',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
