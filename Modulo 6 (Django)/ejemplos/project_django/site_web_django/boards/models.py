from django.db import models

# De esta forma se puede convertir un modelo directamente en un formulario. Perfecto para aplicaciones
# basadas en Bases de datos
class BoardsModel(models.Model): #Se declara el modelo
    # Campos del modelo
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    modificado = models.DateTimeField(auto_now_add= True)

    def __str__ (self):
        return self.titulo
    