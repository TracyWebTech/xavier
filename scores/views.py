# Create your views here.

from django.shortcuts import render, get_object_or_404

from classes.models import Class
from periods.models import Period


def list(request, year, period_slug, class_slug):
    class_obj = get_object_or_404(Class, slug=class_slug)
    period = get_object_or_404(Period, slug=period_slug)
    students = class_obj.students.filter()
    context = {
        'year': year,
        'period': period,
        'class': class_obj,
        'students': students,
    }

    return render(request, 'scores/list.html', context)
