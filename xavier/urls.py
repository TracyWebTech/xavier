from django.conf.urls import patterns, include, url
from django.contrib import admin

from xavier.api import v1_api
from xavier.views import HomePageView


# TODO: Find a better place to put the lines below
from django.template.loader import add_to_builtins
add_to_builtins('django.templatetags.i18n')


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^classes/', include('classes.urls')),
    url(r'^periods/', include('periods.urls')),
    url(r'^scores/', include('scores.urls')),
    url(r'^attendances/', include('attendances.urls')),
    url(r'^$', HomePageView.as_view(), name='homepage'),
)
