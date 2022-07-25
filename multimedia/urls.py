# mysite/multimedia/urls.py

from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<post_id>', views.post, name='post'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]