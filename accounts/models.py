from django.db import models
from school.models import School
from subject.models import Subject


class Student(models.Model):
    GENDER_OPTIONS = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )

    code = models.IntegerField()
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    school = models.ForeignKey(School)

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)
