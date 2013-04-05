from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^(?P<school_slug>[-\w]+)/scores/', include('scores.urls')),
)


