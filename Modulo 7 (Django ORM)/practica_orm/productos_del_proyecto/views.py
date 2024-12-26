from django.shortcuts import render
from .models import Producto

def index(request):
    productos = Producto().objects.all().values()
    return render(request, 'productos_del_proyecto/index.html', context={'productos' : productos})