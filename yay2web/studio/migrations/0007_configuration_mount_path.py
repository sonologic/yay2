# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0006_sourcealsa_strip_blank'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='mount_path',
            field=models.CharField(default=b'/mnt', max_length=b'2048'),
        ),
    ]
