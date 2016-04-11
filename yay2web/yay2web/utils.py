from django.http import HttpRequest
from studio.models import Configuration

def context_processor(HttpRequest):
    rv = {}

    config = Configuration.objects.get()

    rv['station_name'] = config.station_name

    return rv
