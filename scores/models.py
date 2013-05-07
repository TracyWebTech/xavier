# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


# TODO Change modeling of criterias
class EvaluationCriteria(models.Model):
    name = models.CharField(_(u'name'), max_length=30)
    weight = models.SmallIntegerField(_(u'weight'))
    class_subject = models.ForeignKey("classes.ClassSubject",
                                      verbose_name=_(u'class subject'))

    class Meta:
        unique_together = ('name', 'weight', 'class_subject')
        verbose_name = _(u'evaluation criteria')
        verbose_name_plural = _(u'evaluation criterias')

    def __unicode__(self):
        return self.name


class Score(models.Model):
    student = models.ForeignKey("accounts.Student", verbose_name=_(u'student'))
    score = models.SmallIntegerField(_(u'score'))
    criteria = models.ForeignKey("scores.EvaluationCriteria",
                                 verbose_name=_(u'criteria'))
    subperiod = models.ForeignKey("periods.SubPeriod", verbose_name=_(u'subperiod'))

    class Meta:
        unique_together = ('student', 'criteria', 'subperiod')
        verbose_name = _(u'score')
        verbose_name_plural = _(u'scores')

    def save(self, *args, **kwargs):
        student_classes = self.student.class_set.all()
        criteria_class = self.criteria.class_subject.classroom
        if criteria_class not in student_classes:
            raise ValidationError(
                _("Student not in the class of given criteria")
            )
        super(Score, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.score)
