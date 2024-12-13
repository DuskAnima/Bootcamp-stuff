from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime
from .forms import InputForm, WidgetForm, BoardsForm, RegistroUsarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Para gestionar permisos
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import BoardsModel
#Mixins (agregar funciones a una vista existente.)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class Persona(object): 
#En este caso, como estamos trabajando con FBV (Function-Base Views), la clase solo es un constructor que
#luego una función utilizará como parámetro
    def __init__(self, nombre, apellido, login):
        self.nombre = nombre
        self.apellido = apellido
        self.login = login 

class IndexPageView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    login_url = '/login/'
    permission_required = 'boards.view_boardsmodel', 'boards.es_miembro_1'
    template_name = 'index.html'

def logout_view(request):
    logout(request)
    messages.info(request, 'Se ha cerrado la sesión satisfactoriamente.')
    return HttpResponseRedirect(reverse('menu'))

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Iniciaste sesión como {username}.')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Invalido username o password')
        else:
            messages.error(request, 'Invalido username o password')
    else:
        form = AuthenticationForm()
    return render(request=request, template_name='registration/login.html', context={'login_form' : form})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsarioForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(BoardsModel) # Obtenemos el ContentType del modelo 
            #(una suerte de identificador del Modelo que queremos operar)
            es_miembro_1 = Permission.objects.get( # Asignamos a una variable el permiso que queremos otorgar, 
            #pasándole además, el ContentType para poder identificar de esta manera tanto el nombre del permiso
            # como el identificador del modelo que posee este permiso.
                codename = 'es_miembro_1',
                content_type = content_type
            )
            add_boards = Permission.objects.get(
                codename = 'add_boardmodel',
                content_type = content_type
            )
            view_boards = Permission.objects.get(
                codename = 'view_boardmodel',
                content_type = content_type
            )
            user.user_permissions.add(es_miembro_1, add_boards, view_boards)
            user.is_staff = True
            user = form.save()
            login(request, user)
            messages.success(request, 'Registrado Satisfactoriamente.')
            return HttpResponseRedirect(reverse('menu'))
        else: 
            messages.error(request, 'Registro inválido. Algunos datos ingresados no son correctos')
            return render(request=request, template_name='registration/registro.html', context={'register_form' : form})
    else:
        form = RegistroUsarioForm()
    return render(request=request, template_name='registration/registro.html', context={'register_form' : form})

def boardsform_view(request):
    context = {}
    form = BoardsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, 'datosform.html', context)

def widget_view(request):
    context = {}
    form = WidgetForm(request.POST or None)
    context['form'] = form
    return render(request, 'widget_home.html', context)

def datosform_view(request):
    context = {}
    context['form']= InputForm()
    return render(request,'datosform.html', context)

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


