from django.conf import settings
from django.conf.urls.defaults import patterns, include, \
    url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    # just for testing - native way to sampleapp urls 
    # (r'^sampleapp-native/', include('sampleapp.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)
