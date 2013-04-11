# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


SCHOOL_CACHE = {}


class SchoolManager(models.Manager):

    def get_current(self, request):
        """
        Returns the current ``School`` based on the ``request.get_host()``.
        The ``School`` object is cached the first time it's retrieved from
        the database.

        """
        hostname = request.get_host().split(':')[0]
        try:
            current_school = SCHOOL_CACHE[hostname]
        except KeyError:
            try:
                current_school = self.get(hostname=hostname)
            except School.DoesNotExist:
                current_school = self.get(pk=1)
            SCHOOL_CACHE[hostname] = current_school
        return current_school

    def clear_cache(self):
        """Clears the ``School`` object cache."""
        global SITE_CACHE
        SITE_CACHE = {}


class School(models.Model):
    name = models.CharField(_(u'name'), max_length=64)
    short_name = models.CharField(_(u'short name'), max_length=32)
    hostname = models.CharField(_('host name'), max_length=128, unique=True)

    objects = SchoolManager()

    class Meta:
        verbose_name = _(u'school')
        verbose_name_plural = _(u'schools')

    def __unicode__(self):
        return self.name
