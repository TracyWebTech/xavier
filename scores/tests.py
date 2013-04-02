# -*- coding:utf-8 -*-

from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import EvaluationCriteria, Score
from accounts.models import Student, Teacher
from classes.models import Grade, Class, ClassSubject
from subjects.models import Subject
from schools.models import School
from periods.models import Period, SubPeriod

from datetime import datetime, timedelta


class ScoresTest(TestCase):
    fixtures = ['tests/subjects.json', 'tests/groups.json']

    def setUp(self):
        birthday = datetime.now().date()

        # Creating users
        self.student1 = Student.objects.create(username='user1',
                                              password='test',
                                              birthday=birthday, gender='M',
                                              code='10')
        self.student2 = Student.objects.create(username='user2',
                                              password='test',
                                              birthday=birthday, gender='M',
                                              code='11')
        self.teacher = Teacher.objects.create(username='user3',
                                              password='test',
                                              birthday=birthday, gender='M')

        # Creating Class and students
        self.school = School.objects.create(name='escolateste')
        self.period = Period.objects.create(name='anual', year='2013-02-02',
                                            school=self.school)
        self.students = Student.objects.all()
        self.grade = Grade.objects.create(name='3 ano',
                                          grade_type='ensino médio')
        self.class1 = Class.objects.create(identification='A',
                                           period=self.period,
                                           grade=self.grade)
        self.class1.students.add(*self.students)

        # Creating class subject
        classroom = self.class1
        subject = Subject.objects.get(pk=1)
        teacher = self.teacher
        self.classubj = ClassSubject.objects.create(classroom=classroom,
                                                    subject=subject,
                                                    teacher=teacher)

    def test_student_score_ok(self):
        criteria = EvaluationCriteria.objects.create(
            name='Prova',
            weight=2,
            class_subject=self.classubj
        )

        start = datetime.now().date()
        end = datetime.now().date() + timedelta(weeks=8)
        subperiod = SubPeriod.objects.create(name='1 bimestre', start=start,
                                             end=end, period=self.period)

        score = Score.objects.create(student=self.student1, score=10,
                                     criteria=criteria, subperiod=subperiod)

        for student in self.students:
            self.assertIn(score.criteria.class_subject.classroom,
                          student.class_set.all())

    def test_student_with_wrong_class(self):
        # creating different class
        period = Period.objects.create(name='anual', year='2013-05-02',
                                       school=self.school)
        students = Student.objects.all()
        grade = Grade.objects.create(name='2 ano',
                                     grade_type='ensino médio')
        classroom = Class.objects.create(identification='B',
                                         period=self.period,
                                         grade=self.grade)

        subject = Subject.objects.get(pk=1)
        teacher = self.teacher
        classubj = ClassSubject.objects.create(classroom=classroom,
                                               subject=subject,
                                               teacher=teacher)

        criteria = EvaluationCriteria.objects.create(
            name='Prova',
            weight=2,
            class_subject=classubj
        )

        start = datetime.now().date()
        end = datetime.now().date() + timedelta(weeks=8)
        subperiod = SubPeriod.objects.create(name='1 bimestre', start=start,
                                             end=end, period=period)

        # It must have the same class, in this case there is not
        # so it should raise a validation error.
        with self.assertRaises(ValidationError):
            Score.objects.create(student=self.student1, score=10,
                                 criteria=criteria,
                                 subperiod=subperiod)
