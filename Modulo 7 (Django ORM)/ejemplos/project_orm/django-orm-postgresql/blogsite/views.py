from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

def index(request):
    posts = Post.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))