#!/usr/bin/env python

import os
import sys
import glob

from fabric.api import run, local
from fabric.contrib import django
from fabric.context_managers import lcd

from django.core import management


DJANGO_PROJECT_NAME = 'xavier'
LOCAL_CWD_PATH = os.path.abspath(os.path.dirname(__file__))


def ldjango_project(fn):
    def wrapper(*args, **kwargs):
        django.project('xavier')

        if LOCAL_CWD_PATH not in sys.path:
            sys.path.insert(0, LOCAL_CWD_PATH)

        return fn(*args, **kwargs)

    return wrapper

@ldjango_project
def load_testdata():
    fixt_path = 'fixtures/sample/'

    fixtures = sorted(glob.glob(os.path.join(fixt_path, '*.json')))
    management.call_command('loaddata', *fixtures)

    management.call_command('loadtestdata', 'accounts.User:200')
    #    local(python_path +
    #          ' manage.py loadtestdata accounts.User:200')
    #    local(python_path +
    #          ' manage.py loadtestdata accounts.Employee:30')
    #    local(python_path +
    #          ' manage.py loadtestdata accounts.Teacher:10')
    #    # separating the student creation in different commands
    #    # 'cause the loadtestdata can have an integrityerror for unique
    #    # fields
    #    local(python_path +
    #          ' manage.py loadtestdata accounts.Student:50')
    #    #local(python_path +
    #    #      ' manage.py loadtestdata accounts.Student:50')
    #    #local(python_path +
    #    #      ' manage.py loadtestdata accounts.Student:50')
    #    # generating classes
    #    local(python_path + ' manage.py loadtestdata classes.Grade:2')
    #    local(python_path + ' manage.py loadtestdata classes.Class:2')


def translate():
    dirs = [file for file in os.listdir('.') if os.path.isdir(file)]
    for dir in dirs:
        if os.path.exists(os.path.join(dir, 'locale')):
            with lcd(dir):
                local('django-admin.py compilemessages')
