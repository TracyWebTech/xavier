import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic.base import View, TemplateView
from django.utils.translation import ugettext

from schools.models import School
from subjects.models import Subject
from timetables.models import Timetable, Time


class SchoolTimetableList(TemplateView):
    template_name = 'timetables/timetable_list.html'

    def get_context_data(self, **kwargs):
        context = super(SchoolTimetableList, self).get_context_data(**kwargs)
        context['timetables'] = Timetable.objects.all()
        context['title'] = ugettext('Timetables')
        return context


class AddTimetable(TemplateView):
    template_name = 'timetables/add_timetable.html'

    def get_context_data(self, **kwargs):
        context = super(AddTimetable, self).get_context_data(**kwargs)
        context['title'] = ugettext('Timetables')
        return context


class EditTimetable(TemplateView):
    template_name = 'timetables/edit_timetable.html'

    def get_context_data(self, **kwargs):
        context = super(EditTimetable, self).get_context_data(**kwargs)
        timetable_slug = context['timetable_slug']
        context['timetable'] = Timetable.objects.get(slug=timetable_slug)
        context['subtitle'] = context['timetable'].name
        context['times'] = Time.objects.filter(timetable=context['timetable'])
        context['title'] = ugettext('Timetables')
        return context

class RemoveTimetable(View):

    def post(self, request, *args, **kwargs):
        timetable_pk = request.POST.get('timetable_pk', None)
        if not timetable_pk:
            return HttpResponseBadRequest()
        Timetable.objects.get(pk=timetable_pk).delete()
        return HttpResponse()

class UpdateTimes(View):

    def post(self, request, *args, **kwargs):
        start = request.POST.get('start', None)
        end = request.POST.get('end', None)
        timetable_slug = request.POST.get('timetable_slug', None)
        time_pk = request.POST.get('time_combination_pk', None)
        if time_pk:
            if not start and not end and not timetable_slug:
                Time.objects.get(pk=time_pk).delete()
                return HttpResponse()
            time = get_object_or_404(Time, pk=time_pk)
            time.start = start
            time.end = end
            time.save()
            return HttpResponse()

        if timetable_slug and start and end:
            timetable = Timetable.objects.get(slug=timetable_slug)
            time = Time.objects.create(start=start, end=end,
                                       timetable=timetable)
            return HttpResponse(json.dumps(time.pk), mimetype="application/json")
        return HttpResponse()

class UpdateTimetable(View):

    def post(self, request, *args, **kwargs):
        timetable_name = request.POST.get('timetable_name', None)
        if not timetable_name:
            return HttpResponseBadRequest()
        school = School.objects.get_current()
        timetable = Timetable.objects.create(school=school,
                                             name=timetable_name)
        return HttpResponse(json.dumps(timetable.slug),
                            mimetype="application/json")
