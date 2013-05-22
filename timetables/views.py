import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View, TemplateView
from django.utils.translation import ugettext

from classes.models import Class, ClassSubject
from schools.models import School
from subjects.models import Subject
from timetables import models

def get_timetables():
    return models.Timetable.objects.filter(school=School.objects.get_current())

class SchoolTimetableList(TemplateView):
    template_name = 'timetables/timetable_list.html'

    def get_context_data(self, **kwargs):
        context = super(SchoolTimetableList, self).get_context_data(**kwargs)
        context['timetables'] = models.Timetable.objects.all()
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
        timetable_pk = context['timetable_pk']
        context['timetable'] = models.Timetable.objects.get(pk=timetable_pk)
        context['times'] = models.Time.objects.filter(
                timetable=context['timetable']).order_by('start')
        context['title'] = ugettext('Timetables')
        return context

class RemoveTimetable(View):

    def post(self, request, *args, **kwargs):
        timetable_pk = request.POST.get('timetable_pk', None)
        if not timetable_pk:
            return HttpResponseBadRequest()
        models.Timetable.objects.get(pk=timetable_pk).delete()
        return HttpResponse()

class UpdateTimes(View):

    def post(self, request, *args, **kwargs):
        start = request.POST.get('start', None)
        end = request.POST.get('end', None)
        timetable_pk = request.POST.get('timetable_pk', None)
        time_pk = request.POST.get('time_combination_pk', None)
        if time_pk:
            if not start and not end and not timetable_pk:
                models.Time.objects.get(pk=time_pk).delete()
                return HttpResponse()
            time = get_object_or_404(models.Time, pk=time_pk)
            time.start = start
            time.end = end
            time.save()
            return HttpResponse()

        if timetable_pk and start and end:
            timetable = models.Timetable.objects.get(pk=timetable_pk)
            time = models.Time.objects.create(start=start, end=end,
                                       timetable=timetable)
            return HttpResponse(json.dumps(time.pk), mimetype="application/json")
        return HttpResponse()

class UpdateTimetable(View):

    def post(self, request, *args, **kwargs):
        timetable_name = request.POST.get('timetable_name', None)
        timetable_pk = request.POST.get('timetable_pk', None)
        if not timetable_name:
            return HttpResponseBadRequest()
        if timetable_pk:
            timetable = models.Timetable.objects.get(pk=timetable_pk)
            timetable.name = timetable_name
            timetable.save()
            return HttpResponse()
        school = School.objects.get_current()
        timetable = models.Timetable.objects.create(school=school,
                                             name=timetable_name)

        data = {'slug': timetable.slug, 'pk': timetable.pk}
        return HttpResponse(json.dumps(data), mimetype="application/json")


class ListClasses(TemplateView):
    template_name = 'timetables/timetable_class_listing.html'

    def get_context_data(self, **kwargs):
        context = super(ListClasses, self).get_context_data(**kwargs)
        context['title'] = ugettext('Class Timetables')
        return context

class ClassTimetable(TemplateView):
    template_name = 'timetables/class_timetable.html'

    def get_context_data(self, **kwargs):
        context = super(ClassTimetable, self).get_context_data(**kwargs)
        context['class'] = Class.objects.get(slug=context['class_slug'])
        context['days'] = models.ClassSubjectTime.WEEKDAY_CHOICES

        context['timetables_exist'] = False
        if models.Timetable.objects.exists():
            context['timetables_exist'] = True

        context['timetable_list'] = ''
        context['timetable_pk'] = ''
        context['block_timetable_change'] = False
        times = ''
        try:
            classtimetable = models.ClassTimetable.objects.get(
                    classroom__slug=context['class_slug'])
            context['timetable_pk'] = classtimetable.timetable.pk
        except models.ClassTimetable.DoesNotExist:
            # TODO Set a default timetable somewhere to be used when the
            # class doesn't have a timetable specified
            # TODO if there is timetables available, list them and send
            # a warning that there is no timetable linked to this class yet
            context['timetable_list'] = get_timetables()
        else:
            times = models.Time.objects.filter(
                    timetable=classtimetable.timetable)

            cst = models.ClassSubjectTime.objects.filter(
                class_subject__classroom=classtimetable.classroom
            )
            if cst.exists():
                context['block_timetable_change'] = True

        # TODO: deploy a method on models to get the timetable
        context['timetable_list'] = get_timetables()
        day_time_subject = []
        for time in times:
            time_dict = {
                'time': time,
                'subjects': []
            }
            for day_abbr, day in models.ClassSubjectTime.WEEKDAY_CHOICES:
                try:
                    class_subject_time = time.classsubjecttime_set.get(
                            class_subject__classroom=context['class'],
                            weekday=day_abbr)
                except models.ClassSubjectTime.DoesNotExist:
                    subject = (None, day_abbr, None)
                else:
                    subject = (class_subject_time.pk, day_abbr, day,
                               class_subject_time.class_subject.subject,
                               class_subject_time.class_subject.teacher)

                time_dict['subjects'].append(subject)
            day_time_subject.append(time_dict)

        context['times'] = day_time_subject
        context['title'] = ugettext('Timetable')
        context['subtitle'] = unicode(context['class'])
        return context


class UpdateClassSubjectTime(View):

    def post(self, request, *args, **kwargs):
        classroom_pk = request.POST.get('class', None)
        subject_pk = request.POST.get('subject_pk', None)
        time_pk = request.POST.get('time', None)
        weekday_abbr = request.POST.get('weekday', None)
        class_subject_time_pk = request.POST.get('class_subject_time_pk', None)
        if not classroom_pk or not subject_pk or not time_pk \
                or not weekday_abbr:
            return HttpResponseNotFound()
        classroom = Class.objects.get(pk=classroom_pk)
        time = models.Time.objects.get(pk=time_pk)
        subject = Subject.objects.get(pk=subject_pk)
        class_subject = ClassSubject.objects.get(classroom=classroom,
                                                 subject=subject)
        if not class_subject:
            return HttpResponseNotFound()

        # TODO return and set the class_subject_time_pk in the html
        if class_subject_time_pk:
            class_subject_time = models.ClassSubjectTime.objects.get(
                    pk=class_subject_time_pk)
            class_subject_time.class_subject = class_subject
            class_subject_time.save()
            return HttpResponse(json.dumps(class_subject_time.pk),
                                mimetype="application/json")

        class_subject_time, created = models.ClassSubjectTime.objects.get_or_create(
                    weekday=weekday_abbr, time=time,
                    class_subject__classroom=class_subject.classroom,
                    defaults={'class_subject': class_subject})
        if not created:
            class_subject_time.class_subject = class_subject
            class_subject_time.save()
        return HttpResponse()

class ApplyClassTimetable(View):

    def post(self, request, *args, **kwargs):
        classroom_pk = request.POST.get('class_pk', None)
        timetable_pk = request.POST.get('timetable_pk', None)
        classtimetable, created = models.ClassTimetable.objects.get_or_create(
                classroom_id=classroom_pk,
                defaults={'timetable_id': timetable_pk})
        if not created:
            classtimetable.timetable_id = timetable_pk
            classtimetable.save()
        return HttpResponse()

class LinkClassTimetableList(TemplateView):
    template_name = 'timetables/choose_timetable_list.html'

    def get_context_data(self, **kwargs):
        context = super(LinkClassTimetableList,
                        self).get_context_data(**kwargs)
        context['class'] = Class.objects.get(slug=context['class_slug'])
        context['timetable_list'] = get_timetables()
        context['title'] = ugettext("Timetable")
        context['subtitle'] = context['class']
        context['class_timetable_url'] = reverse('class_timetable',
                kwargs={'class_slug': context['class_slug']})
        return context
