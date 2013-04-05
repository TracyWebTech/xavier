# -*- coding: utf-8 -*-

from datetime import date
from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import Student
from classes.models import ClassSubject
from .models import NonAttendance


class NonAttendanceTestCase(TestCase):
    fixtures = ['tests/accounts.json', 'tests/classes.json']

    def setUp(self):
        self.student1 = Student.objects.get(pk=4)
        self.class_subject = ClassSubject.objects.get(pk=1)

    def testNonAttendanceModel(self):
        today = date.today()
        nonattendance1 = NonAttendance.objects.create(
            student=self.student1,
            class_subject=self.class_subject,
            day=today,
        )
        nonattendance2 = NonAttendance(
            student=self.student1,
            class_subject=self.class_subject,
            day=today,
        )
        with self.assertRaises(ValidationError):
            nonattendance2.full_clean()
