# Create your views here.

import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404

from classes.models import ClassSubject
from periods.models import Period


def list(request, year, class_subject_slug):
    class_subject = get_object_or_404(ClassSubject, slug=class_subject_slug)
    students = class_subject.classroom.students.filter()

    return render(request, 'scores/list.html', {'year': year,
        'class': class_subject,
        'students': students,
        'criterias': class_subject.evaluationcriteria_set.values(),
    })

def get_score(request):
    # scores = request.POST.get('scores', None)
    if not scores:
        return HttpResponseBadRequest()
    average = 0
    return HttpResponse(json.dumps(average), mimetype="application/json")
