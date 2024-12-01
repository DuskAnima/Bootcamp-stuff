from django.urls import path
from .views import index, mostrarLibros

urlpatterns = [
    path('',  index, name='index'),
    path('listbook/', mostrarLibros, name='listbook')
]