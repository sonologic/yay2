# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0008_localmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='localmedia',
            name='rescan',
            field=models.BooleanField(default=True),
        ),
    ]
