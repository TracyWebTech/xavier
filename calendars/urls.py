from django.conf.urls import include, patterns, url

from calendars import views


urlpatterns = patterns('',
    url(r'^$', views.Calendar.as_view(), name='calendar'),
    url(r'^toggle-break/$', views.ajax_toggle_break),
)
