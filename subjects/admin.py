from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)
