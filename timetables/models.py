# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from schools.models import School
from subjects.models import Subject


class Timetable(models.Model):
    school = models.ForeignKey(School)
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _('timetable')
        verbose_name_plural = _('timetables')

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self))
        super(Timetable, self).save(*args, **kwargs)


class Time(models.Model):
    timetable = models.ForeignKey(Timetable, verbose_name=_('timetable'))
    start = models.TimeField()
    end = models.TimeField()

    def __unicode__(self):
        return u'{0} - {1}'.format(unicode(self.start), unicode(self.end))

    def clean(self):
        if self.end <= self.start:
            error_msg = _('The start must be before the end')
            raise ValidationError(error_msg)

        intersection = Time.objects.filter(Q(
            start__lte=self.start, end__gte=self.start
        ) | Q(
            start__gte=self.start, start__lt=self.end
        ), timetable__name=self.timetable.name)

        if self.pk:
            intersection.exclude(pk=self.pk)

        if intersection.exists():
            error_msg = _('Schedule not valid')
            raise ValidationError(error_msg)

class ClassSubjectTime(models.Model):
    WEEKDAY_CHOICES = (
        (_('mon'), _('Monday')),
        (_('tue'), _('Tuesday')),
        (_('wed'), _('Wednesday')),
        (_('thu'), _('Thursday')),
        (_('fri'), _('Friday')),
        (_('sat'), _('Saturday')),
        (_('sun'), _('Sunday')),
    )
    weekday = models.CharField(_('weekday'), max_length=3,
        choices=WEEKDAY_CHOICES)
    class_subject = models.ForeignKey('classes.ClassSubject',
                                      verbose_name=_('class subject'))
    time = models.ForeignKey(Time, verbose_name=_('time'))

    def __unicode__(self):
        return u'{0} - {1}'.format(self.time, self.class_subject)

    class Meta:
        verbose_name = _('class subject time')
        verbose_name_plural = _('class subject times')
        unique_together = ('class_subject', 'weekday', 'time')
