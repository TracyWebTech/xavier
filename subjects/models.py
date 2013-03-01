from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subject(models.Model):
    name = models.CharField(_('name'), max_length=30)

    def __unicode__(self):
        return self.name
