from django.conf.urls import include, patterns, url

from classes import views


urlpatterns = patterns('',
    # Class model
    url(r'^class/$', views.ClassList.as_view(), name='class-list'),
    url(r'^class/add/$', views.ClassCreate.as_view(), name='class-create'),
    url(r'^class/(?P<pk>\d+)/$', views.ClassDetail.as_view(), name='class-detail'),
    url(r'^class/(?P<pk>\d+)/edit/$', views.ClassUpdate.as_view(), name='class-update'),
    url(r'^class/(?P<pk>\d+)/delete/$', views.ClassDelete.as_view(), name='class-delete'),
)
