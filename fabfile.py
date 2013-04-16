#!/usr/bin/env python

import os
import sys
import glob

from fabric.api import run, local
from fabric.contrib import django
from fabric.context_managers import lcd

from django.core import management

DJANGO_PROJECT_NAME = 'xavier'
django.project(DJANGO_PROJECT_NAME)
from django.db.utils import IntegrityError
from classes.models import Class, Period, Grade


LOCAL_CWD_PATH = os.path.abspath(os.path.dirname(__file__))


def ldjango_project(fn):
    def wrapper(*args, **kwargs):
        django.project(DJANGO_PROJECT_NAME)

        if LOCAL_CWD_PATH not in sys.path:
            sys.path.insert(0, LOCAL_CWD_PATH)

        return fn(*args, **kwargs)

    return wrapper


def create_class():
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

def translate():
    dirs = [file for file in os.listdir('.') if os.path.isdir(file)]
    for dir in dirs:
        if os.path.exists(os.path.join(dir, 'locale')):
            with lcd(dir):
                local('django-admin.py makemessages --all')
                local('django-admin.py compilemessages')
