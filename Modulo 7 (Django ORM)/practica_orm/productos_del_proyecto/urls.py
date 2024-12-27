from django.urls import path
from .views import index, agregar

urlpatterns = [
    path('', index, name='index'),
    path('agregar/', agregar, name='agregar'),
]