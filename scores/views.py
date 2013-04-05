# Create your views here.

from django.shortcuts import render


def list(request, school_slug, class_slug, year, period_slug):
    context = {
        'class': class_slug,
        'year': year,
        'period': period_slug,
    }

    return render(request, 'scores/list.html', context)
