from django.conf.urls import patterns, url

from timetables import views


urlpatterns = patterns('',
    url(r'^$', views.SchoolTimetableList.as_view(), name='school_timetables'),
    url(r'^edit/(?P<timetable_pk>[\d]+)$',
            views.EditTimetable.as_view(), name='edit_timetable'),
    url(r'^add/$', views.AddTimetable.as_view(), name='add_timetable'),
    url(r'^remove/$', views.RemoveTimetable.as_view(), name='remove_timetable'),
    url(r'^update_times/$', views.UpdateTimes.as_view(), name='update_times'),
    url(r'^update_class_subject_time/$', views.UpdateClassSubjectTime.as_view(),
            name='update_class_subject_time'),
    url(r'^update_timetable/$', views.UpdateTimetable.as_view(),
            name='update_timetable'),

    url(r'^classes/$', views.ListClasses.as_view(),
            name='list_classes_for_timetables'),
    url(r'^classes/(?P<class_slug>[-\w]+)/$',
            views.ClassTimetableView.as_view(),
            name='class_timetable'),
    url(r'^classes/(?P<class_slug>[-\w]+)/link_classtimetable_list/$',
            views.LinkClassTimetableList.as_view(),
            name='link_classtimetable_list'),
    url(r'^apply_classtimetable/', views.ApplyClassTimetable.as_view(),
            name='apply_classtimetable'),
)
