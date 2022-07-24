# mysite/multimedia/views.py

from django.shortcuts import render
import json

from .models import Post
from .config import Config

def index(request):
    posts = Post.objects.all().filter(is_published='yes')

    Config.context['page_title'] = 'ទំព័រ​ដើម'
    Config.context['posts'] = posts
    Config.context['route'] = ''
    
    return render(request, 'base.html', Config.context)

def post(request, id):
    post = Post.objects.get(id=id)

    if post.video:
        result = post.video.values()      
        videos = [entry for entry in result]

        for entry in videos:
            entry.pop("created_at")

        videos = json.dumps(videos)
    
    Config.context['page_title'] = 'ទំព័រ​​​​​​​​អត្ថបទ'
    Config.context['post'] = post
    Config.context['videos'] = videos
    Config.context['route'] = 'post'

    return render(request, 'base.html', Config.context)