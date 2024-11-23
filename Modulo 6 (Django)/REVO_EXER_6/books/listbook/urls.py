from django.urls import path
from .views import mostrarLibros

urlpatterns = [
    path('', mostrarLibros, name='listbooks')
]