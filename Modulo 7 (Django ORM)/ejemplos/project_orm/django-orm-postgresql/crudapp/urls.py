from django.urls import path
from .views import insertar_emp, mostrar_emp, editar_emp, eliminar_emp, actualizarempleado, empleado_detalle

urlpatterns = [
    path('', insertar_emp, name='insertar-emp'),
    path('mostrar/', mostrar_emp, name='mostrar-emp'),
    path('editar/<int:pk>', editar_emp, name='editar-emp'),
    path('editar/actualizarempleado/<int:id>', actualizarempleado, name='actualizarempleado'),
    path('eliminar/<int:pk>', eliminar_emp, name='eliminar-emp'),
    path('empleado/<int:pk>', empleado_detalle, name='empleado-detalle'),
]
