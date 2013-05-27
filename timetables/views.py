import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View, TemplateView
from django.utils.translation import ugettext

from classes.models import Class, ClassSubject
from schools.models import School
from subjects.models import Subject
from timetables.models import Timetable, Time, ClassTimetable, ClassSubjectTime

def get_timetables():
    return Timetable.objects.filter(school=School.objects.get_current())

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
        timetable_pk = context['timetable_pk']
        context['timetable'] = Timetable.objects.get(pk=timetable_pk)
        context['times'] = Time.objects.filter(
                timetable=context['timetable'])
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
        timetable_pk = request.POST.get('timetable_pk', None)
        time_pk = request.POST.get('time_combination_pk', None)
        if time_pk:
            if not start and not end and not timetable_pk:
                # TODO it must verify if there is any subject using this time
                # and warn the user
                Time.objects.get(pk=time_pk).delete()
                return HttpResponse()
            time = get_object_or_404(Time, pk=time_pk)
            time.start = start
            time.end = end
            time.save()
            return HttpResponse()

        if timetable_pk and start and end:
            timetable = Timetable.objects.get(pk=timetable_pk)
            time = Time.objects.create(start=start, end=end,
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
            timetable = Timetable.objects.get(pk=timetable_pk)
            timetable.name = timetable_name
            timetable.save()
            return HttpResponse()
        school = School.objects.get_current()
        timetable = Timetable.objects.create(school=school,
                                             name=timetable_name)

        data = {'slug': timetable.slug, 'pk': timetable.pk}
        return HttpResponse(json.dumps(data), mimetype="application/json")


class ListClasses(TemplateView):
    template_name = 'timetables/timetable_class_listing.html'

    def get_context_data(self, **kwargs):
        context = super(ListClasses, self).get_context_data(**kwargs)
        context['title'] = ugettext('Class Timetables')
        return context

class ClassTimetableView(TemplateView):
    template_name = 'timetables/class_timetable.html'

    def get_context_data(self, **kwargs):
        context = super(ClassTimetableView, self).get_context_data(**kwargs)
        context['class'] = Class.objects.get(slug=context['class_slug'])
        context['days'] = ClassSubjectTime.WEEKDAY_CHOICES

        context['timetables_exist'] = False
        if Timetable.objects.exists():
            context['timetables_exist'] = True

        context['timetable_list'] = ''
        context['timetable_pk'] = ''
        context['block_timetable_change'] = False
        times = ''
        try:
            classtimetable = ClassTimetable.objects.get(
                    classroom__slug=context['class_slug'])
            context['timetable_pk'] = classtimetable.timetable.pk
        except ClassTimetable.DoesNotExist:
            # TODO Set a default timetable somewhere to be used when the
            # class doesn't have a timetable specified
            # TODO if there is timetables available, list them and send
            # a warning that there is no timetable linked to this class yet
            context['timetable_list'] = get_timetables()
        else:
            times = Time.objects.filter(
                    timetable=classtimetable.timetable)

            cst = ClassSubjectTime.objects.filter(
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
            for day_abbr, day in ClassSubjectTime.WEEKDAY_CHOICES:
                try:
                    class_subject_time = time.classsubjecttime_set.get(
                            class_subject__classroom=context['class'],
                            weekday=day_abbr)
                except ClassSubjectTime.DoesNotExist:
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
        if not classroom_pk or not time_pk or not weekday_abbr:
            return HttpResponseNotFound()
        classroom = Class.objects.get(pk=classroom_pk)
        time = Time.objects.get(pk=time_pk)

        if not class_subject_time_pk and not subject_pk:
            return HttpResponse()

        if not subject_pk:
            # TODO we shouldn't be deleting the subjects, we should keep the
            # time the subject remained on that class
            ClassSubjectTime.objects.get(
                class_subject__classroom=classroom, time=time,
                weekday=weekday_abbr
            ).delete()
            return HttpResponse()
        subject = Subject.objects.get(pk=subject_pk)
        class_subject = ClassSubject.objects.get(classroom=classroom,
                                                 subject=subject)
        if not class_subject:
            return HttpResponseNotFound()

        # TODO return and set the class_subject_time_pk in the html
        if class_subject_time_pk:
            class_subject_time = ClassSubjectTime.objects.get(
                    pk=class_subject_time_pk)
            class_subject_time.class_subject = class_subject
            class_subject_time.save()
            return HttpResponse(json.dumps(class_subject_time.pk),
                                mimetype="application/json")

        class_subject_time, created = ClassSubjectTime.objects.get_or_create(
                    weekday=weekday_abbr, time=time,
                    class_subject__classroom=class_subject.classroom,
                    defaults={'class_subject': class_subject})
        if not created:
            class_subject_time.class_subject = class_subject
            class_subject_time.save()
        return HttpResponse(json.dumps(class_subject_time.pk),
                            mimetype="application/json")

class ApplyClassTimetable(View):

    def post(self, request, *args, **kwargs):
        classroom_pk = request.POST.get('class_pk', None)
        timetable_pk = request.POST.get('timetable_pk', None)
        classtimetable, created = ClassTimetable.objects.get_or_create(
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
