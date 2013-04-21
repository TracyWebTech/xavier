# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from accounts import models, views

urlpatterns = patterns('',
    # Students
    url(r'^student/$', views.student_list, name='student-list'),
    url(r'^student/add/$', views.student_create, name='student-create'),
    url(r'^student/(?P<pk>\d+)/$', views.student_detail, name='student-detail'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.student_update, name='student-update'),
    url(r'^student/(?P<pk>\d+)/delete/$', views.student_delete, name='student-delete'),

    # Teachers
    url(r'^teacher/$', views.teacher_list, name='teacher-list'),
    url(r'^teacher/add/$', views.teacher_create, name='teacher-create'),
    url(r'^teacher/(?P<pk>\d+)/$', views.teacher_detail, name='teacher-detail'),
    url(r'^teacher/(?P<pk>\d+)/edit/$', views.teacher_update, name='teacher-update'),
    url(r'^teacher/(?P<pk>\d+)/delete/$', views.teacher_delete, name='teacher-delete'),

    # Employees
    url(r'^employee/$', views.employee_list, name='employee-list'),
    url(r'^employee/add/$', views.employee_create, name='employee-create'),
    url(r'^employee/(?P<pk>\d+)/$', views.employee_detail, name='employee-detail'),
    url(r'^employee/(?P<pk>\d+)/edit/$', views.employee_update, name='employee-update'),
    url(r'^employee/(?P<pk>\d+)/delete/$', views.employee_delete, name='employee-delete'),

    # General accounts
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
)
