from django import template

register = template.Library()


@register.filter
def is_late(student, attendance_book):
    return attendance_book.is_late(student)

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
