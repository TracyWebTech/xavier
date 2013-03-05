from django.db import IntegrityError
from django.test import TestCase
from .models import School


class SchoolTests(TestCase):
    def test_school_duplicate(self):
        School.objects.create(name='escolateste')
        with self.assertRaises(IntegrityError):
            School.objects.create(name='escolateste')
