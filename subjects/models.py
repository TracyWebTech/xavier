# -*- coding: utf-8 -*-

from django.utils.text import slugify
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subject(models.Model):
    name = models.CharField(_(u'name'), max_length=30, unique=True)
    slug = models.SlugField(max_length=30, null=True, unique=True)

    class Meta:
        verbose_name = _(u'subject')
        verbose_name_plural = _(u'subjects')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self))
        super(Subject, self).save(*args, **kwargs)
