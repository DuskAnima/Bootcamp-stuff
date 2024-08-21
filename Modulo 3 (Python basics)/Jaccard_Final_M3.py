nombres = [ #Lista de tuplas en las cuales se define profesión y nombre
    ('mago', 'Harry Houdini'),
    ('mago', 'David Blaine'),
    ('mago', 'Teller'),
    ('cientifico', 'Newton'),
    ('cientifico', 'Hawking'),
    ('cientifico', 'Einstein'),
    ('otros', 'Messi'),
    ('otros', 'Pele'),
    ('otros', 'Juanes')
]

def indexador(): # Módulo clasificador de profesiones
    magos = [] # Listas que tomarán cada valor segun el resultado de las iteraciones
    cientificos = []
    otros = []
    for profesion, nombre in nombres: # Al ser tuplas de dos valores, se puede acceder a cada valor remitiéndo a su posición
        if profesion == "mago": # Condicionales que separan en función del primer valor de la tupla
            magos.append(nombre) # Anexa a la lista el segundo valor de la tupla
        elif profesion == "cientifico":
            cientificos.append(nombre)
        else:
            otros.append(nombre)
    return magos, cientificos, otros #indexador() retorna 3 listas, las cuales deberán ser desempaquetadas asignandoles variables.

def hacer_grandioso(magos):
    magos = [print(f"El gran {mago}")for mago in magos] #Compresión de listas para imprimir magos.

def imprimir_nombres():
    magos, cientificos, otros = indexador() #Se desempaquetan 3 listas asignandoles variables para que las funciones puedan operar.
    for mago in magos: #Bucle para imprimir magos.
        print(mago)
    for cientifico in cientificos: #Bucle para imprimir cientificos.
        print(cientifico)
    for otro in otros: #Bucle para imprimir otros.
        print(otro)
    hacer_grandioso(magos) #función que imprime los magos grandiosos.

imprimir_nombres()