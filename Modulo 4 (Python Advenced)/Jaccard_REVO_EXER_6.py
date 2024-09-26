suma = 3000
contador = 0

def dividir(suma, contador):
    try:
        resultado = suma / contador
        print(resultado)
    except ZeroDivisionError:
        print("División por cero")


dividir(suma, contador)