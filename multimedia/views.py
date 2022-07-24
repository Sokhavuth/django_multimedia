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