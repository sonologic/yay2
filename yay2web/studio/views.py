from time import time
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import json
import alsaaudio

from django.contrib.auth.decorators import login_required

# html views

@login_required
def index(request):
    context = RequestContext(request, {
    })
    return render(request, 'studio/dashboard.html', context)

def sinks(request):
    context = RequestContext(request, {
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


