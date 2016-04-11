# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0002_sinkicecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceAlsa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('alsa_device', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
