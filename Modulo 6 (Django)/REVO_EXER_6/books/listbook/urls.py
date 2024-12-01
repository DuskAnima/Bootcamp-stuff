from django.urls import path
from .views import index, mostrarLibros, ingresarLibros

urlpatterns = [
    path('',  index, name='index'),
    path('listbook/', mostrarLibros, name='listbook'),
    path('inputbook/', ingresarLibros, name='inputbook'),
]