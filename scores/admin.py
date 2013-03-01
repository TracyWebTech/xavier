from django.contrib import admin
from .models import EvaluationCriteria, Score


class EvaluationCriteriaAdmin(admin.ModelAdmin):
    pass


class ScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(EvaluationCriteria, EvaluationCriteriaAdmin)
admin.site.register(Score, ScoreAdmin)
