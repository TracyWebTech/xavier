import calendar

from django import template
from django.utils import timezone
from django.utils.translation import ugettext

register = template.Library()


@register.simple_tag()
def get_month_name(bimester, month):
    width = 2
    month_name = calendar.month_name[bimester * width + month]
    return ugettext(month_name)
