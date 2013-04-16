# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import Student


class AttendanceBook(models.Model):
    classroom = models.ForeignKey('classes.Class')
    day = models.DateField()
    students = models.ManyToManyField(
        Student,
        through='attendances.Attendance',
        verbose_name=_('students')
    )

    class Meta:
        unique_together = ('classroom', 'day')
        verbose_name = _('attendance book')
        verbose_name_plural = _('attendance books')

    def __unicode__(self):
        return u'%s, %s' % (self.classroom.identification, self.day)

    def is_late(self, student):
        try:
            attendance = self.attendance_set.get(student=student)
        except Attendance.DoesNotExist:
            return None
        return attendance.is_late


class Attendance(models.Model):
    attendance_book = models.ForeignKey(
        'attendances.AttendanceBook',
        verbose_name=_('attendance book'))
    student = models.ForeignKey('accounts.Student', verbose_name=_('student'))
    is_late = models.BooleanField(_('is late?'))

    class Meta:
        unique_together = ('attendance_book', 'student')
        verbose_name = _('attendance')
        verbose_name_plural = _('attendances')
