from django.db import models
from django.contrib.auth.models import User

class Proveedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    horarios = models.CharField(max_length=256)
    telefono = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=512)
    foto = models.ImageField(upload_to='fotos_proveedores/', null=True, blank=True)
    user = models.OneToOneField(User, models.CASCADE)

    class Meta:
        db_table = 'ayudante_proveedor'

class ProveedorMensaje(models.Model):
    id = models.BigAutoField(primary_key=True)
    mensaje = models.CharField(max_length=512)
    fecha_registro = models.DateField()
    proveedor = models.ForeignKey(Proveedor, models.CASCADE)

    class Meta:
        db_table = 'ayudante_proveedormensaje'


class ProveedorServicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, models.CASCADE)
    servicio = models.ForeignKey('Servicio', models.CASCADE)

    class Meta:
        db_table = 'ayudante_proveedorservicio'


class Servicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=128)

    class Meta:
        db_table = 'ayudante_servicio'
    
    def __str__(self):
        return self.nombre