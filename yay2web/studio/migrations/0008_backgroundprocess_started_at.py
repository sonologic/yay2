# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0007_auto_20160412_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundprocess',
            name='started_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
