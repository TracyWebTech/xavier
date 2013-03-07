# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class School(models.Model):
    name = models.CharField(_(u'name'), max_length=50, unique=True)

    class Meta:
        verbose_name = _(u'school')
        verbose_name_plural = _(u'schools')

    def __unicode__(self):
        return self.name
