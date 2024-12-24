from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=256)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=128)
    descripción = models.CharField(max_length=256)
    fecha_de_lanzamiento = models.DateField
    categoria = models.ForeignKey(Categoria,
                                on_delete=models.PROTECT)
    
#La mayoría de los projectos comienzan por la definición del modelo.
#Luego de la definición del modelo, lo siguiente (usualmente) es la definición de las URLS