# -*- coding: utf-8 -*-

from schools.models import School


def current_school(request):
    return dict(current_school=School.objects.get_current(request))
