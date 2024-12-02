from django.urls import path, include
from .views import IndexPageView, obtenerFecha, menuView, mostrar, datosform_view, widget_view, boardsform_view, registro_view, login_view, logout_view

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('fecha/<name>', obtenerFecha, name='fecha'),
    path('menu/', menuView, name='menu'),
    path('mostrar/', mostrar, name='mostrar'),
    path('datosform/', datosform_view, name='datosform'),
    path('widgetform', widget_view, name='widgetform'),
    path('boardsform/', boardsform_view, name='boardsform'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]