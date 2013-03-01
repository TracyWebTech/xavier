from django.db import models
from school.models import School


class Period(models.Model):
    name = models.CharField(max_length=50)
    year = models.DateField()
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.name


class SubPeriod(models.Model):
    name = models.CharField(max_length=30)
    start = models.DateField()
    end = models.DateField()
    period = models.ForeignKey(Period)

    def __unicode__(self):
        return self.name
