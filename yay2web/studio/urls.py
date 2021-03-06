from django.conf.urls import url

from . import views

urlpatterns = [
    # html views:
    url(r'^$', views.index, name='dashboard'),
    url(r'^login/?$', views.log_in, name='login'),
    url(r'^sources/?$', views.sources, name='sources'),
    url(r'^source/alsa/(-?[0-9]+)/?$', views.source_alsa, name='source_alsa'),
    url(r'^sink/icecast/([0-9]+)/?$', views.sink_icecast, name='sink_icecast'),
    url(r'^sinks/?$', views.sinks, name='sinks'),
    url(r'^processes/?$', views.processes, name='processes'),
    url(r'^logfiles/?$', views.logfiles, name='logfiles'),
    url(r'^logfile/([0-9]+)/?$', views.logfile, name='logfile'),
    url(r'^terminate/([0-9]+)/?$', views.terminate, name='terminate'),
    url(r'^start/([0-9]+)/?$', views.start, name='start'),
    # json views:
    url(r'^status/?$', views.status, name='status'),
    url(r'^cards/?$', views.cards, name='cards'),
    url(r'^pcms(/capture|/playback)?/?$', views.pcms, name='pcms'),
    url(r'^liquidsoap/?$', views.liquidsoap, name='liquidsoap'),
    url(r'^logentries/([0-9]+)/(-?[0-9]+)/?$', views.logentries, name='logentries'),
]

