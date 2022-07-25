# mysite/multimedia/views.py

import json
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer

from .models import Post
from .config import Config

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().filter(is_published='yes')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def index(request):
    posts = Post.objects.all().filter(is_published='yes')

    Config.context['page_title'] = 'ទំព័រ​ដើម'
    Config.context['posts'] = posts
    Config.context['route'] = ''
    
    return render(request, 'base.html', Config.context)

def post(request, post_id):
    post = Post.objects.get(post_id=post_id)
    print(post)
    if post.video.values():
        result = post.video.values()      
        videos = [entry for entry in result]

        for entry in videos:
            entry.pop("created_at")

        videos = json.dumps(videos)
        Config.context['videos'] = videos
    else:
        Config.context['videos'] = False
    
    Config.context['page_title'] = 'ទំព័រ​​​​​​​​អត្ថបទ'
    Config.context['post'] = post
    Config.context['route'] = 'post'

    return render(request, 'base.html', Config.context)