# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0007_configuration_mount_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('local_path', models.CharField(max_length=2048)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
