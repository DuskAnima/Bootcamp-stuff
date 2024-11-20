from django.urls import path
from .views import palindromo

urlpatterns = [
    path('<palabra>', palindromo, name='palindromo'),
]