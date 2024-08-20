##############IMPORTANTE!#################
#preguntar si debo separar la lista con código o si lo separo manualmente

magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = ["Messi", "Pele", "Juanes"]

def hacer_grandioso(magos):
    magos = [print(f"El gran {mago}")for mago in magos] #Compresión de listas para imprimir magos

#hacer_grandioso(magos)

def imprimir_nombres(magos, cientificos, otros):
    for mago in magos: #Bucle para imprimir magos
        print(mago)
    for cientifico in cientificos: #Bucle para imprimir cientificos
        print(cientifico)
    for otro in otros: #Bucle para imprimir otros
        print(otro)
    hacer_grandioso(magos)

imprimir_nombres(magos, cientificos, otros)


"""
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y Einstein son científicos. 
Debemos separar los nombres en tres grupos: magos, científicos y otros; y escribir una función llamada hacer_grandioso(), 
que modifique la lista de magos añadiendo la frase 'El gran' antes del nombre de cada mago. Crear una función llamada 
imprimir_nombres(), que imprime el nombre de cada persona de la lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego imprimir los nombres de 
los magos grandiosos, los nombres de los científicos, y los restantes
"""