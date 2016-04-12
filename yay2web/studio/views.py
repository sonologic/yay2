from time import time
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import json
import alsaaudio
from .models import SourceAlsa, Configuration, SinkIcecast, SourceFallback, Logfile, LogfileEntry, BackgroundProcess
from yay2web.utils import generate_liquidsoap_config

from django.contrib.auth.decorators import login_required

# html views

@login_required
def index(request):
    context = RequestContext(request, {
    })
    return render(request, 'studio/dashboard.html', context)

@login_required
def sources(request):
    sources = []

    alsa_sources = SourceAlsa.objects.all()

    for source in alsa_sources:
        source.type = "alsa"
        source.details = source.alsa_device
        sources += [source]

    fallback_sources = SourceFallback.objects.all()

    for source in fallback_sources:
        source.type = "fallback"
        source.details = source.list_sources()
        sources += [source]

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

@login_required
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

@login_required
def logfiles(request):
    logfiles = Logfile.objects.all()
    context = RequestContext(request, {
        'logfiles' : logfiles,
    })
    return render(request, 'studio/logfiles.html', context)

def logfile(request, logfile_id):
    logfile = Logfile.objects.get(pk=logfile_id)
    context = RequestContext(request, {
        'logfile' : logfile,
    })
    return render(request, 'studio/logfile.html', context)

@login_required
def processes(request):
    processes = BackgroundProcess.objects.all()
    context = RequestContext(request, {
        'processes' : processes,
    })
    return render(request, 'studio/processes.html', context)
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

@login_required
def liquidsoap(request):
    rv  = generate_liquidsoap_config()

    return HttpResponse(rv, content_type="plain/text")

@login_required
def logentries(request, logfile_id, start_id):
    logfile = Logfile.objects.get(id=logfile_id)
    if start_id == "-1":
        temp_entries = LogfileEntry.objects.filter(logfile__exact=logfile).order_by('-id')[:100]
        entry = temp_entries[len(temp_entries)-1]
        start_id = entry.id

    entries = LogfileEntry.objects.filter(logfile__exact=logfile, id__gte=start_id).order_by('id')[:100]
    data=[]
    for entry in entries:
        data += [ {
            'datetime' : entry.date.strftime("%c"),
            'id'        : entry.id,
            'message'  : entry.message
        } ]
    return HttpResponse(json.dumps(data), content_type="application/json")