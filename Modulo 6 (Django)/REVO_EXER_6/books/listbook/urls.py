from django.urls import path
from .views import index, mostrarLibros, ingresarLibros, registro_view

urlpatterns = [
    path('',  index, name='index'),
    path('listbook/', mostrarLibros, name='listbook'),
    path('inputbook/', ingresarLibros, name='inputbook'),
    path('registro/', registro_view, name='registro')
]