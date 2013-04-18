# -*- coding: utf-8 -*-

from django.views import generic
from django.core.urlresolvers import reverse_lazy

from xavier.views import GenericTemplateMixin
from classes import models, forms


class ClassList(GenericTemplateMixin, generic.ListView):
    model = models.Class
    paginate_by = 20


class ClassDetail(GenericTemplateMixin, generic.DetailView):
    model = models.Class


class ClassCreate(GenericTemplateMixin, generic.CreateView):
    model = models.Class


class ClassUpdate(GenericTemplateMixin, generic.UpdateView):
    model = models.Class


class ClassDelete(GenericTemplateMixin, generic.DeleteView):
    model = models.Class
    success_url = reverse_lazy('classes-class-list')
