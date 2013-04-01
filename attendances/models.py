# -*- coding: utf-8 -*-

from django.db import models


class NonAttendance(models.Model):
    student = models.ForeignKey('accounts.Student')
    class_subject = models.ForeignKey('classes.ClassSubject')
    day = models.DateField()
