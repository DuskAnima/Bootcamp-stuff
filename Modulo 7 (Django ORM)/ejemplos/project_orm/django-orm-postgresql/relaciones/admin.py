from django.contrib import admin
from .models import Automotriz, ModeloCarro

class AutomotrizAdmin(admin.ModelAdmin):
    fields = ['nombre', 'pais']
    list_display = ('id', 'nombre', 'pais')
    list_display_links = ['nombre']
    ordering = ('nombre', 'pais')

class ModeloCarroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'automotriz', 'f_fabricacion', 'costo_fabricacion', 'precio_venta', 'costo')
    ordering = ('automotriz',)
    list_display_links = ['nombre', 'automotriz']
    list_filter = ('nombre', 'automotriz')
    list_per_page = 4

    def costo(self, obj):
        if obj.precio_venta is None:
            return 'Costo Desconocido'
        elif obj.precio_venta >= 5000:
            return 'Costo Alto'
        else:
            return 'Costo Bajo'

admin.site.register(Automotriz, AutomotrizAdmin)
admin.site.register(ModeloCarro, ModeloCarroAdmin)
