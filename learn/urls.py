from django.conf.urls import url, include
from learn import views as learn_views

urlpatterns = [
    url(r'^$', learn_views.index, name='index'),
]
