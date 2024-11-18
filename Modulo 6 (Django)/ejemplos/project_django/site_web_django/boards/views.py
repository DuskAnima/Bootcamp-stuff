from django.views.generic import TemplateView
from django.shortcuts import render
import datetime

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