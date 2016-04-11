from django.db import models
from django.core.exceptions import ValidationError

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

# studio configuration

class Configuration(models.Model):
    station_name = models.CharField(max_length=1024)

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

# sources

class Source(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

