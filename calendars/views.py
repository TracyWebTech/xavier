import calendar

from datetime import date

from django import http
from django.core import exceptions
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


def ajax_toggle_break(request):
    if request.is_ajax():
        try:
            year, month, month_day = request.GET.get('day').split('-')
            day = date(int(year), int(month), int(month_day))
            calendar = models.Calendar.objects.all()[0]  # TODO
        except ValueError:
            return http.HttpResponse(status=400)
        except AttributeError:
            return http.HttpResponse(status=400)
        except exceptions.ObjectDoesNotExist:
            return http.HttpResponse(status=400)
        break_, created = models.Break.objects.get_or_create(
            calendar=calendar,
            day=day,
        )
        if not created:
            break_.delete()
        return http.HttpResponse(status=200)
    return http.HttpResponse(status=400)
