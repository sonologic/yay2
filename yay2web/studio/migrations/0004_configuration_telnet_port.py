# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0003_sourcealsa'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='telnet_port',
            field=models.IntegerField(default=1236),
        ),
    ]
