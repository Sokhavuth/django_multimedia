# mysite/multimedia/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<id>', views.post, name='post'),
]