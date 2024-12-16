from django.contrib import admin
from .models import Vehiculo

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_de_creacion', 'fecha_de_modificacion')
    list_display = ('marca', 'modelo', 'precio')
    search_fields = ('marca', 'modelo', 'categoria')
    list_filter = ('marca', 'modelo', 'categoria')

admin.site.register(Vehiculo, VehiculoAdmin)