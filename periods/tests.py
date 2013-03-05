from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Period, SubPeriod
from schools.models import School

from datetime import datetime, timedelta


class PeriodsTest(TestCase):
    def setUp(self):
        self.school = School.objects.create(name='escolateste')

    def test_period_ok(self):
        period = Period.objects.create(name='anual', year='2013-02-02',
                                       school=self.school)

    def test_subperiod_ok(self):
        period = Period.objects.create(name='anual', year='2013-02-02',
                                       school=self.school)
        start = datetime.now().date()
        end = start + timedelta(weeks=8)
        subperiod = SubPeriod.objects.create(name='1 bimestre', start=start,
                                             end=end, period=period)

    def test_subperiod_duplicate(self):
        period = Period.objects.create(name='anual', year='2013-02-02',
                                       school=self.school)
        start = datetime.now().date()
        end = start + timedelta(weeks=8)
        subperiod = SubPeriod.objects.create(name='1 bimestre', start=start,
                                             end=end, period=period)
        with self.assertRaises(ValidationError):
            SubPeriod.objects.create(name='2 bimestre', start=start, end=end,
                                     period=period)

    def test_subperiod_end_before_start(self):
        period = Period.objects.create(name='anual', year='2013-02-02',
                                       school=self.school)
        start = datetime.now().date()
        end = start - timedelta(weeks=8)
        with self.assertRaises(ValidationError):
            SubPeriod.objects.create(name='1 bimestre', start=start, end=end,
                                     period=period)

    def test_subperiod_over_another(self):
        period = Period.objects.create(name='anual', year='2013-02-02',
                                       school=self.school)
        start = datetime.now().date()
        end = start + timedelta(weeks=8)
        subperiod = SubPeriod.objects.create(name='1 bimestre', start=start,
                                             end=end, period=period)
        with self.assertRaises(ValidationError):
            start += timedelta(weeks=4)
            subperiod = SubPeriod.objects.create(
                name='1 bimestre',
                start=start,
                end=end,
                period=period
            )
