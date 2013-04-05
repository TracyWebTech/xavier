
from django.conf.urls import patterns, include, url

urlpatterns = patterns('scores.views',
    url(r'(?P<class_slug>[-\w]+)/(?P<year>\d{4})/(?P<period_slug>[-\w]+)/?$',
        'list')
)
