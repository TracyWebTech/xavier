from django.conf.urls import include, patterns, url

from classes import views


urlpatterns = patterns('',
    # Class model
    url(r'^class/$', views.ClassList.as_view(), name='classes-class-list'),
    url(r'^class/add/$', views.ClassCreate.as_view(), name='classes-class-create'),
    url(r'^class/(?P<id>\d+)/$', views.ClassDetail.as_view(), name='classes-class-detail'),
    url(r'^class/(?P<id>\d+)/update/$', views.ClassUpdate.as_view(), name='classes-class-update'),
    url(r'^class/(?P<id>\d+)/delete/$', views.ClassDelete.as_view(), name='classes-class-delete'),
)
