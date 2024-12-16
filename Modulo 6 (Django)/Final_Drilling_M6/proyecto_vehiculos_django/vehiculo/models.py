from django.db import models

BRAND_CHOICES = [
    ('ford', 'Ford'),
    ('fiat', 'Fiat'),
    ('chevrolet', 'Chevrolet'),
    ('toyota', 'Toyota'),
]
CATEGORIES_CHOICES = [
    ('particular', 'Particular'),
    ('transporte', 'Transporte'),
    ('carga', 'Carga'),
]

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, choices=BRAND_CHOICES, default='ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50, unique=True)
    serial_motor = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIES_CHOICES, default='particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ('visualizar_catalogo', 'Puede visualizar catalogo de vehículos'),
        ]

