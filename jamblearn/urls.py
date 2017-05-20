"""jamblearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from learn.views import *

router = routers.DefaultRouter()
router.register(r'exams',  ExamsViewSet,  base_name='ExamsList')
router.register(r'examsubject',  ExamSubjectViewSet,  base_name='Exams')
router.register(r'questions',  QuestionViewSet,  base_name='Questions')
router.register(r'answers',  AnswerViewSet,  base_name='Answers')
router.register(r'scores',  UserScoreViewSet,  base_name='UserScore')
router.register(r'leadersboard',  LeadersBoardViewSet,  base_name='LeadersBoard')

urlpatterns = [
    url(r'', include('learn.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/question/(?P<exam>.+)/(?P<year>.+)/(?P<subject>.+)/$', QuestionList.as_view()),
    url(r'^api/exam/(?P<exam>.+)/$', ExamList.as_view()),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
