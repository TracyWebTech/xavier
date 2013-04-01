# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Calendar, Break


class CalendarAdmin(admin.ModelAdmin):
    pass


class BreakAdmin(admin.ModelAdmin):
    pass


admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Break, BreakAdmin)
