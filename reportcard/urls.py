
from django.conf.urls import patterns, url

urlpatterns = patterns('reportcard.views',
    url(r'^([\w-]+)/([0-9]+)/$', 'student_reportcard',
        name='student-reportcard'),
)
