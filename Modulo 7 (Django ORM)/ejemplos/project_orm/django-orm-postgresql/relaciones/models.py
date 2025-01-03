from django.db import models
import datetime

anios_choices = []
for r in range(1950, (datetime.datetime.now().year+1)):
    anios_choices.append((r,r))

def anio_actual():
    return datetime.date.today().year

class Automotriz(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre
    
class DirectorEjecutivo(models.Model):
    automotriz = models.OneToOneField(Automotriz, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class ModeloCarro(models.Model):
    nombre = models.CharField(max_length=255)
    automotriz = models.ForeignKey(Automotriz, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=anios_choices, default=anio_actual)
    costo_fabricacion = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    precio_venta = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    tipo_combustible = models.ManyToManyField(TipoCombustible, blank=True) 


    def __str__(self):
        return self.nombre
    
