from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from .forms import VehiculoForm, SignupForm
from .models import Vehiculo

def index_view(request):
    return render(request, 'vehiculo/index.html')

def vehiculoadd_view(request):
    form = VehiculoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.info(request, 'La información ha sido ingresada exitosamente.')
        return redirect('vehiculoadd')
    else:
        if request.method == 'POST':
            messages.error(request, 'La información ingresada es erronea, revise los campos y vuelva a intentar.')
    return render(request, 'vehiculo/vehiculoadd.html', context={'form' : form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            content_type = ContentType.objects.get_for_model(Vehiculo) #Obtenemos el modelo que maneja los permisos
            visualizar_catalogo = Permission.objects.get( # Declaramos el permiso que queremos asignar
                codename = 'visualizar_catalogo',
                content_type = content_type
            )
            user.user_permissions.add(visualizar_catalogo)
            login(request, user)
            messages.success(request, 'Registrado satisfactoriamente.')
            return redirect('index')
        else:
            messages.error(request, 'Registro inválido. Los datos ingresados no son correctos.')
    else:
        form = SignupForm() 
    return render(request, 'vehiculo/registration/signup.html', context = {'signup_form' : form}) 

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)
                messages.info(request, f'Iniciaste sesión como {username}.')
                return redirect('index')
            else:
                messages.error(request, 'Datos inválidos, intentelo de nuevo.')
        else:
            messages.error(request, 'Datos inválidos, intentelo de nuevo.')
    else:
        form = AuthenticationForm()
    return render(request=request, template_name='vehiculo/registration/login.html', context={'login_form' : form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Se ha cerrado la sesión satisfactoriamente.')
    return redirect('index')

def vehiculolist_view(request):
    lista_vehiculos = Vehiculo.objects.all()
    context = {'vehiculos' : lista_vehiculos}
    return render(request, 'vehiculo/vehiculolist.html', context)