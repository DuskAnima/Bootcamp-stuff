from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'f_vencimiento',]
        labels = {
            'nombre': 'Nombre del Producto',
            'f_vencimiento': 'Fecha de Vencimiento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-class',
                'placeholder': 'Ingrese el nombre del producto',
            }),
            'precio': forms.TextInput(attrs={
                'class': 'form-class',
                'placeholder': 'Precio del producto',
            }),
            'descripción': forms.TextInput(attrs={
                'class': 'form-class',
                'placeholder': 'Descripción del producto'
            }),
            'f_vencimiento': forms.DateInput(attrs= {
                'class': 'form-class',
                'type': 'date',
            }),
        }
