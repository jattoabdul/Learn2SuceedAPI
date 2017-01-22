from rest_framework import serializers
from learn.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ExamSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamSubject
        fields = ('exam', 'subject', 'year', 'duration')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('question', 'text', 'is_valid')


class QuestionSerializer(serializers.ModelSerializer):
    exam = serializers.ReadOnlyField(source='exam.exam')
    subject = serializers.ReadOnlyField(source='exam.subject')
    year = serializers.ReadOnlyField(source='exam.year')
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['exam', 'subject', 'year', 'id', 'serial_no', 'question_text', 'answers']

    @staticmethod
    def get_answers(obj):
        return [{'id': a.id, 'text': a.text, 'is_valid': a.is_valid} for a in obj.answers.all()]


class UserScoreSerializer(serializers.ModelSerializer):
    exam = serializers.ReadOnlyField(source='exam.exam')
    subject = serializers.ReadOnlyField(source='exam.subject')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserScore
        fields = ('user', 'exam', 'subject', 'score')


class LeadersBoardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user.username')

    class Meta:
        model = LeadersBoard
        fields = ('user', 'points')
