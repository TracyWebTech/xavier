from django.contrib import admin
from .models import Grade, Class, ClassSubject


class GradeAdmin(admin.ModelAdmin):
    pass


class ClassAdmin(admin.ModelAdmin):
    pass


class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ['classroom', 'teacher', 'subject']


admin.site.register(Grade, GradeAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(ClassSubject, ClassSubjectAdmin)
