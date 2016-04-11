from django.contrib import admin

from .models import Configuration, SinkIcecast, SourceAlsa

admin.site.register(Configuration)
admin.site.register(SinkIcecast)
admin.site.register(SourceAlsa)

