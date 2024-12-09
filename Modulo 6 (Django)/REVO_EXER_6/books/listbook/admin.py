from django.contrib import admin
from .models import InputBookModel

admin.site.site_header= 'Librería'
admin.site.index_title= 'Panel de control'
admin.site.site_title= 'Administrador de libros'

class BookAdmin(admin.ModelAdmin):
    # titulo autor valoración
    readonly_fields = ('creado', 'modificado')
    list_display = ('titulo', 'autor', 'valoracion')
    search_fields = ('titulo', 'autor')
    list_filter = ('valoracion', 'modificado')




admin.site.register(InputBookModel, BookAdmin)

