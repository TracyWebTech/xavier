from django.conf.urls import include, patterns, url

from attendances import views


urlpatterns = patterns(
    '',
    url(r'^$', views.Index.as_view(), name='attendances-index'),
    url(r'^(?P<classroom_slug>[-\w]+)/$', views.ClassAttendances.as_view(), name='attendances-class'),
    url(r'^(?P<classroom_slug>[-\w]+)/(?P<student>\d+)/change-status/$', views.ajax_attendance_change_status),
    url(r'^(?P<classroom_slug>[-\w]+)/(?P<student>\d+)/set-explanation/$', views.ajax_attendance_set_explanation),
)
