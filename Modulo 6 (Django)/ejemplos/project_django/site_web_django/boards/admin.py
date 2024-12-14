from django.contrib import admin, messages
from .models import BoardsModel
####### tips 11, evitar que no-superadmins cambien permisos. ###########
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



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



#################### tips 11, evitar que no-superadmins cambien permisos.  ####################
admin.site.unregister(User) #Primero debe desregistrarse el modelo User de la app admin

@admin.register(User) # Luego se debe volver a registrar con la nueva configuración
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser'
            }
        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
        return

#####################
