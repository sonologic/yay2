# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'studio', '0001_initial'), (b'studio', '0002_sinkicecast'), (b'studio', '0003_sourcealsa'), (b'studio', '0004_configuration_telnet_port'), (b'studio', '0005_configuration_log_path'), (b'studio', '0006_sourcealsa_strip_blank'), (b'studio', '0007_configuration_mount_path'), (b'studio', '0008_localmedia'), (b'studio', '0009_localmedia_rescan'), (b'studio', '0010_sourcefallback_sourcefallbacksource'), (b'studio', '0011_auto_20160411_2125'), (b'studio', '0012_auto_20160411_2126'), (b'studio', '0013_auto_20160411_2136'), (b'studio', '0014_sinkicecast_source'), (b'studio', '0015_configuration_playlist_path')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('station_name', models.CharField(max_length=1024)),
                ('telnet_port', models.IntegerField(default=1236)),
                ('log_path', models.CharField(default=b'/tmp', max_length=b'2048')),
                ('mount_path', models.CharField(default=b'/mnt', max_length=b'2048')),
                ('playlist_path', models.CharField(default=b'/home/yay2/playlists', max_length=b'2048')),
            ],
        ),
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
                ('source', models.CharField(default=b'sine', max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SourceAlsa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('alsa_device', models.CharField(max_length=1024)),
                ('strip_blank', models.FloatField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocalMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('local_path', models.CharField(max_length=2048)),
                ('rescan', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
                ('fallback', models.ForeignKey(to='studio.SourceFallback')),
            ],
        ),
        migrations.AlterField(
            model_name='sourcefallback',
            name='strip_blank',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sourcefallback',
            name='strip_blank',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sourcefallback',
            name='track_sensitive',
            field=models.BooleanField(default=False),
        ),
    ]
