# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
)
