# coding=utf-8
from django.contrib import admin
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    # количество пустых строк добавлеямых после существующих Choice-ов
    extra = 1


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):

    search_fields = ['question_text']

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
