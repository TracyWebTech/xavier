# -*- coding: utf-8 -*-

from towel.modelview import ModelView

from .models import Period


class PeriodView(ModelView):
    paginate_by = 20

period_views = PeriodView(Period)
