# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy

from xavier import views
from classes import models, forms


class ClassList(views.ListView):
    model = models.Class
    paginate_by = 20


class ClassDetail(views.DetailView):
    model = models.Class


class ClassCreate(views.CreateView):
    model = models.Class


class ClassUpdate(views.UpdateView):
    model = models.Class


class ClassDelete(views.DeleteView):
    model = models.Class
    success_url = reverse_lazy('classes-class-list')
