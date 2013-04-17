from django.conf.urls import patterns, include, url

urlpatterns = patterns('scores.views',
    url(r'^(?P<year>\d{4})/(?P<class_slug>[-\w]+)/(?P<subject_slug>[-\w]+)/$',
    url(r'^$', 'classes_list', name='classes_list'),
        'scores_list', name='scores_list'),
    url(r'^get_score$', 'get_score', name='get_score'),
    url(r'^get_subjects', 'get_subjects', name='get_subjects'),
)
