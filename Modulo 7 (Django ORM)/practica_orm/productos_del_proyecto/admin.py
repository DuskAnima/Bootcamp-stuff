from django.contrib import admin
from .models import Fabrica, Producto

class FabricaAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre', 'pais') 
    list_display = ('nombre', 'pais') 
    

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('f_vencimiento', 'fabrica') 
    list_display = ('nombre', 'descripcion', 'precio', 'f_vencimiento', 'fabrica')
    search_fields = ('nombre', 'descripcion')

admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Producto, ProductoAdmin)