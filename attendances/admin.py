# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import NonAttendance


class NonAttendanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(NonAttendance, NonAttendanceAdmin)
