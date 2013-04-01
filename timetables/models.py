# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Timetable(models.Model):
    calendar = models.ForeignKey('calendars.Calendar')
    class_subject = models.ForeignKey('classes.ClassSubject')
    start = models.TimeField()
    end = models.TimeField()


class SpecialTimetable(Timetable):
    day = models.DateField()
    replacement_teacher = models.ForeignKey(
        'accounts.Teacher',
        null=True, blank=True,
        verbose_name=_(u'replacement teacher'),
    )


class Attendance(models.Model):
    day = models.DateField()
    student = models.ForeignKey('accounts.Student')
    timetable = models.ForeignKey(Timetable)
    is_attendee = models.BooleanField() # TODO: review field name, not sure about it
