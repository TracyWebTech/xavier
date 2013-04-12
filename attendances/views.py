# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404
from django.utils.text import capfirst
from django.utils.translation import ugettext as _


from classes.models import Class
from xavier.views import ModelView

from .models import AttendanceBook


class AttendanceBookView(ModelView):
    base_template = 'attendances/base.html'
    paginate_by = 20

    def get_class_rooms(self, request):
        return Class.objects.filter(
            period__school=self.get_current_school(request)
        )

    def get_query_set(self, request, *args, **kwargs):
        # Filter items only from current school
        qs = super(ModelView, self).get_query_set(request, *args, **kwargs)
        return qs.filter(classroom__period__school=self.get_current_school(request))

    def additional_urls(self):
        return [
            (r'^take-attendance/(?P<classroom>\d+)/$', self.take_attendance),
        ]

    def take_attendance(self, request, classroom):
        if not self.adding_allowed(request):
            return self.response_adding_denied(request)

        object = get_object_or_404(Class, pk=classroom)
        context = {
            'title': _('Take attendance for class %s' % object.identification),
            'object': object,
        }
        return self.render(
            request,
            'attendances/take_attendance.html',
            self.get_context(request, context)
        )

    def list_view(self, request, *args, **kwargs):
        context = dict(class_rooms=self.get_class_rooms(request))
        return self.render_list(request, context)

attendancebook_views = AttendanceBookView(AttendanceBook)
