# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from accounts.models import Student, Teacher
from periods.models import Period
from subjects.models import Subject
from schools.managers import CurrentSchoolManager
from timetables.models import Timetable


class Grade(models.Model):
    name = models.CharField(_(u'name'), max_length=50)
    grade_type = models.CharField(_(u'grade type'), max_length=50)

    class Meta:
        ordering = ['grade_type', 'name']
        unique_together = ('name', 'grade_type')
        verbose_name = _(u'grade')
        verbose_name_plural = _(u'grades')

    def __unicode__(self):
        return self.name


class Class(models.Model):
    identification = models.CharField(
        _(u'identification'),
        max_length=20,
        blank=True
    )
    period = models.ForeignKey(Period, verbose_name=_(u'period'))
    students = models.ManyToManyField(Student, verbose_name=_(u'students'))
    grade = models.ForeignKey(Grade, verbose_name=_(u'grade'))
    timetable = models.ForeignKey(Timetable, verbose_name=_('timetable'),
                                  null=True)
    slug = models.SlugField(max_length=70, null=True, unique=True)

    objects = models.Manager()
    on_school = CurrentSchoolManager(school_field='period__school')

    class Meta:
        ordering = ['period', 'grade', 'identification']
        unique_together = ('identification', 'period', 'grade')
        verbose_name = _(u'class')
        verbose_name_plural = _(u'classes')

    def __unicode__(self):
        return u'{0} - {1}, {2}'.format(self.grade.name, self.identification,
                                        self.period.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self))
        super(Class, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('class-detail', None, {'pk': self.pk})


class ClassSubject(models.Model):
    classroom = models.ForeignKey(Class, verbose_name=_(u'classroom'))
    subject = models.ForeignKey(Subject, verbose_name=_(u'subject'))
    teacher = models.ForeignKey(Teacher, verbose_name=_(u'teacher'))
    slug = models.SlugField(max_length=70, null=True, unique=True)

    objects = models.Manager()
    on_school = CurrentSchoolManager(school_field='classroom__period__school')

    class Meta:
        # TODO It should be class, subject and teacher
        unique_together = ('classroom', 'subject')
        verbose_name = _(u'class subject')
        verbose_name_plural = _(u'class subjects')

    def __unicode__(self):
        return u'{0} ({1})'.format(unicode(self.classroom), self.subject)

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self))
        super(ClassSubject, self).save(*args, **kwargs)
