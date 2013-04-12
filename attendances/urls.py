from django.conf.urls import include, patterns, url

from .views import attendancebook_views


urlpatterns = patterns('',
    url(r'^attendancebook/', include(attendancebook_views.urls)),
)
