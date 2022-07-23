# mysite/mysite/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('multimedia.urls')),
    path('admin/', admin.site.urls),
]