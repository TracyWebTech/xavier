# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class NonAttendance(models.Model):
    student = models.ForeignKey('accounts.Student')
    class_subject = models.ForeignKey('classes.ClassSubject')
    day = models.DateField()

    class Meta:
        verbose_name = _('non-attendance')
        verbose_name_plural = _('non-attendances')
