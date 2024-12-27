from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm

def index(request):
    productos = Producto.objects.all().values()
    return render(request, 'productos_del_proyecto/index.html', 
    context={'productos' : productos})

def agregar(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = ProductoForm()
    return render(request, 'productos_del_proyecto/agregar.html', context={'form' : form})