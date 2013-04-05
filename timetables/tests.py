# -*- coding: utf-8 -*-

from datetime import date
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.timezone import now

from accounts.models import Teacher
from calendars.models import Calendar
from classes.models import ClassSubject
from .models import Timetable


class TimetableTestCase(TestCase):
    fixtures = ['tests/accounts.json', 'tests/classes.json',
                'tests/calendars.json']

    def setUp(self):
        self.calendar = Calendar.objects.get(pk=1)
        self.class_subject = ClassSubject.objects.get(pk=1)
        self.teacher = Teacher.objects.get(pk=6)

    def testTimetableModel(self):
        Timetable.objects.create(
            calendar=self.calendar,
            class_subject=self.class_subject,
            start=now(),
            end=now(),
            weekday='mon',
        )
        Timetable.objects.create(
            calendar=self.calendar,
            class_subject=self.class_subject,
            start=now(),
            end=now(),
            day=date.today(),
            replacement_teacher=self.teacher,
        )
        with self.assertRaises(ValidationError):
            timetable = Timetable(
                calendar=self.calendar,
                class_subject=self.class_subject,
                start=now(),
                end=now(),
                weekday='sun',
                day=date.today()
            )
            timetable.full_clean()
