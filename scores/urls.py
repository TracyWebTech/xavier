from django.conf.urls import patterns, include, url

urlpatterns = patterns('scores.views',
    url(r'^$', 'classes_list', name='classes_list'),
    url(r'^(?P<year>\d{4})/(?P<subject_slug>[-\w]+)/(?P<class_slug>[-\w]+)/$',
        'scores_list', name='scores_list'),
    url(r'^get_score$', 'get_score', name='get_score'),
)
