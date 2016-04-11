from time import time
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import json
import alsaaudio
from .models import SourceAlsa, Configuration, SinkIcecast
from yay2web.utils import generate_liquidsoap_config

from django.contrib.auth.decorators import login_required

# html views

@login_required
def index(request):
    context = RequestContext(request, {
    })
    return render(request, 'studio/dashboard.html', context)

def sources(request):
    sources = SourceAlsa.objects.all()

    for source in sources:
        source.type = "alsa"
        source.details = source.alsa_device

    context = RequestContext(request, {
        'sources' : sources,
    })
    return render(request, 'studio/sources.html', context)

@login_required
def source_alsa(request, source_id):
    source = SourceAlsa.objects.get(pk=source_id)

    context = RequestContext(request, {
        'source_id' : source_id,
    })
    return render(request, 'studio/source.html', context)
   
def sinks(request):
    sinks = SinkIcecast.objects.all()

    for sink in sinks:
        sink.type = "icecast"
        sink.details = sink.server + ":" + str(sink.port) + "/" + sink.mount

    context = RequestContext(request, {
        'sinks' : sinks,
    })
    return render(request, 'studio/sinks.html', context)
    
#@login_required
#def config_sink_icecast(request):
#    context = {}
#    return render(request, 'studio/config_sink.html', context)
#
#@login_required
#def config_source_alsa(request):
#    context = {}
#    return render(request, 'studio/config_sink.html', context)

# json views (todo, split to api ap)

@login_required
def status(request):
    data = {
        't' : time(),
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required
def cards(request):
    data = alsaaudio.cards()
    return HttpResponse(json.dumps(data), content_type="application/json")

@login_required
def pcms(request):
    data = alsaaudio.pcms()
    return HttpResponse(json.dumps(data), content_type="application/json")

# liquidsoap config
def liquidsoap(request):
    rv  = generate_liquidsoap_config()

    return HttpResponse(rv, content_type="plain/text")
    
