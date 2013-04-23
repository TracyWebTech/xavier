from django.conf.urls import patterns, include, url

urlpatterns = patterns('scores.views',
    url(r'^$', 'classes_list', name='classes_list'),
    url(r'^(?P<class_slug>[-\w]+)/(?P<subject_slug>[-\w]+)/$', 'scores_list', name='scores_list'),
    url(r'^get_score$', 'get_score', name='get_score'),
)
