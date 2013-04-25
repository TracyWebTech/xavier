#!/usr/bin/env python

import os
import sys
import glob
import random

from fabric.api import run, local
from fabric.contrib import django
from fabric.context_managers import lcd

from django.core import management


LOCAL_CWD_PATH = os.path.abspath(os.path.dirname(__file__))
DJANGO_PROJECT_NAME = 'xavier'

NAMES = []

def ldjango_project(fn):
    def wrapper(*args, **kwargs):
        django.project(DJANGO_PROJECT_NAME)

        if LOCAL_CWD_PATH not in sys.path:
            sys.path.insert(0, LOCAL_CWD_PATH)

        return fn(*args, **kwargs)

    return wrapper


def populate_classes():
    from classes.models import Class, Period, Student
    students = list(Student.objects.all())
    classes = Class.objects.all()

    for classroom in classes:
        random.shuffle(students)
        for i in range(20):
            classroom.students.add(students[i])


def get_names():
    global NAMES

    if NAMES:
        return NAMES

    with file(os.path.join(LOCAL_CWD_PATH, 'fixtures', 'names.txt')) as f_names:
        NAMES = f_names.readlines()

    return NAMES


def get_name():
    names = get_names()
    name = random.choice(NAMES)
    names.remove(name)
    return name


def get_user_dict():
    name = get_name()
    username = name.replace(' ', '')[:30]
    first_name, last_name = name.split(' ', 1)
    return {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
    }


def create_teachers():
    from accounts.models import Teacher
    names = get_names()
    for i in range(0, 30):
        user_dict = get_user_dict()
        Teacher.objects.create(
            birthday='1989-02-01',
            gender=random.choice(['M', 'F']),
            school_id=1,
            **user_dict
        )


def create_students():
    from accounts.models import Student
    names = get_names()

    for i in range(0, 100):
        user_dict = get_user_dict()
        Student.objects.create(
            birthday='1989-02-01',
            gender=random.choice(['M', 'F']),
            school_id=1,
            code=i,
            **user_dict
        )

def create_class():
    from classes.models import Class, Period, Grade
    identifications = ["A", "B"]
    periods = Period.objects.all()
    grades = Grade.objects.all()
    for period in periods:
        for grade in grades:
            for identification in identifications:
                classroom = Class.objects.create(
                    identification=identification,
                    period=period,
                    grade=grade
                )


def create_class_subject():
    from subjects.models import Subject
    from classes.models import ClassSubject, Class
    from accounts.models import Teacher

    teachers = list(Teacher.objects.all())
    classes = Class.objects.all()
    subjects = Subject.objects.all()

    for classroom in classes:
        for subject in subjects:
            ClassSubject.objects.create(
                classroom=classroom,
                subject=subject,
                teacher=random.choice(teachers),
            )

def create_eval_criteria():
    from classes.models import ClassSubject, Class
    from scores.models import EvaluationCriteria

    class_subjects = ClassSubject.objects.all()
    for class_subject in class_subjects:
        EvaluationCriteria.objects.create(
            name='Prova 1',
            weight=1,
            class_subject=class_subject
        )
        EvaluationCriteria.objects.create(
            name='Prova 2',
            weight=2,
            class_subject=class_subject
        )
        EvaluationCriteria.objects.create(
            name='Prova 3',
            weight=3,
            class_subject=class_subject
        )
        EvaluationCriteria.objects.create(
            name='Trabalho',
            weight=1,
            class_subject=class_subject
        )


@ldjango_project
def load_testdata():
    from django.db.utils import IntegrityError
    fixt_path = 'fixtures/sample/'

    fixtures = sorted(glob.glob(os.path.join(fixt_path, '*.json')))
    management.call_command('loaddata', *fixtures)

    create_teachers()
    create_students()
    create_class()
    populate_classes()
    create_class_subject()
    create_eval_criteria()

    management.call_command('loaddata', os.path.join(fixt_path, '0-admin.json'))


def translate():
    dirs = [file for file in os.listdir('.') if os.path.isdir(file)]
    for dir in dirs:
        if os.path.exists(os.path.join(dir, 'locale')):
            with lcd(dir):
                local('django-admin.py makemessages --all')
                local('django-admin.py compilemessages')
