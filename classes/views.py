# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy

from xavier import views
from classes import models
from schools.models import School


class ClassBaseMixin(object):
    model = models.Class

    @property
    def current_school(self):
        return School.objects.get_current(self.request)

    def get_queryset(self):
        queryset = super(PeriodBaseMixin, self).get_queryset()
        return queryset.filter(school=self.current_school)


class ClassList(ClassBaseMixin, views.ListView):
    paginate_by = 20


class ClassDetail(ClassBaseMixin, views.DetailView):
    pass


class ClassCreate(ClassBaseMixin, views.CreateView):
    pass


class ClassUpdate(ClassBaseMixin, views.UpdateView):
    pass


class ClassDelete(views.DeleteView):
    success_url = reverse_lazy('class-list')


class_list = ClassList.as_view()
class_detail = ClassDetail.as_view()
class_create = ClassCreate.as_view()
class_update = ClassUpdate.as_view()
class_delete = ClassDelete.as_view()
