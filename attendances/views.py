# -*- coding: utf-8 -*-

from datetime import date

from django import http
from django.core import exceptions
from django.views import generic
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext

from xavier import views
from accounts.models import Student
from attendances import models
from classes.models import Class


def get_attendance_book(classroom, day):
    if not isinstance(day, date):
        year, month, month_day = day.split('-')
        day = date(int(year), int(month), int(month_day))
    if not isinstance(classroom, Class):
        classroom = Class.objects.get(pk=classroom)
    attendance_book, _ = models.AttendanceBook.objects.get_or_create(
        classroom=classroom,
        day=day,
    )
    return attendance_book


class Index(generic.TemplateView):
    template_name = 'attendances/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update({
            'title': ugettext('Attendances'),
            'classroom_list': Class.on_school.all()
        })
        return context


class ClassAttendances(generic.TemplateView):
    template_name = 'attendances/class.html'

    def get_context_data(self, **kwargs):
        context = super(ClassAttendances, self).get_context_data(**kwargs)
        classroom = get_object_or_404(Class, pk=kwargs['classroom'])
        day = self.request.GET.get('day', date.today())
        attendance_book = get_attendance_book(classroom, day)
        context.update({
            'title': ugettext('Attendances'),
            'subtitle': unicode(classroom),
            'classroom': classroom,
            'attendance_book': attendance_book
        })
        return context


def ajax_attendance_change_status(request, classroom, student):
    if request.is_ajax():
        try:
            student = Student.objects.get(pk=student)
            day = request.GET.get('day', date.today())
            status = request.GET.get('status')
            attendance_book = get_attendance_book(classroom, day)
        except ValueError:
            return http.HttpResponse(status=400)
        except exceptions.ObjectDoesNotExist:
            return http.HttpResponse(status=400)
        attendance, created = models.Attendance.objects.get_or_create(
            attendance_book=attendance_book,
            student=student,
            defaults={'status': status}
        )
        if not created:
            attendance.status = status
            attendance.save()
        return http.HttpResponse(status=200)
    return http.HttpResponse(status=400)


def ajax_attendance_set_explanation(request, classroom, student):
    if request.is_ajax():
        try:
            student = Student.objects.get(pk=student)
            day = request.GET.get('day', date.today())
            explanation = request.GET.get('explanation', '')
            attendance_book = get_attendance_book(classroom, day)
        except ValueError:
            return http.HttpResponse(status=400)
        except exceptions.ObjectDoesNotExist:
            return http.HttpResponse(status=400)
        attendance, created = models.Attendance.objects.get_or_create(
            attendance_book=attendance_book,
            student=student,
            defaults={'status': 'absent', 'explanation': explanation}
        )
        if not created:
            attendance.explanation = explanation
            attendance.save()
        return http.HttpResponse(status=200)
    return http.HttpResponse(status=400)
