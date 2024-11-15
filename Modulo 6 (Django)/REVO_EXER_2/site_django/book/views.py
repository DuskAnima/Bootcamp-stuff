"""
Texto por defecto:
from django.shortcuts import render

# Create your views here.
"""
"""
Método "normal" de agregar views
from django.http import HttpResponse

def index(request):
    return HttpResponse ("Bienvenido a mi sitio de libros")
"""
# Método "templates"

from django.views.generic import TemplateView

class indexPageView(TemplateView):
    template_name = "index.html"