from django.conf.urls import include, patterns, url

from periods import views


urlpatterns = patterns('',
    url(r'^period/$', views.period_list, name='period-list'),
    url(r'^period/add/$', views.period_create, name='period-create'),
    url(r'^period/(?P<pk>\d+)/$', views.period_detail, name='period-detail'),
    url(r'^period/(?P<pk>\d+)/edit/$', views.period_update, name='period-update'),
    url(r'^period/(?P<pk>\d+)/delete/$', views.period_delete, name='period-delete'),
)
