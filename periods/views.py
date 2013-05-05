# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

from xavier import views
from periods import models
from schools.models import School


def period_select(request, pk):
    try:
        subperiod = models.SubPeriod.objects.get(pk=pk)
    except models.SubPeriod.DoesNotExist:
        pass
    else:
        request.set_subperiod(subperiod)

    next = request.GET.get('next', '/')
    return redirect(next)


class PeriodMixin(object):
    model = models.Period


class PeriodList(PeriodMixin, views.ListView):
    paginate_by = 20


class PeriodDetail(PeriodMixin, views.DetailView):
    pass


class PeriodCreate(PeriodMixin, views.CreateView):
    pass


class PeriodUpdate(PeriodMixin, views.UpdateView):
    pass


class PeriodDelete(PeriodMixin, views.DeleteView):
    success_url = reverse_lazy('period-list')


period_list = PeriodList.as_view()
period_detail = PeriodDetail.as_view()
period_create = PeriodCreate.as_view()
period_update = PeriodUpdate.as_view()
period_delete = PeriodDelete.as_view()
