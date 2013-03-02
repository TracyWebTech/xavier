from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import PermissionManager
from django.db import models
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from schools.models import School
from subjects.models import Subject


class User(AbstractUser):
    GENDER_OPTIONS = (
        (_('F'), _('Feminino')),
        (_('M'), _('Masculino')),
    )
    birthday = models.DateField(_('birthday'))
    gender = models.CharField(_('gender'), max_length=2,
                              choices=GENDER_OPTIONS)
    school = models.ForeignKey(School, blank=True, null=True)
    REQUIRED_FIELDS = ['email', 'birthday', 'gender']

    def __unicode__(self):
        return self.username


class Student(User):
    code = models.IntegerField(_('code'), unique=True)

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')


class Employee(User):
    degree = models.CharField(_('degree'), max_length=50, blank=True,
                              null=True)

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')


class Teacher(Employee):
    subjects = models.ManyToManyField(Subject)

    class Meta:
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')


@receiver(post_save, sender=Teacher)
def set_teacher_groups(sender, instance, **kwargs):
    default_group_teacher = Group.objects.get(name='Teacher')
    default_group_employee = Group.objects.get(name='Employee')
    instance.groups.add(default_group_teacher, default_group_employee)


@receiver(post_save, sender=Student)
def set_student_group(sender, instance, **kwargs):
    default_group = Group.objects.get(name='Student')
    instance.groups.add(default_group)
