from django.db import models

class Fabrica(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=100, null=True, blank=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=512)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, null=True, blank=True) # Unp a muchos. Una fabrica, muchos productos.
    f_vencimiento = models.DateField(null=True, blank=True)