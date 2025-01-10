from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import RegistroUsuarioForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registrado satisfactoriamente.')
            return HttpResponseRedirect(reverse('crudapp:mostrar'))
        messages.error(request, 'Registro inválido. Algunos datos son incorrectos.')
    form = RegistroUsuarioForm()
    return render(request=request, template_name='registro.html', context = {'register_form' : form})