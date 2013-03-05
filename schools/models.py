from django.db import models
from django.utils.translation import ugettext_lazy as _


class School(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True)

    def __unicode__(self):
        return self.name
