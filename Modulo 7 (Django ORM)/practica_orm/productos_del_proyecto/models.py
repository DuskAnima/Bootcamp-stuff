from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=512)
