from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from schools.models import School

from datetime import datetime, timedelta


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

    def save(self, *args, **kwargs):
        # validate subperiod
        if self.end <= self.start:
            raise ValidationError("End before start.")
        x = Q(start__lte=self.start, end__gte=self.end)
        y = Q(start__gte=self.start, end__lte=self.start)
        subperiods = SubPeriod.objects.filter(x | y).exists()
        if subperiods:
            raise ValidationError(_("Invalid subperiod."))
        super(SubPeriod, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
