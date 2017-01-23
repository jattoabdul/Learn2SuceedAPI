from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from rest_framework import views, viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from learn.serializers import *
from learn.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from learn.permissions import AdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework import generics


# Create your views here.
def index(request):
    context_dict = locals()
    return render(request, "index.html", context_dict)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AdminOrReadOnly,)


class ExamSubjectViewSet(viewsets.ModelViewSet):
    queryset = ExamSubject.objects.all()
    serializer_class = ExamSubjectSerializer
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
    queryset = User.objects.annotate(total_points=Sum('myscores__score')).order_by('-total_points')
    serializer_class = LeadersBoardSerializer
    permission_classes = (IsOwnerOrReadOnly,)
