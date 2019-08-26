from django.contrib import admin

from .models import Question, Reponses, Questionnaire


class ReponsesInline(admin.TabularInline):
    model = Reponses


class QuestionAdmin(admin.ModelAdmin):
    # list_display = ('enonce',)
    inlines = [
        ReponsesInline,
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Questionnaire)

# Register your models here.
