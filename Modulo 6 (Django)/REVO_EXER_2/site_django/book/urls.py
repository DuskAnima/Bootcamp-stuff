"""
Método "normal"
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('book', views.index , name='index'),
]
"""
#Método template

from django.urls import path
from . views import indexPageView

urlpatterns = [
    path("", indexPageView.as_view(), name="index"),
]
