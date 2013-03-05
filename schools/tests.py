from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import School


class SchoolTests(TestCase):
    def test_school_duplicate(self):
        School.objects.create(name='escolateste')
        with self.assertRaises(ValidationError):
            School.objects.create(name='escolateste')
