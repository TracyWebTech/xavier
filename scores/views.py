# Create your views here.

import json
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.utils import simplejson

from accounts.models import Student
from classes.models import Class, ClassSubject
from periods.models import Period
from scores.models import EvaluationCriteria, Score, StudentScore


def classes_list(request):
    return render(request, 'scores/classes_list.html', {})


def scores_list(request, year, class_slug, subject_slug):
    class_subject = get_object_or_404(ClassSubject,
                                      classroom__slug=class_slug,
                                      subject__slug=subject_slug)
    students = class_subject.classroom.students.filter()
    subperiod = class_subject.classroom.period.subperiod_set
    subperiod = subperiod.prefetch_related('period')

    return render(request, 'scores/scores_list.html', {'year': year,
        'title': unicode(class_subject),
        'class_subject': class_subject,
        'students': students,
        'criterias': class_subject.evaluationcriteria_set.values(),
    })


def get_score(request):
    data = request.POST.get('data', None)
    student_id = request.POST.get('student_id', None)
    if not data or not student_id:
        return HttpResponseBadRequest()

    student = Student.objects.get(pk=student_id)

    scores = simplejson.loads(data)
    average = 0
    weight = 0
    for criteria_id, score in scores.items():
        criteria = EvaluationCriteria.objects.get(pk=criteria_id)
        criteria_weight = float(criteria.weight)
        if score:
            try:
                score = float(score)
            except score.ValueError:
                # TODO display a message to user if a letter is send
                msg = u'Only numbers are allowed'
                HttpResponse(msg)
            else:
                # student_score = StudentScore.objects.create(score=score)
                # Score.objects.create(
                #     student=student,
                #     scores=student_score,
                #     criteria=criteria,
                # )
                average += score * criteria_weight
        weight += criteria_weight
    average = average / weight

    # TODO if average is bigger than 10, set a msg and the average field to 10
    # or don't allow values bigger than 10 on template
    return HttpResponse(json.dumps(average), mimetype="application/json")


def get_subjects(request):
    class_pk = request.POST.get('class_pk', None)
    if not class_pk:
        return HttpResponseNotFound()
    classroom = Class.objects.get(pk=class_pk)
    class_subjects = classroom.classsubject_set.all()
    data = []
    for class_subject in class_subjects:
        subject = class_subject.subject
        url = reverse('scores_list', args=[
                classroom.period.year, subject.slug, classroom.slug])
        data.append([subject.name, url])
    return HttpResponse(json.dumps(data), mimetype="application/json")
