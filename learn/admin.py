from django.contrib import admin
from learn.models import *


# Register your models here.
class ExamSubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('exam', 'subject', 'year')}
    search_fields = ['exam', 'subject', 'year']
    list_display = ['exam', 'year', 'subject', 'duration']


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text', 'exam']
    list_display = ['serial_no', 'question_text', 'is_published', 'exam']
    ordering = ['serial_no']


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['question', 'text']
    list_display = ['question', 'text', 'is_valid']


class UserScoreAdmin(admin.ModelAdmin):
    search_fields = ['user', 'exam', 'score']
    list_display = ['user', 'exam', 'score']
    ordering = ['created_on']


class LeadersBoardAdmin(admin.ModelAdmin):
    search_fields = ['user_exam', 'points']
    list_display = ['user_exam', 'points']
    ordering = ['points']

# Register your models here.
admin.site.register(ExamSubject, ExamSubjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserScore, UserScoreAdmin)
admin.site.register(LeadersBoard, LeadersBoardAdmin)
