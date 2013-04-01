# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Calendar(models.Model):
    """
    By default all days in a period are school days unless otherwise
    specified using the Break model.

    """
    period = models.ForeignKey('periods.Period')

    class Meta:
        verbose_name = _('calendar')
        verbose_name_plural = _('calendars')

    def __unicode__(self):
        return u"{0}'s calendar".format(self.period)


class Break(models.Model):
    """
    Use it to determine weekends with no classes, holidays and days
    off.

    """
    calendar = models.ForeignKey(Calendar)
    day = models.DateField(_('day'))

    class Meta:
        verbose_name = _('break')
        verbose_name_plural = _('breaks')
