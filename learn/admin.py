from django.contrib import admin
from learn.models import *


# Register your models here.
class ExamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_display = ['name']


class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_display = ['name']


class YearAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('year_number',)}
    search_fields = ['year_number']
    list_display = ['year_number']


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text', 'subject', 'exam', 'year']
    list_display = ['serial_no', 'question_text', 'is_published', 'exam', 'subject', 'year']
    ordering = ['serial_no']


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['question', 'text']
    list_display = ['question', 'text', 'is_valid']


class UserScoreAdmin(admin.ModelAdmin):
    search_fields = ['user', 'score']
    list_display = ['user', 'exam', 'subject', 'score']


class LeadersBoardAdmin(admin.ModelAdmin):
    search_fields = ['user_exam', 'points']
    list_display = ['user_exam', 'points']
    ordering = ['points']

# Register your models here.
admin.site.register(Exam, ExamAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserScore, UserScoreAdmin)
admin.site.register(LeadersBoard, LeadersBoardAdmin)
