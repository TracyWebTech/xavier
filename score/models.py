from django.db import models
from classes.models import ClassSubject
from period.models import SubPeriod


class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=30)
    weight = models.SmallIntegerField()
    class_subject = models.ForeignKey(ClassSubject)


class Score(models.Model):
    score = models.IntegerField()
    criteria = models.ForeignKey(EvaluationCriteria)
    class_subject = models.ForeignKey(ClassSubject)
    subperiod = models.ForeignKey(SubPeriod)
