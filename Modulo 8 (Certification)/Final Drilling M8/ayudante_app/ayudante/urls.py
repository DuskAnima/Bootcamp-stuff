from django.urls import path
from .views import v_index, v_crear_cuenta, v_iniciar_sesion, v_cerrar_sesion, v_mi_cuenta, v_detalle_proveedor, v_cuenta_incluir_servicio, v_cuenta_remover_servicio

urlpatterns = [
    path('', v_index, name='index'),
    path('crear-cuenta/', v_crear_cuenta, name='crear-cuenta'),
    path('iniciar-sesion/', v_iniciar_sesion, name='iniciar-sesion'),
    path('cerrar-sesion/', v_cerrar_sesion, name='cerrar-sesion'),
    path('mi-cuenta/', v_mi_cuenta, name='mi-cuenta'),
    path('proveedor/<str:email>/', v_detalle_proveedor, name='detalle-proveedor'),
    path('mi-cuenta/incluir-servicio/', v_cuenta_incluir_servicio, name='incluir-servicio'),
    path('mi-cuenta/remover-servicio/', v_cuenta_remover_servicio, name='remover-servicio')
]