from django import template

register = template.Library()


@register.filter
def is_attendee(student, attendance_book):
    return attendance_book.is_attendee(student)
