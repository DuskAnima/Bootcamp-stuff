from django.shortcuts import render
from .forms import InputBookForm
from django.http import HttpResponseRedirect
from django.urls import reverse

libros = ['Django 3 Web Development Cookbok Fourth Edition', 'Two Scoops of Django 3.x', 'El libro de Django', 'Python WEb Development with Django', 'Django for Professionals', 'Django for APIs']
autores = ['Aidas Bendoraitis', 'Daniel Feldroy', 'Adrian Holovaty', 'Jeff Forcier', 'William S. Vincent', 'William S. Vincent']
precio = [3250, 1570, 1400, 1375, 2100, 2540]

class Libros():
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self. autor = autor
        self.precio = precio

def ingresarLibros(request):
    context = {}
    form = InputBookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('inputbook')) #Falta declarar el nombre de la url
    context['form'] = form
    return render(request, 'listbook/inputbook.html', context)

def mostrarLibros(request):
    lista_libros = []
    for i in range(len(libros)):
        libro = Libros(libros[i], autores[i], precio[i])
        lista_libros.append(libro)
    context = {'libros' : lista_libros}
    return render(request, 'listbook/listbook.html', context)

def index(request):
    return render(request, 'listbook/index.html')