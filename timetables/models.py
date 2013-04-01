# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Timetable(models.Model):
    calendar = models.ForeignKey('calendars.Calendar')
    class_subject = models.ForeignKey('classes.ClassSubject')
    start = models.TimeField()
    end = models.TimeField()
    weekday = models.CharField(
        _('weekday'),
        max_length=3,
        choices=(
            ('mon', 'Monday'),
            ('tue', 'Tuesday'),
            ('wed', 'Wednesday'),
            ('thu', 'Thursday'),
            ('fri', 'Friday'),
            ('sat', 'Saturday'),
            ('sun', 'Sunday'),
        ),
        null=True, blank=True,
    )

    # The following fields are useful to specify extra classes and/or
    # replacement teachers
    day = models.DateField(
        _('day'),
        null=True, blank=True,
    )
    replacement_teacher = models.ForeignKey(
        'accounts.Teacher',
        null=True, blank=True,
        verbose_name=_(u'replacement teacher'),
    )

    def clean(self):
        if (not self.weekday and not self.day) or (self.weekday and self.day):
            raise ValidationError('You must specify either a day or a weekday')
