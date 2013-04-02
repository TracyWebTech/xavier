# -*- coding: utf-8 -*-

from datetime import date
from django.core.exceptions import ValidationError
from django.test import TestCase

from periods.models import Period
from .models import Calendar, Break


class CalendarTestCase(TestCase):
    fixtures = ['tests/periods.json']

    def setUp(self):
        self.period = Period.objects.get(pk=1)

    def testCalendarModel(self):
        calendar1 = Calendar.objects.create(period=self.period)
        calendar2 = Calendar(period=self.period)
        with self.assertRaises(ValidationError):
            calendar2.full_clean()


class BreakTestCase(TestCase):
    fixtures = ['tests/periods.json']

    def setUp(self):
        self.period = Period.objects.get(pk=1)
        self.calendar = Calendar.objects.create(period=self.period)

    def testBreakModel(self):
        today = date.today()
        break1 = Break.objects.create(calendar=self.calendar, day=today)
        break2 = Break.objects.create(calendar=self.calendar, day=today)
        with self.assertRaises(ValidationError):
            break2.full_clean()
