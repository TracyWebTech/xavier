# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import Student
from schools.managers import CurrentSchoolManager


class AttendanceBook(models.Model):
    classroom = models.ForeignKey('classes.Class')
    day = models.DateField()
    students = models.ManyToManyField(
        Student,
        through='attendances.Attendance',
        verbose_name=_('students')
    )

    objects = models.Manager()
    on_school = CurrentSchoolManager(school_field='classroom__period__school')

    class Meta:
        unique_together = ('classroom', 'day')
        verbose_name = _('attendance book')
        verbose_name_plural = _('attendance books')

    def __unicode__(self):
        return u'%s, %s' % (self.classroom.identification, self.day)

    def get_student_explanation(self, student):
        try:
            attendance = self.attendance_set.get(student=student)
        except Attendance.DoesNotExist:
            return ''
        return attendance.explanation

    def get_student_status(self, student):
        try:
            attendance = self.attendance_set.get(student=student)
        except Attendance.DoesNotExist:
            return Attendance.ABSENT
        return attendance.status

    def is_late(self, student):
        status = self.get_student_status(student)
        if status == Attendance.LATE:
            return True
        return False

    def is_present(self, student):
        status = self.get_student_status(student)
        if status == Attendance.PRESENT:
            return True
        return False

    def is_absent(self, student):
        status = self.get_student_status(student)
        if status == Attendance.ABSENT:
            return True
        return False


class Attendance(models.Model):
    PRESENT = 'present'
    LATE = 'late'
    ABSENT = 'absent'
    STATUS_CHOICES = (
        (PRESENT, _('Present')),
        (LATE,    _('Present but late')),
        (ABSENT,  _('Absent')),
    )

    attendance_book = models.ForeignKey(
        'attendances.AttendanceBook',
        verbose_name=_('attendance book')
    )
    student = models.ForeignKey('accounts.Student', verbose_name=_('student'))
    status = models.CharField(
        _('status'),
        max_length=8,
        choices=STATUS_CHOICES,
        default='present',
    )
    explanation = models.TextField(_('notes'), blank=True)

    objects = models.Manager()
    on_school = CurrentSchoolManager(
        school_field='attendance_book__classroom__period__school'
    )

    class Meta:
        unique_together = ('attendance_book', 'student')
        verbose_name = _('attendance')
        verbose_name_plural = _('attendances')
