
import os

from fabric.api import run, local
from fabric.context_managers import lcd


def make_fixtures():
    path_fixtures = 'fixtures/sample/'
    python_path = '/home/luanp/src/.virtualenvs/schoolproject/bin/python'
    load_cmd = python_path + " manage.py loaddata "
    if os.path.exists(path_fixtures):
        # loading schools
        local(load_cmd + path_fixtures + "1-schools.json")
        # loading periods
        local(load_cmd + path_fixtures + "2-periods.json")
        # loading subjects
        local(load_cmd + path_fixtures + "3-subjects.json")
        # generating users
        local(python_path +
              ' manage.py loadtestdata accounts.User:200')
        local(python_path +
              ' manage.py loadtestdata accounts.Employee:30')
        local(python_path +
              ' manage.py loadtestdata accounts.Teacher:10')
        # separating the student creation in different commands
        # 'cause the loadtestdata can have an integrityerror for unique
        # fields
        local(python_path +
              ' manage.py loadtestdata accounts.Student:50')
        local(python_path +
              ' manage.py loadtestdata accounts.Student:50')
        local(python_path +
              ' manage.py loadtestdata accounts.Student:50')
        # generating classes
        local(python_path + ' manage.py loadtestdata classes.Grade:2')
        local(python_path + ' manage.py loadtestdata classes.Class:2')


def translate():
    dirs = [file for file in os.listdir('.') if os.path.isdir(file)]
    for dir in dirs:
        if os.path.exists(os.path.join(dir, 'locale')):
            with lcd(dir):
                local('django-admin.py compilemessages')
