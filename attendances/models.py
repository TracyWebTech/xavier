# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AttendanceBook(models.Model):
    classroom = models.ForeignKey('classes.Class')
    day = models.DateField()

    class Meta:
        unique_together = ('classroom', 'day')
        verbose_name = _('attendance book')
        verbose_name_plural = _('attendance books')


class Attendance(models.Model):
    attendance_book = models.ForeignKey(AttendanceBook)
    student = models.ForeignKey('accounts.Student')

    class Meta:
        unique_together = ('attendance_book', 'student')
        verbose_name = _('attendance')
        verbose_name_plural = _('attendances')
