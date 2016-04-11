from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'yay2web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^studio/', include('studio.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
