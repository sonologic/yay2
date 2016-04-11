# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0004_configuration_telnet_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='log_path',
            field=models.CharField(default=b'/tmp', max_length=b'2048'),
        ),
    ]
