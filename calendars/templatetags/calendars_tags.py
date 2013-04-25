import calendar

from datetime import date

from django import template
from django.utils.translation import ugettext

from calendars import models


register = template.Library()


@register.simple_tag()
def get_month_name(bimester, month):
    width = 2
    month_name = calendar.month_name[bimester * width + month]
    return ugettext(month_name)


@register.filter
def is_break(day):
    calendar = models.Calendar.objects.all()[0]  # TODO
    try:
        models.Break.objects.get(calendar=calendar, day=day)
        return True
    except models.Break.DoesNotExist:
        return False
