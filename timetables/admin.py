# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Timetable, Time, ClassSubjectTime


class TimetableAdmin(admin.ModelAdmin):
    pass


class TimeAdmin(admin.ModelAdmin):
    pass


class ClassSubjectTimeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(ClassSubjectTime, ClassSubjectTimeAdmin)
