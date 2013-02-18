from django.db import models
from school.models import School


class Period(models.Model):
    name = models.CharField(max_length=50)
    year = models.DateTimeField()
    school = models.ForeignKey(School)


class SubPeriod(models.Model):
    name = models.CharField(max_length=30)
    start = models.DateField()
    end = models.DateField()
    period = models.ForeignKey(Period)
