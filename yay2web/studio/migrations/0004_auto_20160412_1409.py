# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0003_logfile_logfileentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logfile',
            name='name',
            field=models.CharField(unique=True, max_length=1024),
        ),
    ]
