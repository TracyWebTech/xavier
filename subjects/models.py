# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subject(models.Model):
    name = models.CharField(_(u'name'), max_length=30)

    class Meta:
        verbose_name = _(u'subject')
        verbose_name_plural = _(u'subjects')

    def __unicode__(self):
        return self.name
