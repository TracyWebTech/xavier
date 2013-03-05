# -*- coding:utf-8 -*-

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from .models import User, Student, Employee, Teacher
from schools.models import School
from subjects.models import Subject
from datetime import datetime


def users(self):
    birthday = datetime.now().date()
    self.school = School.objects.create(name='escolateste')

    self.user = User.objects.create(username='user', password='test',
                                    birthday=birthday, gender='M')
    self.student = Student.objects.create(username='user1', password='test',
                                          birthday=birthday, gender='M',
                                          code='10', school=self.school)
    self.employee = Employee.objects.create(username='user2',
                                            password='test', birthday=birthday,
                                            gender='M')
    self.teacher = Teacher.objects.create(username='user3', password='test',
                                          birthday=birthday, gender='M')


class AccountTests(TestCase):
    fixtures = ['subjects_for_test.json',
                'groups_for_test.json']

    def test_users(self):
        users(self)
        self.assertEqual(self.user.username, 'user')
        self.assertEqual(self.student.code, '10')
        self.assertEqual(self.employee.username, 'user2')
        self.assertEqual(self.teacher.username, 'user3')

    def test_teacher_ok(self):
        users(self)
        subject = Subject.objects.get(pk=1)
        self.teacher.subjects.add(subject)
        self.assertEqual(self.teacher.subjects.all()[0].name, u'Ingl\xeas')
        self.assertQuerysetEqual(self.teacher.groups.all(),
                                 ['<Group: Teacher>', '<Group: Employee>'])
        self.assertIsNotNone(self.teacher.school)

    def test_student_ok(self):
        users(self)
        self.assertQuerysetEqual(self.student.groups.all(),
                                 ['<Group: Student>'])
        self.assertIsNotNone(self.student.school)

    def test_student_duplicated_code_school(self):
        users(self)
        birthday = datetime.now().date()
        with self.assertRaises(ValidationError):
            self.student = Student.objects.create(username='userduplicated',
                                                  password='test',
                                                  birthday=birthday,
                                                  gender='M', code='10',
                                                  school=self.school)

    def test_employee_ok(self):
        users(self)
        self.assertQuerysetEqual(self.employee.groups.all(),
                                 ['<Group: Employee>'])
