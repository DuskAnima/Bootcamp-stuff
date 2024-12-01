from django import forms
from .models import InputBookModel
from django.core.exceptions import ValidationError

class InputBookForm(forms.ModelForm):
    class Meta:
        model = InputBookModel
        fields = '__all__'
    
    def clean_valoracion(self):
        valoracion = self.cleaned_data.get('valoracion')
        if valoracion < 0 or valoracion > 10000:
            raise ValidationError('Ingrese un valor entre 0 y 10.000')
        return valoracion
    