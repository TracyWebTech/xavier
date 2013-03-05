from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Subject


class SimpleTest(TestCase):
    fixtures = ['subjects_for_test.json', ]
    def test_duplicate_subject(self):
        with self.assertRaises(ValidationError):
            Subject.objects.create(name='Geografia')
