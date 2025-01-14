from django.urls import path
from .views import insertar_lab, mostrar_lab, editar_lab, actualizarlab, eliminar_lab

urlpatterns = [
    path('', insertar_lab, name='insertar-lab'),
    path('mostrar/', mostrar_lab, name='mostrar-lab'),
    path('editar/<int:id>', editar_lab, name='editar-lab'),
    path('editar/actualizarlab/<int:id>', actualizarlab, name='actualizar-lab'),
    path('eliminar/<int:id>', eliminar_lab, name='eliminar-lab'),
]