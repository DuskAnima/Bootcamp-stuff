estudiantes = [ 
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]}, 
    ]


def promedio(): #Módulo para conseguir promedio y anexarlo al diccionario
    for estudiante in estudiantes:
        promedio = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
        estudiante['promedio'] = promedio

def studentStuff():
    promedio() #Se invoca la función de promedio
    for estudiante in estudiantes: #itera por la lista
        if estudiante['edad'] > 18 and estudiante['promedio'] > 85: #Define los parametros de filtro
            print(estudiante)

studentStuff()


# > Primero se dividen la lista en cada diccionario. Cada diccionario será "estudiante".
# > Luego, por cada estudiante, debo extraer sus notas respectivas
# > De esas notas debo sacar el promedio
    # > Hacer un módulo para operar con números y sacar promedios
    # > Para operar más facilmente con el promedio, se anexará como una nueva clave:valor al
# >luego debo comprobar si ese estudiante es mayor de 18 y si tiene promedio mayor a 85
# imprimir los que cumplan el criterio