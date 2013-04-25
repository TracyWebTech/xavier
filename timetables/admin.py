# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Timetable, Time


class TimetableAdmin(admin.ModelAdmin):
    pass

class TimeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Time, TimeAdmin)
