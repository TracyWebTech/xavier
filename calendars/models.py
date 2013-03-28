# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Calendar(models.model):
    period = models.ForeignKey('periods.Period')
    policy = models.CharField(
        _('policy'),
        max_length=20,
        choices=(
            ('break',     _('Day off unless otherwise specified')),
            ('schoolday', _('School day unless otherwise specified')),
        ),
        default='break',
    )
    is_weekends_break = models.BooleanField(
        _('break on weekends'),
        help_text=_('Mark if weekends are (usually) considered days off'),
    )


class Break(models.Model):
    calendar = models.ForeignKey(Calendar)
    day = models.DateField(_('day'))


class SchoolDay(models.Model):
    calendar = models.ForeignKey(Calendar)
    day = models.DateField(_('day'))
