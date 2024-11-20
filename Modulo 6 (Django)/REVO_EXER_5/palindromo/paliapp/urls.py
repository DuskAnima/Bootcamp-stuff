from django.urls import path
from .views import palindromo

urlpatterns = [
    path('', palindromo, name='palindromo'),
]