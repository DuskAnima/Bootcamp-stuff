from django.urls import path
from .views import index, agregar, nombre_usuario, producto_detalle

urlpatterns = [
    path('', index, name='index'),
    path('agregar/', agregar, name='agregar'),
    path('username/<str:cadena>', nombre_usuario, name='username'),
    path('<int:pk>/', producto_detalle, name='mostrar')
]