# Create your views here.

import json
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext

from accounts.models import Student
from classes.models import Class, ClassSubject
from periods.models import Period, SubPeriod
from scores.models import EvaluationCriteria, Score


def classes_list(request):
    # TODO Dynamic year instead hardcoded
    return render(request, 'scores/classes_list.html', {
        'title': ugettext(u'Scores'),
        'subtitle': u'{} 2013'.format(ugettext(u'Classes')),
    })


def scores_list(request, year, subject_slug, class_slug):
    class_subject = get_object_or_404(ClassSubject,
                                      classroom__slug=class_slug,
                                      subject__slug=subject_slug)
    students = class_subject.classroom.students.filter()
    subperiod = class_subject.classroom.period.get_current_subperiod()
    students_list = []
    criterias = class_subject.evaluationcriteria_set.all()

    for student in students:
        student_scores = {}
        student_scores['student'] = student
        student_scores['scores'] = {}
        student_scores['average'] = student.get_average(subperiod.pk)

        # returns a qs with scores of given student
        scores = student.get_scores(subperiod_id=subperiod.pk)
        for criteria in criterias:
            for score in scores:
                if score.criteria == criteria:
                    student_scores['scores'][criteria.pk] = score.score
                    break
            else:
                student_scores['scores'][criteria.pk] = ''
        students_list.append(student_scores)

    title = u"{0} - {1}, {2}".format(class_subject.classroom.grade,
            class_subject.classroom.identification,
            subperiod.name)
    return render(request, 'scores/scores_list.html', {'year': year,
        'title': title,
        'subtitle': class_subject.subject.name,
        'class_subject': class_subject,
        'students_list': students_list,
        'criterias': criterias,
        'subperiod_pk': subperiod.pk,
    })


def get_score(request):
    data = request.POST.get('data', None)
    student_id = request.POST.get('student_id', None)
    subperiod_pk = request.POST.get('subperiod_pk', None)
    if not data or not student_id or not subperiod_pk:
        return HttpResponseBadRequest()

    student = Student.objects.get(pk=student_id)
    subperiod = SubPeriod.objects.get(pk=subperiod_pk)

    scores = json.loads(data)
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
                score_obj, created = Score.objects.get_or_create(
                        student=student,
                        criteria=criteria,
                        subperiod=subperiod,
                        defaults={'score': score, }
                )
                if not created:
                    score_obj.score = score
                    score_obj.save()
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
