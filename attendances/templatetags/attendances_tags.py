from django import template

register = template.Library()


@register.filter
def is_late(student, attendance_book):
    return attendance_book.is_late(student)
