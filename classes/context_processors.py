# -*- coding: utf-8 -*-

from classes.models import Class, ClassSubject
from schools.models import School


def all_classes(request):
    school = School.objects.get_current()
    return dict(classes=Class.objects.filter(period__school=school))
