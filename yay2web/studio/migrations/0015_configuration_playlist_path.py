# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0014_sinkicecast_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='playlist_path',
            field=models.CharField(default=b'/home/yay2/playlists', max_length=b'2048'),
        ),
    ]
