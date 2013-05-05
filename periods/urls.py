from django.conf.urls import include, patterns, url

from periods import views


urlpatterns = patterns('periods.views',
    url(r'^period/$', 'period_list', name='period-list'),
    url(r'^period/add/$', 'period_create', name='period-create'),
    url(r'^period/(?P<pk>\d+)/$', 'period_detail', name='period-detail'),
    url(r'^period/(?P<pk>\d+)/edit/$', 'period_update', name='period-update'),
    url(r'^period/(?P<pk>\d+)/delete/$', 'period_delete', name='period-delete'),
    url(r'^subperiod/(?P<pk>\d+)/select/$', 'period_select', name='period-select'),
)
