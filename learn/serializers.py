from rest_framework import filters
from rest_framework import serializers, fields
from learn.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ExamsSerializer(serializers.HyperlinkedModelSerializer):
    subjects = fields.MultipleChoiceField(choices=MY_CHOICES)

    class Meta:
        model = Exams
        fields = ('name', 'logoUrl', 'subjects', 'startDate', 'stopDate')


class ExamSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamSubject
        fields = ('exam', 'subject', 'year', 'duration')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('question', 'text')


class QuestionSerializer(serializers.ModelSerializer):
    exam = serializers.ReadOnlyField(source='exam.exam')
    subject = serializers.ReadOnlyField(source='exam.subject')
    year = serializers.ReadOnlyField(source='exam.year')
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['exam', 'subject', 'year', 'id', 'serial_no', 'question_text',  'answers', 'correct']

    @staticmethod
    def get_answers(obj):
        return obj.answers.values('text')


class UserScoreSerializer(serializers.ModelSerializer):
    exam = serializers.ReadOnlyField(source='exam.exam')
    subject = serializers.ReadOnlyField(source='exam.subject')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserScore
        fields = ('user', 'exam', 'subject', 'score')


class LeadersBoardSerializer(serializers.ModelSerializer):
    total_points = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('username', 'total_points')
        ordering = ('-total_points',)

