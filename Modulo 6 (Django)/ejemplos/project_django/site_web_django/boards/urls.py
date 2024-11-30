from django.urls import path, include
from .views import IndexPageView, obtenerFecha, menuView, mostrar, datosform_view, widget_view

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('fecha/<name>', obtenerFecha, name='fecha'),
    path('menu/', menuView, name='menu'),
    path('mostrar/', mostrar, name='mostrar'),
    path('datosform/', datosform_view, name='datosform'),
    path('widgetform', widget_view, name='widgetform')
]