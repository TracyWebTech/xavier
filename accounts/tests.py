# -*- coding:utf-8 -*-

from datetime import date
from django.test import TestCase

from schools.models import School
from subjects.models import Subject
from .models import User, Student, Employee, Teacher


class AccountTestCase(TestCase):
    fixtures = ['tests/subjects.json']

    def setUp(self):
        birthday = date.today()
        self.school = School.objects.create(name='escolateste')
        self.user = User.objects.create(
            username='user', password='test',
            birthday=birthday,
            gender='M'
        )
        self.student = Student.objects.create(
            username='student', password='test',
            birthday=birthday,
            gender='M',
            code='10',
            school=self.school
        )
        self.employee = Employee.objects.create(
            username='employee', password='test',
            birthday=birthday,
            gender='M',
            school=self.school
        )
        self.teacher = Teacher.objects.create(
            username='teacher', password='test',
            birthday=birthday,
            gender='M',
            school=self.school
        )

    def testUserModel(self):
        self.assertQuerysetEqual(self.user.groups.all(), [])
        self.assertIsNone(self.user.school)

    def testStudentModel(self):
        self.assertQuerysetEqual(
            self.student.groups.all(),
            ['<Group: Student>']
        )
        self.assertIsNotNone(self.student.school)

    def testEmployeeModel(self):
        self.assertQuerysetEqual(
            self.employee.groups.all(),
            ['<Group: Employee>']
        )
        self.assertIsNotNone(self.student.school)

    def testTeacherModel(self):
        subject = Subject.objects.get(pk=1)
        self.teacher.subjects.add(subject)
        self.assertEqual(self.teacher.subjects.all()[0].name, u'Ingl\xeas')
        self.assertQuerysetEqual(
            self.teacher.groups.all(),
            ['<Group: Teacher>', '<Group: Employee>']
        )
        self.assertIsNotNone(self.teacher.school)
