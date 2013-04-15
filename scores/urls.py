
from django.conf.urls import patterns, include, url

urlpatterns = patterns('scores.views',
    url(r'(?P<year>\d{4})/(?P<class_subject_slug>[-\w]+)/?$',
        'list', name='scores_list'),
    url(r'get_score', 'get_score', name='get_score')
)
