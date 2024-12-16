from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'


# Clase para registrar usuarios
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User # Modelo de dajngo, por defecto posee user, password1 y password2
        fields = ('username', 'email', 'password1', 'password2') # Se declara el mail para agregarlo

    def save(self, commit=True): 
        user = super(SignupForm, self).save(commit=False) 
        user.email = self.cleaned_data['email'] # Se declara la key que manipulará el valor del email.
        if commit: 
            user.save()
        return user 