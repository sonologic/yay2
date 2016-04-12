# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_squashed_0015_configuration_playlist_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='cmd_path',
            field=models.CharField(default=b'/home/yay2/run', max_length=b'2048'),
        ),
    ]
