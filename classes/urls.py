from django.conf.urls import include, patterns, url

from .views import class_views


urlpatterns = patterns('',
    url(r'^', include(class_views.urls)),
)
