from django.views.generic import TemplateView
from django.shortcuts import render
import datetime


#En este caso, como estamos trabajando con FBV (Function-Base Views), la clase solo es un constructor que
#luego una función utilizará como parámetro
class Persona(object): 
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def mostrar(request):
    persona = Persona('Juan', 'Pérez')
    items = ['Primero', 'Segundo', 'Tercero', 'Cuarto']
    context = {'nombre' : persona.nombre, 'apellido': persona.apellido, 'items' : items}
    return render(request, 'templateexample.html', context)

class IndexPageView(TemplateView):
    template_name = "index.html"

def obtenerFecha(request, name):
    fechaActual = datetime.datetime.now()
    context = {'fecha' : fechaActual, 'name' : str(name).capitalize}
    return render(request, 'fecha.html', context)

def menuView(request):
    template_name = 'menu.html'
    return render(request, template_name)

"""from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Mensaje, Hola mundo.")

"""