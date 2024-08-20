x = [[1,2,3], 
    [0,4,5], 
    [4,0,1], 
    [6,5,4]]

#Función que utiliza comprensión de listas para, primero, eliminar desde el indice y, después, elementos especificos

def zeroKiller(x):
    # filtro de sub índices que comiencen por 0
    x = [n for i, n in enumerate(x) if x[i][0] != 0] 
    # n = cambios se harán durante cada iteración
        # i = posición de cada elemento de la lista). n = valor asociado a cada posición en la lista
            # if = si, durante las iteraciones, en la lista x (indice [i], sub indice[0]), hay 
            # elementos diferente de cero !=0, estos redefinirán la lista x, excluyendo las sublistas comenzadas por 0.
#----------------------------------------------------------------------------------------------------------------------
    # filtro de valores individuales equivalentes a 0 dentro de sub índices
    x = [[i1 for i1 in i if i1 !=0]for i in x]
    # i1 cambios que se harán durante cada iteración
        # i1 = acceso iterativo de los elementos individuales de cada sub lista, i = acesso a las sublistas
        # if = si, durante la iteración de cada elemento individual de una sublista, hay elementos diferentes
        # de cero !=0, estos redefinirán su correspondiente sublista, excluyendo a cada valor de 0
        # todo este conjunto define la acción que ocurrirá en el loop for externo.
            # loop for externo: i = acceso iterativo de cada sublista para que el codigo establecido previamente
            # opere en cada iteración externa. x = acceso a la lista para iterar por las sublistas
    print(x)

zeroKiller(x)
