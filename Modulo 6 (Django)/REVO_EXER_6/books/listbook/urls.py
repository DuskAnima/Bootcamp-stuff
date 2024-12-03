from django.urls import path
from .views import index, mostrarLibros, ingresarLibros, registro_view, login_view, logout_view

urlpatterns = [
    path('',  index, name='index'),
    path('listbook/', mostrarLibros, name='listbook'),
    path('inputbook/', ingresarLibros, name='inputbook'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]