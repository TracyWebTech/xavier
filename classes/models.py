from django.db import models
from django.utils.translation import ugettext_lazy as _
from period.models import Period
from accounts.models import Student, Teacher
from subject.models import Subject


class Grade(models.Model):
    name = models.CharField(_('name'), max_length=50)
    grade_type = models.CharField(_('grade type'), max_length=50)


class Class(models.Model):
    identification = models.CharField(_('identification'), max_length=20)
    period = models.ForeignKey(Period)
    students = models.ManyToManyField(Student)
    grade = models.ForeignKey(Grade)


class ClassSubject(models.Model):
    classroom = models.ForeignKey(Class)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
