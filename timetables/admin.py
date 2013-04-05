# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Timetable


class TimetableAdmin(admin.ModelAdmin):
    pass


admin.site.register(Timetable, TimetableAdmin)
