from django.contrib import admin, messages
from .models import BoardsModel

admin.site.site_header = 'Curso Django'
admin.site.index_title = 'Panel de control Django Project'
admin.site.site_title = 'Administrador Django'

class BoardsAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('titulo', 'clasificacion', 'valor')
    search_fields = ('titulo', 'descripcion')
    ordering = ('valor',)
    list_filter = ('creado', 'valor')

    def clasificacion(self, obj):
        return 'Alto' if obj.valor >= 5 else 'Bajo'

    def actualizar_valor_a_8(modeladmin, request, queryset):
        queryset.update(valor=8.0)
        messages.success(request, 'Valor actualizado a 8')
    admin.site.add_action(actualizar_valor_a_8, 'Colocar valor a 8')
    
admin.site.register(BoardsModel, BoardsAdmin)