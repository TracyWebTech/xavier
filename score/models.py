from django.db import models
from django.utils.translation import ugettext_lazy as _
from classes.models import ClassSubject
from period.models import SubPeriod


class EvaluationCriteria(models.Model):
    name = models.CharField(_('name'), max_length=30)
    weight = models.SmallIntegerField(_('weight'))
    class_subject = models.ForeignKey(ClassSubject)


class Score(models.Model):
    score = models.IntegerField(_('score'))
    criteria = models.ForeignKey(EvaluationCriteria)
    class_subject = models.ForeignKey(ClassSubject)
    subperiod = models.ForeignKey(SubPeriod)
