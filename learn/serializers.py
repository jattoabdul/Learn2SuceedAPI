from rest_framework import serializers
from learn.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Year
        fields = ('year_number',)


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ('name',)


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('name',)


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('text', 'is_valid')


class QuestionSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    year = YearSerializer(read_only=True)
    answer = AnswerSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('exam', 'subject', 'year', 'question_text', 'answer')


class UserScoreSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserScore
        fields = ('user', 'exam', 'subject', 'score')


class LeadersBoardSerializer(serializers.ModelSerializer):
    user_exam = UserScoreSerializer(read_only=True)

    class Meta:
        model = LeadersBoard
        fields = ('user_exam', 'points')
