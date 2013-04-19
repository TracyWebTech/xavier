# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy

from xavier import views
from periods import models
from schools.models import School


class PeriodBaseMixin(object):
    model = models.Period

    @property
    def current_school(self):
        return School.objects.get_current(self.request)

    def get_queryset(self):
        queryset = super(PeriodBaseMixin, self).get_queryset()
        return queryset.filter(school=self.current_school)


class PeriodList(PeriodBaseMixin, views.ListView):
    paginate_by = 20


class PeriodDetail(PeriodBaseMixin, views.DetailView):
    pass


class PeriodCreate(PeriodBaseMixin, views.CreateView):
    pass


class PeriodUpdate(PeriodBaseMixin, views.UpdateView):
    pass


class PeriodDelete(PeriodBaseMixin, views.DeleteView):
    success_url = reverse_lazy('period-list')


period_list = PeriodList.as_view()
period_detail = PeriodDetail.as_view()
period_create = PeriodCreate.as_view()
period_update = PeriodUpdate.as_view()
period_delete = PeriodDelete.as_view()
