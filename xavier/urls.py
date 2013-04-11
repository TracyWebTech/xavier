from django.conf.urls import patterns, include, url
from django.contrib import admin

from xavier.views import HomePageView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^classes/', include('classes.urls')),
    url(r'^periods/', include('periods.urls')),
    url(r'^$', HomePageView.as_view(), name='homepage'),
)
