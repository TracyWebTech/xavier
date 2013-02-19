from django.contrib import admin
from .models import Student, Teacher


class StudentAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
