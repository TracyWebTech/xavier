
import os

from fabric.api import run, local
from fabric.context_managers import lcd


def translate():
    dirs = [file for file in os.listdir('.') if os.path.isdir(file)]
    for dir in dirs:
        if os.path.exists(os.path.join(dir, 'locale')):
            with lcd(dir):
                local('django-admin.py compilemessages')
