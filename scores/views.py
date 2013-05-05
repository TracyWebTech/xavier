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
    return render(request, 'scores/classes_list.html', {
        'title': ugettext(u'Scores'),
    })


def scores_list(request, subject_slug, class_slug):
    class_subject = get_object_or_404(ClassSubject,
                                      classroom__slug=class_slug,
                                      subject__slug=subject_slug)
    students = class_subject.classroom.students.filter()

    subperiod = request.subperiod
    students_list = []
    criterias = class_subject.evaluationcriteria_set.all()

    math = u'('
    weight = 0
    for criteria in criterias:
        math += u'{0} x {1} + '.format(criteria.name,
                                       unicode(criteria.weight))
        weight += float(criteria.weight)
    math = math[:-3]
    math += ') / {0}'.format(unicode(weight))

    for student in students:
        student_scores = {}
        student_scores['student'] = student
        student_scores['scores'] = {}
        try:
            average = student.get_average(subperiod.pk, class_subject)
        except ZeroDivisionError:
            average = None
        else:
            student_scores['average'] = average


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

    subtitle = u'{0}, {1} - {2}, {3}'.format(
        class_subject.subject,
        class_subject.classroom.grade,
        class_subject.classroom.identification,
        class_subject.classroom.period.name
    )
    teacher_subject = u'{0} {1} - {2}'.format(ugettext(u'Teacher'),
            class_subject.teacher,
            class_subject.subject.name)
    return render(request, 'scores/scores_list.html', {'year': '2013',
        'title': ugettext(u'Scores'),
        'subtitle': subtitle,
        'teacher_subject': teacher_subject,
        'students_list': students_list,
        'criterias': criterias,
        'subperiod_pk': subperiod.pk,
        'math': math,
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
                if float(score) < 0:
                    return HttpResponseBadRequest()
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
    average = round((average / weight), 1)

    # TODO if average is bigger than 10, set a msg and the average field to 10
    # or don't allow values bigger than 10 on template
    return HttpResponse(json.dumps(average), mimetype="application/json")
