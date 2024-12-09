from django import forms
from .models import InputBookModel
from django.core.exceptions import ValidationError
# Librerías para crear un sign in
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Clase para registrar usuario
class RegistrarUsuarioForm(UserCreationForm):
    #Aquí se declaran los campos que se quieren agregar al form que se creará
    email = forms.CharField(required=True)

    class Meta: # Se requiere declarar la clase meta con las siguientes convenciones
        model = User # Usuarios manejados con el sistema de autenticación de django. Por defecto posee user, password1 y password2
        fields = ('username', 'email', 'password1', 'password2') # Tupla en la que se declaran los campos que poseerá la forma

    def save(self, commit=True): #Se declara la función para guardar usuarios
        user = super(RegistrarUsuarioForm, self).save(commit=False) #Se instancia de manera recursiva el formulario. Al declarar
        # commit=False, nos aseguramos de que se guarde en memoria para poder manipular los valores sin que se guarden aun en la DB.
        user.email = self.cleaned_data['email'] # Se declara la key que manipulará el valor del email.
        if commit: # Este condicional nos asegura de que la información se guardará si llamamos a la función save()
            user.save()
        return user # Esta linea nos asegura poder manipular los datos del usuario, estén guardados o no.

"""
> django.contrib.auth.forms import UserCreationForm
    Lo que hace es importar un grupo de elementos de front-end que trabajarán como un Form el cual django
    posee pre configurado.
> django.contrib.auth.models import User
    Lo que hace es importar un model que Django posee integrado por defecto, el cual nosotros podemos instanciar
    y alterar a gusto. Por defecto maneja los tributos de username, password1 y password2.
> El proceso para crear un form de sign up se estructura combinando estas dos clases, primero creando la clase
    que heredará la form, la cual podremos alterar agregando nuevos atributos.
    > Luego establecemos la clase meta para poder declarar el modelo que importamos, User y los campos que va
        a manejar la form.
    > Finalmente declaramos un método save() que va a instanciar recursivamente a la clase contenedora para
        utilizar el interior de este metodo tanto para poder "sincronizar" los datos de la Form y el Model
        como para poder guardar los elementos en una base de datos si se llama a la función.
    > También cabe destacar que el return del user nos interesa porque de esta manera podremos manipular los datos
        de la instancia en la vista.
"""

class InputBookForm(forms.ModelForm):
    class Meta:
        model = InputBookModel
        fields = '__all__'
    
    def clean_valoracion(self):
        valoracion = self.cleaned_data['valoracion']
        if valoracion > 10000 or valoracion < 1:
            raise forms.ValidationError("Ingrese una valoración entre 1 y 10.000")
        return valoracion
    