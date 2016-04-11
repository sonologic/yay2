from django.db import models
from django.core.exceptions import ValidationError
from alsaaudio import cards,pcms

# helper functions

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

# studio configuration

class Configuration(models.Model):
    station_name = models.CharField(max_length=1024)
    telnet_port = models.IntegerField(default=1236)
    log_path = models.CharField(max_length="2048",default="/tmp")
    mount_path = models.CharField(max_length="2048",default="/mnt")
    playlist_path = models.CharField(max_length="2048",default="/home/yay2/playlists")

    def clean(self):
        validate_only_one_instance(self)
            
# sinks
            
class Sink(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

class SinkIcecast(Sink):
    server = models.CharField(max_length=1024)
    port = models.PositiveIntegerField(default=8080)
    mount = models.CharField(max_length=1024)
    username = models.CharField(max_length=1024)
    password = models.CharField(max_length=1024, null=True)
    source = models.CharField(max_length=128, default="sine")

# sources

class Source(models.Model):
    name = models.CharField(max_length=128)
    strip_blank = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True

class SourceAlsa(Source):
    alsa_device = models.CharField(max_length=1024)

class SourceFallback(Source):
    track_sensitive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SourceFallbackSource(models.Model):
    fallback = models.ForeignKey(SourceFallback)
    name = models.CharField(max_length=128)
    order = models.IntegerField(default=0)

    def __str__(self):
        return "{0}: {1}, order={2}".format(
                    name,
                    str(fallback),
                    order)
    
# media

class Media(models.Model):
    name = models.CharField(max_length=1024)
    rescan = models.BooleanField(default=True)

    class Meta:
        abstract = True

class LocalMedia(Media):
    local_path = models.CharField(max_length=2048)


