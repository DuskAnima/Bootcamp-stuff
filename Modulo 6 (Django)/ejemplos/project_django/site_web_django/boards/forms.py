#Librería estándar de Django
from django import forms
from .models import BoardsModel

#Creación de un forms
class InputForm(forms.Form):
    nombres = forms.CharField(max_length = 200)
    apellidos = forms.CharField(max_length = 200)
    prioridad = forms.IntegerField(min_value=1, max_value=3)
    contrasenia = forms.CharField(widget = forms.PasswordInput())

class WidgetForm(forms.Form):
    # Se puede alterar la forma de los widgets pero estos siguen requiriendo el mismo tipo de input establecido
    # en el principio de la declaración.
    nombre = forms.CharField()
    apellido = forms.CharField()
    prioridad = forms.IntegerField()
    habilitado = forms.BooleanField()
    date = forms.DateField(widget=forms.SelectDateWidget)

#Primero se crea un Form y se le hereda forms.ModelForm
class BoardsForm(forms.ModelForm):
    # Luego se le especifica el modelo a utilizar
    class Meta:
        model = BoardsModel
        fields = "__all__"