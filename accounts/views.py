# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import modelform_factory

from xavier.views import ModelView

from .models import Student, Teacher, Employee


class AccountView(ModelView):
    paginate_by = 20

    def get_query_set(self, request, *args, **kwargs):
        # Filter items only from current school
        qs = super(ModelView, self).get_query_set(request, *args, **kwargs)
        return qs.filter(school=self.get_current_school(request))

    def get_form(self, request, instance=None, change=None, **kwargs):
        # Overriding just to exclude school field
        formfield_callback = self.get_formfield_callback(request)
        kwargs.setdefault('formfield_callback', formfield_callback)
        kwargs.setdefault('form', self.form_class or forms.ModelForm)
        return modelform_factory(self.model, exclude=('school',), **kwargs)

    def save_model(self, request, instance, form, change):
        if not change:
            instance.school = self.get_current_school(request)
        instance.save()


students_views = AccountView(Student)
teachers_views = AccountView(Teacher)
employees_views = AccountView(Employee)
