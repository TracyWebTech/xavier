from django.conf.urls import include, patterns, url

from calendars import views


urlpatterns = patterns('',
    url(r'^$', views.Calendar.as_view(), name='calendar'),
)
