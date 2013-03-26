from django.conf.urls import patterns, include, url

urlpatterns = patterns('schools.views',
    url(r'^/?$', 'list_schools'),
)
