# mysite/multimedia/views.py

from django.shortcuts import render

from .models import Post

def index(request):
    posts = Post.objects.all().filter(is_published=True)
    
    context = {
        'site_title':'​ពហុព័ត៌មាន',
        'page_title': 'ទំព័រ​ដើម',
        'items': posts,
        'route': '/',
    }

    return render(request, 'base.html', context)