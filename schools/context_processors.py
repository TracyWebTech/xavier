# -*- coding: utf-8 -*-

from schools.models import School


def current_school(request):
    # School's manager already performs a cache for the
    # ``get_current`` method so you don't need worry about that
    return dict(current_school=School.objects.get_current())
