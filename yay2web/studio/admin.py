from django.contrib import admin

from .models import Configuration, SinkIcecast, SourceAlsa, SourceFallback, SourceFallbackSource

class SourceAlsaAdmin(admin.ModelAdmin):
    list_display = ('name','alsa_device','strip_blank')

class SinkIcecastAdmin(admin.ModelAdmin):
    list_display = ('name','server','port', 'mount', 'source')

class SourceFallbackAdmin(admin.ModelAdmin):
    list_display = ('name','name')

class SourceFallbackSourceAdmin(admin.ModelAdmin):
    list_display = ('fallback','order','name')

admin.site.register(Configuration)
admin.site.register(SinkIcecast, SinkIcecastAdmin)
admin.site.register(SourceAlsa, SourceAlsaAdmin)
admin.site.register(SourceFallback, SourceFallbackAdmin)
admin.site.register(SourceFallbackSource, SourceFallbackSourceAdmin)

