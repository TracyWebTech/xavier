# -*- coding: utf-8 -*-

from classes.models import ClassSubject
from schools.models import School


def all_classes(request):
    school = School.objects.get_current(request)
    return dict(classes=ClassSubject.objects.filter(teacher__school=school))
