# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0013_auto_20160411_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinkicecast',
            name='source',
            field=models.CharField(default=b'sine', max_length=128),
        ),
    ]
