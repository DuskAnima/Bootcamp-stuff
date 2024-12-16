from django.contrib import admin
from .models import InputBookModel

admin.site.site_header= 'Librería'
admin.site.index_title= 'Panel de control'
admin.site.site_title= 'Administrador de libros'

class BookAdmin(admin.ModelAdmin):
    # titulo autor valoración
    readonly_fields = ('creado', 'modificado')
    list_display = ('titulo', 'autor', 'valoracion', 'clasificacion')
    search_fields = ('titulo', 'autor')
    list_filter = ('valoracion', 'modificado')

    def clasificacion(self, obj):
        if obj.valoracion >= 2500:
            return 'alta'
        elif obj.valoracion < 2500 or obj.valoracion >= 1000:
            return 'media'
        else:
            return 'baja'

admin.site.register(InputBookModel, BookAdmin)

