# -*- coding: utf-8 -*-

from datetime import datetime
from django.test import TestCase

from accounts.models import Student, Teacher
from periods.models import Period
from schools.models import School
from subjects.models import Subject

from .models import Grade, Class, ClassSubject


def users(self):
    birthday = datetime.now().date()

    self.student = Student.objects.create(username='user1', password='test',
                                          birthday=birthday, gender='M',
                                          code='10')
    self.student = Student.objects.create(username='user2', password='test',
                                          birthday=birthday, gender='M',
                                          code='11')
    self.teacher = Teacher.objects.create(username='user3', password='test',
                                          birthday=birthday, gender='M')


def class_hs(self):
    users(self)
    school = School.objects.create(name='escolateste')
    self.period = Period.objects.create(name='anual', year='2013-02-02',
                                        school=school)
    self.students = Student.objects.all()
    self.grade = Grade.objects.create(name='3 ano', grade_type='ensino médio')
    self.class1 = Class.objects.create(identification='A', period=self.period,
                                       grade=self.grade)
    self.class1.students.add(*self.students)


class ClassesTests(TestCase):
    fixtures = ['subjects_for_test.json',
                'groups_for_test.json']

    def test_class_ok(self):
        users(self)
        school = School.objects.create(name='escolateste')
        period = Period.objects.create(name='anual', year='2013-02-02',
                                       school=school)
        students = Student.objects.all()
        grade = Grade.objects.create(name='3 ano', grade_type='ensino médio')
        class1 = Class.objects.create(identification='A', period=period,
                                      grade=grade)
        class1.students.add(*students)

    def test_classsubject_ok(self):
        class_hs(self)
        classroom = self.class1
        subject = Subject.objects.get(pk=1)
        teacher = self.teacher
        classubj = ClassSubject.objects.create(classroom=classroom,
                                               subject=subject,
                                               teacher=teacher)
