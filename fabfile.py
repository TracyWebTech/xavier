#!/usr/bin/env python

import os
import sys
import glob

from fabric.api import run, local
from fabric.contrib import django
from fabric.context_managers import lcd

from django.core import management


LOCAL_CWD_PATH = os.path.abspath(os.path.dirname(__file__))
DJANGO_PROJECT_NAME = 'xavier'


def ldjango_project(fn):
    def wrapper(*args, **kwargs):
        django.project(DJANGO_PROJECT_NAME)

        if LOCAL_CWD_PATH not in sys.path:
            sys.path.insert(0, LOCAL_CWD_PATH)

        return fn(*args, **kwargs)

    return wrapper


def create_students():
    from classes.models import Class, Period, Student
    from random import shuffle
    students = list(Student.objects.all())
    classes = Class.objects.all()

    for classroom in classes:
        shuffle(students)
        for i in range(20):
            classroom.students.add(students[i])


def create_class():
    from classes.models import Class, Period, Grade
    identifications = ["A", "B", "C"]
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


@ldjango_project
def load_testdata():
    from django.db.utils import IntegrityError
    fixt_path = 'fixtures/sample/'

    fixtures = sorted(glob.glob(os.path.join(fixt_path, '*.json')))
    management.call_command('loaddata', *fixtures)

    while True:
        try:
            management.call_command('loadtestdata',
                                'accounts.User:140', 'accounts.Employee:30',
                                'accounts.Teacher:10', 'accounts.Student:100')
        except IntegrityError: pass
        else: break

    create_class()
    create_students()


def translate():
    dirs = [file for file in os.listdir('.') if os.path.isdir(file)]
    for dir in dirs:
        if os.path.exists(os.path.join(dir, 'locale')):
            with lcd(dir):
                local('django-admin.py makemessages --all')
                local('django-admin.py compilemessages')
