from django import template
from django.utils import timezone

from attendances.models import AttendanceBook

register = template.Library()


@register.filter
def is_late(student, attendance_book):
    return attendance_book.is_late(student)

@register.filter
def absent_students(classroom, day=None):
    if day is None:
        day = timezone.now()

    n_students = classroom.students.count()
    try:
        attbook = classroom.attendancebook_set.get(day=day)
    except AttendanceBook.DoesNotExist:
        return n_students # all absent

    return n_students - attbook.students.count()

@register.filter
def is_present(student, attendance_book):
    return attendance_book.is_present(student)

@register.filter
def is_absent(student, attendance_book):
    return attendance_book.is_absent(student)

@register.simple_tag(takes_context=True)
def get_student_explanation(context):
    attendance_book = context.get('attendance_book')
    student = context.get('student')
    return attendance_book.get_student_explanation(student)
