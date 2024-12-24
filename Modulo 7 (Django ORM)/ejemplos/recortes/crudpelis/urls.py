from django.urls import path
from .views import v_categorias, v_categoria_crear, v_categoria_editar, v_categoria_eliminar

urlpatterns = [
    path('index/', v_categorias, name='categorias'),
    path('categoria/crear', v_categoria_crear, name='categorias_crear'),
    path('categoria/editar', v_categoria_editar, name='categorias_editar'),
    path('categoria/eliminar', v_categoria_eliminar, name='categorias_eliminar'),
]

# Luego de la definicón del modelo, creamos las URLS, no olvidar agregar esta carpeta a urls.py 
#del proyecto usando include('<nombre de la app>').

# Lo siguiente es crear las views.