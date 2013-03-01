from django.db import models
from django.utils.translation import ugettext_lazy as _
from periods.models import Period
from accounts.models import Student, Teacher
from subjects.models import Subject


class Grade(models.Model):
    name = models.CharField(_('name'), max_length=50)
    grade_type = models.CharField(_('grade type'), max_length=50)

    def __unicode__(self):
        return self.name


class Class(models.Model):
    identification = models.CharField(_('identification'), max_length=20)
    period = models.ForeignKey(Period)
    students = models.ManyToManyField(Student)
    grade = models.ForeignKey(Grade)

    def __unicode__(self):
        return self.grade.name + ' - ' + self.identification


class ClassSubject(models.Model):
    classroom = models.ForeignKey(Class)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)

    def __unicode__(self):
        return unicode(self.classroom)
