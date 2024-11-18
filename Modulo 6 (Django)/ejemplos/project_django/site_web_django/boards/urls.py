from django.urls import path, include
from .views import IndexPageView, obtenerFecha, menuView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('fecha/<name>', obtenerFecha, name='fecha'),
    path('menu/', menuView, name='menu'),
]