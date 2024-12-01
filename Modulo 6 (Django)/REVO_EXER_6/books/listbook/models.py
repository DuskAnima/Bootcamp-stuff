from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

class InputBookModel(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valoracion = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10000)])
