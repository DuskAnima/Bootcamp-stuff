from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proveedor

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class ProveedorSignupForm(forms.ModelForm):
    horarios = forms.CharField(max_length=256, required=True)
    telefono = forms.CharField(max_length=12, required=True)
    descripcion = forms.CharField(max_length=512, required=False)
    foto = forms.ImageField(required=False)

    class Meta:
        model = Proveedor
        fields = ('horarios', 'telefono', 'descripcion', 'foto')