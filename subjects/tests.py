from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Subject


class SubjectTestCase(TestCase):

    def testSubjectModel(self):
        with self.assertRaises(ValidationError):
            Subject.objects.create(name='Filosofia')
            Subject(name='Filosofia').full_clean()
