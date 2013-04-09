# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import modelform_factory

from xavier.views import ModelView

from .models import Class


class ClassView(ModelView):
    paginate_by = 20

    def get_query_set(self, request, *args, **kwargs):
        # Filter items only from current school
        qs = super(ModelView, self).get_query_set(request, *args, **kwargs)
        return qs.filter(period__school=self.get_current_school(request))


class_views = ClassView(Class)
