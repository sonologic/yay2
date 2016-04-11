# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0009_localmedia_rescan'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceFallback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('strip_blank', models.FloatField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SourceFallbackSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('order', models.IntegerField(default=0)),
                ('track_sensitive', models.BooleanField(default=False)),
                ('fallback', models.ForeignKey(to='studio.SourceFallback')),
            ],
        ),
    ]
