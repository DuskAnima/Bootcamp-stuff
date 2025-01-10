from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm

def index(request):
    productos = Producto.objects.all().values()
    return render(request, 'productos_del_proyecto/index.html', context={'productos' : productos})

def agregar(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = ProductoForm()
    return render(request, 'productos_del_proyecto/agregar.html', context={'form' : form})

def nombre_usuario(request, cadena):
    cadena = 'juanperez'
    return render(request, 'productos_del_proyecto/username.html', context={'cadena':cadena})

def producto_detalle(request, pk):
    producto = Producto.objects.get(id=pk)  # <--- conviene generar un id indivudal e irrepetible manualmente para no estar dando palos de ciego con la pk autoincremental
    context = {'producto': producto}
    return render(request, 'productos_del_proyecto/detalle.html', context)