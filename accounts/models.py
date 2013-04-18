# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from schools.models import School
from subjects.models import Subject


class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'birthday', 'gender']
    GENDER_OPTIONS = (
        (_(u'F'), _(u'Female')),
        (_(u'M'), _(u'Male')),
    )

    birthday = models.DateField(_(u'birthday'), null=True)
    gender = models.CharField(
        _(u'gender'),
        max_length=2,
        choices=GENDER_OPTIONS
    )
    school = models.ForeignKey(School, null=True, verbose_name=_(u'school'))

    class Meta:
        verbose_name = _(u'user')
        verbose_name_plural = _(u'users')

    def __unicode__(self):
        return self.username


class Student(User):
    code = models.IntegerField(_(u'code'), unique=True)

    class Meta:
        verbose_name = _(u'student')
        verbose_name_plural = _(u'students')

    def get_scores(self, subperiod_id, class_subject=None):
        scores = self.score_set.filter(subperiod_id=subperiod_id)
        if class_subject:
            scores = scores.filter(criteria__class_subject=class_subject)
        return scores

    def get_average(self, subperiod_id, class_subject=None):
        # TODO subject = None it works just when a class subject is given
        scores = self.get_scores(subperiod_id, class_subject)
        if not scores:
            return None

        class_subject = scores[0].criteria.class_subject
        criterias = class_subject.evaluationcriteria_set.all()
        score_sum_product = 0.0
        weight_sum = 0.0
        for criteria in criterias:
            for score in scores:
                if score.criteria == criteria:
                    score_sum_product += score.score * score.criteria.weight
                    break
            weight_sum += score.criteria.weight
        return round(float(score_sum_product / weight_sum), 1)


class Employee(User):
    degree = models.CharField(
        _(u'degree'),
        max_length=50,
        null=True, blank=True,
    )

    class Meta:
        verbose_name = _(u'employee')
        verbose_name_plural = _(u'employees')


class Teacher(Employee):
    subjects = models.ManyToManyField(Subject, verbose_name=_(u'subjects'))

    class Meta:
        verbose_name = _(u'teacher')
        verbose_name_plural = _(u'teachers')


@receiver(post_save, sender=Teacher)
def set_teacher_groups(sender, instance, **kwargs):
    default_group_teacher = Group.objects.get(name='Teacher')
    default_group_employee = Group.objects.get(name='Employee')
    instance.groups.add(default_group_teacher, default_group_employee)

@receiver(post_save, sender=Student)
def set_student_group(sender, instance, **kwargs):
    default_group = Group.objects.get(name='Student')
    instance.groups.add(default_group)

@receiver(post_save, sender=Employee)
def set_employee_group(sender, instance, **kwargs):
    default_group = Group.objects.get(name='Employee')
    instance.groups.add(default_group)
