#IMPORTANTE!
#preguntar si debo separar la lista con código o si lo separo manualmente

magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = ["Messi", "Pele", "Juanes"]

def hacer_grandioso(magos):
    magos = [print(f"El gran {mago}")for mago in magos]
    #print(magos)

#hacer_grandioso(magos)

def imprimir_nombres(magos, cientificos, otros):
    for mago in magos:
        print(mago)
    for cientifico in cientificos:
        print(cientifico)
    for otro in otros:
        print(otro)
    hacer_grandioso(magos)



imprimir_nombres(magos, cientificos, otros)

