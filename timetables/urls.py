from django.conf.urls import patterns, url

from timetables import views


urlpatterns = patterns('',
    url(r'^$', views.SchoolTimetableList.as_view(), name='school_timetables'),
    url(r'^edit_timetable/(?P<timetable_slug>[-\w]+)$',
            views.EditTimetable.as_view(), name='edit_timetable'),
    url(r'^add_timetable$', views.AddTimetable.as_view(),
            name='add_timetable'),
    url(r'^update_times$', views.UpdateTimes.as_view(), name='update_times'),
)
