from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Laboratorio

def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all()
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1
    context = {'labs': laboratorios, 'visitas': num_visitas}
    return render(request, 'laboratorio/mostrar.html', context)

def insertar_lab(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect(reverse('mostrar-lab'))
    else:
        return render(request, 'laboratorio/insertar.html')

def editar_lab(request, id):
    laboratorio = Laboratorio.objects.get(id=id)
    context = {'lab' : laboratorio}
    return render(request, 'laboratorio/editar.html', context)

def actualizarlab(request, id):
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais = request.POST['pais']
    laboratorio = Laboratorio.objects.get(id=id)
    laboratorio.nombre = nombre
    laboratorio.ciudad = ciudad
    laboratorio.pais = pais
    laboratorio.save()
    return redirect(reverse('mostrar-lab'))

def eliminar_lab(request, id):
    laboratorio = Laboratorio.objects.get(id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect(reverse('mostrar-lab'))
    context = {'lab' : laboratorio}
    return render(request, 'laboratorio/eliminar.html', context)