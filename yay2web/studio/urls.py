from django.conf.urls import url

from . import views

urlpatterns = [
    # html views:
    url(r'^/?$', views.index, name='dashboard'),
    url(r'^sources/?$', views.sources, name='sources'),
    url(r'^source/alsa/([0-9]+)/?$', views.source_alsa, name='source_alsa'),
    url(r'^sinks/?$', views.sinks, name='sinks'),
    # json views:
    url(r'^status/?$', views.status, name='status'),
    url(r'^cards/?$', views.cards, name='cards'),
    url(r'^pcms/?$', views.pcms, name='pcms'),
    url(r'^liquidsoap/?$', views.liquidsoap, name='liquidsoap'),
]

