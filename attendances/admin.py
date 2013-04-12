# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Attendance, AttendanceBook


class AttendanceAdmin(admin.ModelAdmin):
    pass


class AttendanceBookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceBook, AttendanceBookAdmin)
