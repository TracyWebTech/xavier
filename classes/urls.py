from django.conf.urls import include, patterns, url

from classes import views


urlpatterns = patterns('',
    url(r'^class/$', views.class_list, name='class-list'),
    url(r'^class/add/$', views.class_create, name='class-create'),
    url(r'^class/(?P<pk>\d+)/$', views.class_detail, name='class-detail'),
    url(r'^class/(?P<pk>\d+)/edit/$', views.class_update, name='class-update'),
    url(r'^class/(?P<pk>\d+)/delete/$', views.class_delete, name='class-delete'),
)
