from django.urls import path
from .views import index_view, vehiculoadd_view, signup_view, login_view, logout_view, vehiculolist_view

urlpatterns = [
    path('', index_view, name='index'),
    path('vehiculo/add/', vehiculoadd_view, name='vehiculoadd'),
    path('registro/', signup_view, name='signup'),
    path('ingreso/', login_view, name='login'),
    path('salir/', logout_view, name='logout'),
    path('vehiculo/list', vehiculolist_view, name='vehiculolist')
]