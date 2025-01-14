from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Proveedor, ProveedorMensaje, Servicio, User
from .forms import ProveedorSignupForm, UserSignupForm


def v_index(request):
    usuarios = User.objects.filter(is_staff=False) # Se aplica filtro para que no muestre a usuarios parte del Staff
    for usuario in usuarios:
        usuario.proveedor = Proveedor.objects.filter(user=usuario).first()
    return render(request, 'ayudante/index.html', context={'usuarios': usuarios})

def v_crear_cuenta(request):
    if request.method == 'POST':
        # Asegúrate de pasar request.FILES para procesar archivos
        user_form = UserSignupForm(request.POST, request.FILES)
        proveedor_form = ProveedorSignupForm(request.POST, request.FILES)

        if user_form.is_valid() and proveedor_form.is_valid():
            with transaction.atomic():
                # Crear el usuario
                user = user_form.save()
                # Crear el proveedor asociado al usuario
                proveedor = proveedor_form.save(commit=False)
                proveedor.user = user
                proveedor.save()
                login(request, user)
            # Redirigir al usuario después del registro
                return redirect(reverse('index'))  # O la vista que desees
    else:
        user_form = UserSignupForm()
        proveedor_form = ProveedorSignupForm()

    return render(request, 'ayudante/signup.html', context={'user_form': user_form, 'proveedor_form': proveedor_form})

def v_iniciar_sesion(request):
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
    return render(request=request, template_name='ayudante/login.html', context={'login_form' : form})

def v_cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Se ha cerrado la sesión satisfactoriamente.')
    return redirect('index')

@login_required
def v_mi_cuenta(request):
    user = request.user
    proveedor = Proveedor.objects.get(user=user)
    
    if request.method == 'POST':
        # Pasar request.FILES para procesar la foto
        user_form = UserSignupForm(request.POST, request.FILES, instance=user)
        proveedor_form = ProveedorSignupForm(request.POST, request.FILES, instance=proveedor)

        if user_form.is_valid() and proveedor_form.is_valid():
            user_form.save()
            proveedor_form.save()
            login(request, user)
            return redirect('index') 
    else:
        user_form = UserSignupForm(instance=user)
        proveedor_form = ProveedorSignupForm(instance=proveedor)

    context = {'user_form': user_form, 'proveedor_form': proveedor_form}
    return render(request, 'ayudante/account.html', context)

def v_detalle_proveedor(request, email):
    # Obtén el usuario basado en el correo electrónico
    user = get_object_or_404(User, email=email)
    # Obtén el proveedor asociado al usuario
    proveedor = get_object_or_404(Proveedor, user=user)
    # Obtener los servicios asociados al proveedor
    servicios = Servicio.objects.filter(proveedorservicio__proveedor=proveedor)
    # Obtener los mensajes asociados al proveedor
    mensajes = ProveedorMensaje.objects.filter(proveedor=proveedor).order_by('-fecha_registro')
    # Contexto para pasar a la plantilla
    context = {
        'usuario': user,
        'proveedor': proveedor,
        'servicios': servicios,  # Lista de servicios
        'mensajes': mensajes,    # Lista de mensajes
    }
    return render(request, 'ayudante/details.html', context)


def v_cuenta_incluir_servicio(request):
    pass

def v_cuenta_remover_servicio(request):
    pass