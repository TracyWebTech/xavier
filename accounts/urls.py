# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from .views import students_views, teachers_views, employees_views


urlpatterns = patterns('',
    url(r'^students/', include(students_views.urls)),
    url(r'^teachers/', include(teachers_views.urls)),
    url(r'^employees/', include(employees_views.urls)),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
)
