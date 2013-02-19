from django.contrib import admin
from .models import Period, SubPeriod


class PeriodAdmin(admin.ModelAdmin):
    pass


class SubPeriodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Period, PeriodAdmin)
admin.site.register(SubPeriod, SubPeriodAdmin)
