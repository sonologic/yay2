# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0012_auto_20160411_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcefallbacksource',
            name='track_sensitive',
        ),
        migrations.AddField(
            model_name='sourcefallback',
            name='track_sensitive',
            field=models.BooleanField(default=False),
        ),
    ]
