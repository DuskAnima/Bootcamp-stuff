from django.shortcuts import render
from .forms import InputBookForm, RegistrarUsuarioForm
from .models import InputBookModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages # Módulo que sirve para desplegar alertas.
from django.contrib.auth import authenticate, login, logout # métodos para sus respectivas acciones.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


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
            content_type = ContentType.objects.get_for_model(InputBookModel) # Obtenemos el modelo del cual queremos adquirir el permiso
            development = Permission.objects.get( # Declaramos el permiso que queremos asignar
                codename = 'development',
                content_type = content_type
            )
            user = form.save() # Se guarda al usuario
            user.user_permissions.add(development) # Al usuario guardado se le asigna el respectivo permiso
            login(request, user) # Automáticamente el usuario se verá logeado.
            messages.success(request, 'Registrado satisfactoriamente.') # Mensaje de feedback.
            return HttpResponseRedirect(reverse('index')) # Redirecciona automáticamente a Index. Con reverse declaramos el name y no la ruta.
        else:
            messages.error(request, 'Registro inválido. Los datos ingresados no son correctos.') # Mensaje de feedback
            return render(request, 'listbook/registration/registro.html', context = {'register_form' : form}) # En caso de no ser los datos válidos, la vista se volverá a renderizar.
    else:
        form = RegistrarUsuarioForm() 
    return render(request, 'listbook/registration/registro.html', context = {'register_form' : form}) # El contexto se le debe pasar directamente a cada render para evitar conflictos ante las diferentes condicionales.

def login_view(request):
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST) # Consultar sobre por qué aquí los parametros son diferentes
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)
                messages.info(request, f'Iniciaste sesión como {username}.')
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, 'Invalido username o password')
        else:
            messages.error(request, 'Invalido username o password')
    else:
        form = AuthenticationForm()
    return render(request=request, template_name='listbook/registration/login.html', context={'login_form' : form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Se ha cerrado la sesión satisfactoriamente.')
    return HttpResponseRedirect(reverse('index'))

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