from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post

def index(request):
    posts = Post.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def agregar(request):
    template = loader.get_template('agregar.html')
    return HttpResponse(template.render({}, request))

def agregarregistro(request):
    titulo = request.POST['title']
    contenido = request.POST['content']
    autor = request.POST['author']
    post = Post(title=titulo, content=contenido, author=autor)
    post.save()
    return HttpResponseRedirect(reverse('index'))

def eliminar(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

def actualizar(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('actualizar.html')
    context = {
        'post':post,
    }
    return HttpResponse(template.render(context, request))

def actualizarregistro(request, id):
    titulo = request.POST['title']
    contenido = request.POST['content']
    autor = request.POST['author']
    post = Post.objects.get(id=id)
    post.title = titulo
    post.content = contenido
    post.author = autor
    post.save()
    return HttpResponseRedirect(reverse('index'))
