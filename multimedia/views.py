# mysite/multimedia/views.py

from django.shortcuts import render

context = {
    'site_title':'Django App',
    'page_title': 'ទំព័រ​ដើម',
}

def index(request):
    return render(request, 'front/home.html', context)