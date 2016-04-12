# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0005_logfileentry_logfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('pid', models.IntegerField()),
                ('logfile', models.ForeignKey(to='studio.Logfile')),
            ],
        ),
    ]
