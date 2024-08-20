a = 3
b = 2

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

def tuplizador(a, b):
    sum = suma(a,b)
    rest = resta(a,b)
    multi = multiplicacion(a,b)
    divi = division(a,b)
    return sum,rest,multi,divi

def diccionarizador(a,b):
    c = tuplizador(a,b)
    diccionario = {}
    diccionario['suma'] = c[0]
    diccionario['resta'] = c[1]
    diccionario['multiplicación'] = c[2]
    diccionario['división'] = c[3]
    print(diccionario)

diccionarizador(a, b)
