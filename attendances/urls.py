from django.conf.urls import include, patterns, url

from attendances import views


urlpatterns = patterns(
    '',
    url(r'^attendancebook/$', views.attendancebook_list, name='attendancebook-list'),
    url(r'^attendancebook/add/$', views.attendancebook_create, name='attendancebook-create'),
    url(r'^attendancebook/(?P<pk>\d+)/$', views.attendancebook_detail, name='attendancebook-detail'),
    url(r'^attendancebook/(?P<pk>\d+)/edit/$', views.attendancebook_update, name='attendancebook-update'),
    url(r'^attendancebook/(?P<pk>\d+)/delete/$', views.attendancebook_delete, name='attendancebook-delete'),

    url(r'^take-attendance/(?P<classroom>\d+)/$', views.takeattendance, name='takeattendance'),
    url(r'^take-attendance/(?P<classroom>\d+)/(?P<student>\d+)/change-status/$', views.ajax_attendance_change_status),
    url(r'^take-attendance/(?P<classroom>\d+)/(?P<student>\d+)/set-explanation/$', views.ajax_attendance_set_explanation),
)
