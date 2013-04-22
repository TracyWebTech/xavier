# -*- coding: utf-8 -*-

from django.utils.text import slugify
from django.db import models
from django.utils.translation import ugettext_lazy as _

from schools import managers


class School(models.Model):
    name = models.CharField(_(u'name'), max_length=64)
    short_name = models.CharField(_(u'short name'), max_length=32)
    hostname = models.CharField(_('host name'), max_length=128, unique=True)
    slug = models.SlugField(max_length=50, null=True)

    objects = managers.SchoolManager()

    class Meta:
        verbose_name = _(u'school')
        verbose_name_plural = _(u'schools')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self.short_name))
        super(School, self).save(*args, **kwargs)
