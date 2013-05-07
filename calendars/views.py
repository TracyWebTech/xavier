import calendar

from datetime import date

from django import http
from django.core import exceptions
from django.views import generic
from django.utils.translation import ugettext

from calendars import models


class Calendar(generic.TemplateView):
    template_name = 'calendars/calendar.html'

    def get_context_data(self, request, **kwargs):
        cal = calendar.Calendar(calendar.SUNDAY)
        context = super(Calendar, self).get_context_data(**kwargs)
        context.update({
            'title': ugettext('Calendar'),
            'calendar': cal.yeardatescalendar(request.subperiod.period.year, 2),
        })
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return self.render_to_response(context)


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
