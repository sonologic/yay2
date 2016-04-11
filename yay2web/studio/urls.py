from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/?$', views.index, name='dashboard'),
    url(r'status', views.status, name='status'),
    url(r'cards', views.cards, name='cards'),
    url(r'pcms', views.pcms, name='pcms'),
]

