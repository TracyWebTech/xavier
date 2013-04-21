# -*- coding: utf-8 -*-

from datetime import date

from django import http
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
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


class AttendanceBookList(views.ListView):
    base_template = 'attendances/base.html'
    model = models.AttendanceBook

    def get_classroom_list(self):
        return Class.on_school.all()

    def get_context_data(self, **kwargs):
        context = super(AttendanceBookList, self).get_context_data(**kwargs)
        context.update({
            'classroom_list': self.get_classroom_list(),
        })
        return context


class TakeAttendance(View):

    def get(self, request, classroom):
        classroom = get_object_or_404(Class, pk=classroom)
        day = request.GET.get('day', date.today())
        attendance_book = get_attendance_book(classroom, day)
        context = {
            'title': ugettext('Attendances'),
            'subtitle': unicode(classroom),
            'classroom': classroom,
            'attendance_book': attendance_book
        }
        return render_to_response(
            template_name='attendances/take_attendance.html',
            dictionary=context,
            context_instance=RequestContext(request)
        )


def ajax_attendance_change_status(request, classroom, student):
    if request.is_ajax():
        try:
            student = Student.objects.get(pk=student)
            day = request.GET.get('day', date.today())
            status = request.GET.get('status')
            attendance_book = get_attendance_book(classroom, day)
        except ValueError:
            return http.HttpResponse(status=400)
        except ObjectDoesNotExist:
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
        except ObjectDoesNotExist:
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


attendancebook_list = AttendanceBookList.as_view()
attendancebook_detail = views.DetailView.as_view(model=models.AttendanceBook)
attendancebook_create = views.CreateView.as_view(model=models.AttendanceBook)
attendancebook_update = views.UpdateView.as_view(model=models.AttendanceBook)
attendancebook_delete = views.DeleteView.as_view(model=models.AttendanceBook)

takeattendance = TakeAttendance.as_view()
