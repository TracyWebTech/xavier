import calendar

from datetime import date

from django.views import generic
from django.utils.translation import ugettext

from calendars import models


class Calendar(generic.TemplateView):
    template_name = 'calendars/calendar.html'

    def get_context_data(self, **kwargs):
        context = super(Calendar, self).get_context_data(**kwargs)
        context.update({
            'title': ugettext('Calendar'),
            'subtitle': '2013',
            'calendar': calendar.Calendar(calendar.SUNDAY).yeardatescalendar(2013, 2),
            'today': date.today()
        })
        return context
