from django.db import models

# De esta forma se puede convertir un modelo directamente en un formulario. Perfecto para aplicaciones
# basadas en Bases de datos
class BoardsModel(models.Model): #Se declara el modelo
    # Campos del modelo
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    valor = models.FloatField()
    creado = models.DateTimeField(auto_now_add= True)
    modificado = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name = 'tablero'
        verbose_name_plural = 'tableros'
        ordering = ['-creado']
        permissions = (
            ('es_miembro_1', 'Es miembro con prioridad 1'),
        )
    def __str__ (self):
        return self.titulo
    
    