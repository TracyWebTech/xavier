# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from schools.models import School

from datetime import datetime, timedelta


class Period(models.Model):
    name = models.CharField(max_length=50, verbose_name=_(u'name'))
    year = models.DateField(verbose_name=_(u'year'))
    school = models.ForeignKey(School, verbose_name=_(u'school'))

    class Meta:
        verbose_name = _(u'period')
        verbose_name_plural = _(u'periods')

    def __unicode__(self):
        return self.name


class SubPeriod(models.Model):
    name = models.CharField(max_length=30, verbose_name=_(u'name'))
    start = models.DateField(verbose_name=_(u'start'))
    end = models.DateField(verbose_name=_(u'end'))
    period = models.ForeignKey(Period, verbose_name=_(u'period'))

    class Meta:
        verbose_name = _(u'subperiod')
        verbose_name_plural = _(u'subperiods')

    def save(self, *args, **kwargs):
        # validate subperiod
        if self.end <= self.start:
            raise ValidationError("End before start.")
        x = Q(start__lte=self.start, end__gte=self.end)
        y = Q(start__gte=self.start, end__lte=self.start)
        subperiods = SubPeriod.objects.filter(x | y).exists()
        if subperiods:
            raise ValidationError(_("Invalid subperiod."))
        super(SubPeriod, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
