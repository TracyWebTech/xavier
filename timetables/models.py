# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Timetable(models.Model):
    school = models.ForeignKey("schools.School")
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
    timetable = models.ForeignKey("timetables.Timetable",
                                  verbose_name=_('timetable'))
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        ordering = ['start', ]

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


class ClassTimetable(models.Model):
    classroom = models.ForeignKey('classes.Class', verbose_name=_('classroom'),
                                  unique=True)
    timetable = models.ForeignKey('timetables.Timetable',
                                  verbose_name=_('timetable'))


class ClassSubjectTime(models.Model):
    # weekday
    WEEKDAY_CHOICES = (
        ('mon', _('Monday')),
        ('tue', _('Tuesday')),
        ('wed', _('Wednesday')),
        ('thu', _('Thursday')),
        ('fri', _('Friday')),
        ('sat', _('Saturday')),
        ('sun', _('Sunday')),
    )
    weekday = models.CharField(_('weekday'), max_length=3,
        choices=WEEKDAY_CHOICES)
    class_subject = models.ForeignKey('classes.ClassSubject',
                                      verbose_name=_('class subject'))
    time = models.ForeignKey("timetables.Time", verbose_name=_('time'))

    def get_all_classes(self, subperiod):
        # the var below has the number of existing classes given on the week
        weekdays = {'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4,
                'sat': 5, 'sun': 6}
        days = subperiod.get_days()
        csts = ClassSubjectTime.objects.filter(
            class_subject=self.class_subject
        )
        classes_given = 0
        for cst in csts:
            classes_given += days[weekdays[cst.weekday]]
        return classes_given

    def __unicode__(self):
        return u'{0} - {1}'.format(self.time, self.class_subject)

    def clean(self):
        class_subject_time = ClassSubjectTime.objects.filter(
            weekday=self.weekday,
            class_subject__classroom=self.class_subject.classroom,
            time=self.time
        )
        if self.pk:
            class_subject_time = class_subject_time.exclude(pk=self.pk)
        if class_subject_time.exists():
            raise ValidationError(ugettext(
                    "A class subject time already exist"))

    class Meta:
        verbose_name = _('class subject time')
        verbose_name_plural = _('class subject times')
        unique_together = ('class_subject', 'weekday', 'time')
