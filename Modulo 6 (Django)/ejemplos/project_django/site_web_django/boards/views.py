from django.views.generic import TemplateView
from django.shortcuts import render
import datetime
from .forms import InputForm, WidgetForm


class Persona(object): 
#En este caso, como estamos trabajando con FBV (Function-Base Views), la clase solo es un constructor que
#luego una función utilizará como parámetro
    def __init__(self, nombre, apellido, login):
        self.nombre = nombre
        self.apellido = apellido
        self.login = login 

class IndexPageView(TemplateView):
    template_name = "index.html"

def datosform_view(request):
    context = {}
    context['form']= InputForm()
    return render(request,'datosform.html', context)

def widget_view(request):
    context = {}
    form = WidgetForm(request.POST or None)
    context['form'] = form
    return render(request, 'widget_home.html', context)

def obtenerFecha(request, name):
    fechaActual = datetime.datetime.now()
    context = {'fecha' : fechaActual, 'name' : str(name).capitalize}
    return render(request, 'fecha.html', context)

def menuView(request):
    template_name = 'menu.html'
    return render(request, template_name)

def mostrar(request):
    persona = Persona('Juan', 'Pérez', True)
    items = ['Primero', 'Segundo', 'Tercero', 'Cuarto']
    hrs = datetime.datetime.now()
    #items = []
    context = {'nombre' : persona.nombre, 'apellido': persona.apellido, 'login' : persona.login, 'items' : items, 'hora' : hrs}
    return render(request, 'templateexample.html', context)


