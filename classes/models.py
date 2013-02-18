from django.db import models
from period.models import Period
from account.models import Student, Teacher
from subject.models import Subject


class Class(models.Model):
    identification = models.CharField(max_length=20)
    period = models.ForeignKey(Period)
    students = models.ManyToManyField(Student)
    grade = models.ForeignKey(Grade)


class Grade(models.Models):
    name = models.CharField(max_length=50)
    grade_type = models.CharField(max_length=50)


class ClassSubject(models.Model):
    classroom = ForeignKey(Class)
    subject = ForeignKey(Subject)
    teacher = ForeignKey(Teacher)
