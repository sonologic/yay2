# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SinkIcecast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('server', models.CharField(max_length=1024)),
                ('port', models.PositiveIntegerField(default=8080)),
                ('mount', models.CharField(max_length=1024)),
                ('username', models.CharField(max_length=1024)),
                ('password', models.CharField(max_length=1024, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
