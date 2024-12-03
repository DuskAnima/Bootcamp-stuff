from django.db import models

class InputBookModel(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valoracion = models.IntegerField(max_length=10000)
