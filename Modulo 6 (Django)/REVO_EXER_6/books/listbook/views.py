from django.shortcuts import render
from .forms import InputBookForm, RegistrarUsuarioForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages # Módulo que sirve para desplegar alertas.
from django.contrib.auth import authenticate, login, logout # métodos para sus respectivas acciones.


libros = ['Django 3 Web Development Cookbok Fourth Edition', 'Two Scoops of Django 3.x', 'El libro de Django', 'Python WEb Development with Django', 'Django for Professionals', 'Django for APIs']
autores = ['Aidas Bendoraitis', 'Daniel Feldroy', 'Adrian Holovaty', 'Jeff Forcier', 'William S. Vincent', 'William S. Vincent']
precio = [3250, 1570, 1400, 1375, 2100, 2540]

class Libros():
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self. autor = autor
        self.precio = precio

def registro_view(request):
    if request.method == 'POST': # Si el cliente nos hace una petición con el método POST
        form = RegistrarUsuarioForm(request.POST) #Instanciamos una forma, la cual usará como parametros, los datos capturados del request.
        if form.is_valid(): # True si los datos capturados son válidos bajo las reglas definidas en los campos de formulario
            user = form.save() # Se guarda al usuario
            login(request, user) # Automáticamente el usuario se verá logeado.
            messages.success(request, 'Registrado satisfactoriamente.') # Mensaje de feedback.
            return HttpResponseRedirect(reverse('index')) # Redirecciona automáticamente a Index. Con reverse declaramos el name y no la ruta.
        else:
            messages.error(request, 'Registro inválido. Los datos ingresados no son correctos.') # Mensaje de feedback
            return render(request, 'listbook/registration/registro.html', context = {'register_form' : form}) # En caso de no ser los datos válidos, la vista se volverá a renderizar.
    else:
        form = RegistrarUsuarioForm() 
    return render(request, 'listbook/registration/registro.html', context = {'register_form' : form}) # El contexto se le debe pasar directamente a cada render para evitar conflictos ante las diferentes condicionales.



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