# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from datetime import timedelta

from calendars.models import Calendar
from schools.managers import CurrentSchoolManager


class Period(models.Model):
    name = models.CharField(max_length=50, verbose_name=_(u'name'))
    year = models.PositiveSmallIntegerField(verbose_name=_(u'year'))
    school = models.ForeignKey("schools.School", verbose_name=_(u'school'))
    slug = models.SlugField(max_length=50, null=True, unique=True)

    objects = models.Manager()
    on_school = CurrentSchoolManager()

    class Meta:
        unique_together = ('name', 'year', 'school')
        verbose_name = _(u'period')
        verbose_name_plural = _(u'periods')

    def __unicode__(self):
        return u'{0} ({1})'.format(self.name, self.school.short_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self))
        super(Period, self).save(*args, **kwargs)

    def get_current_subperiod(self):
        now = timezone.now().date()
        return self.subperiod_set.filter(start__lte=now, end__gte=now).get()


class SubPeriod(models.Model):
    name = models.CharField(max_length=30, verbose_name=_(u'name'))
    start = models.DateField(verbose_name=_(u'start'))
    end = models.DateField(verbose_name=_(u'end'))
    period = models.ForeignKey("periods.Period", verbose_name=_(u'period'))
    slug = models.SlugField(max_length=30, null=True, unique=True)

    class Meta:
        unique_together = ('name', 'period')
        verbose_name = _(u'subperiod')
        verbose_name_plural = _(u'subperiods')

    def get_days(self):
        days = {}
        for day in range(int((self.end - self.start).days)):
            weekday = (self.start + timedelta(day)).weekday()
            days[weekday] = days[weekday] + 1 if weekday in days else 1
        return days

    def save(self, *args, **kwargs):
        # validate subperiod
        if self.end <= self.start:
            raise ValidationError("End before start.")
        x = Q(start__lte=self.start, end__gte=self.end)
        y = Q(start__gte=self.start, end__lte=self.start)
        subperiods = SubPeriod.objects.filter(x | y).exists()
        if subperiods:
            raise ValidationError(_("Invalid subperiod."))

        self.slug = slugify(unicode(self))

        super(SubPeriod, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


@receiver(signals.post_save, sender=Period)
def create_calendar_for_period(sender, instance, created, **kwargs):
    if created:
        Calendar.objects.create(period=instance)
