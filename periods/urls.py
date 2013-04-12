from django.conf.urls import include, patterns, url

from .views import period_views


urlpatterns = patterns('',
    url(r'^period/', include(period_views.urls)),
)
