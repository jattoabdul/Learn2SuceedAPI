from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import views, viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from learn.serializers import *
from learn.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from learn.permissions import AdminOrReadOnly, IsOwnerOrReadOnly


# Create your views here.
def index(request):
    context_dict = locals()
    return render(request, "index.html", context_dict)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AdminOrReadOnly,)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (AdminOrReadOnly,)


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (AdminOrReadOnly,)


class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    permission_classes = (AdminOrReadOnly,)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (AdminOrReadOnly,)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (AdminOrReadOnly,)


class UserScoreViewSet(viewsets.ModelViewSet):
    queryset = UserScore.objects.all()
    serializer_class = UserScoreSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class LeadersBoardViewSet(viewsets.ModelViewSet):
    queryset = LeadersBoard.objects.all()
    serializer_class = LeadersBoardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
